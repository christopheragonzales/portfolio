import pandas as pd
import scipy.stats as stats
import os

import matplotlib.pyplot as plt
import seaborn as sns

import re
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

def run_chi2_test(ind_variable, dep_variable, df):
    # Create a contingency table
    contingency_table = pd.crosstab(df[ind_variable], df[dep_variable])
    contingency_table.columns = ["No Default", "Default"]  # Adjust this as needed for your data

    # Run the chi-squared test
    chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
    
    # Print results
    print("Chi-Squared Test Results:")
    print(f"\tChi-Squared Statistic: {chi2:.4f}")
    print(f"\tP-Value: {p}")
    print(f"\tDegrees of Freedom: {dof}")

    # Interpretation based on p-value
    if p < 0.05:
        print("\nResult: There is a statistically significant association between the variables.")
    else:
        print("\nResult: No statistically significant association between the variables.")

def generate_barplot(x_variable, y_variable, data, x_name=None, y_name=None):
    # Set default names if none provided
    if x_name is None:
        x_name = x_variable.replace("_", ' ').title()

    if y_name is None:
        y_name = y_variable.replace("_", " ").title()

    # Remove 'observed' parameter from groupby()
    order = list(data.groupby(x_variable, observed=False)[y_variable].mean().sort_values(ascending=False).index)

    # Ensure the 'graphs' directory exists
    os.makedirs("graphs", exist_ok=True)

    # Create the bar plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title(f"{y_name} Rate for {x_name}", fontsize=16)
    sns.barplot(x=x_variable, y=y_variable, data=data, order=order)

    # Add mean line with label
    mean_value = data[y_variable].mean()
    ax.axhline(mean_value, color='k', ls='--', label=f'Mean {y_name} Rate ({mean_value:.4f})')
    ax.legend()

    # Label axes
    ax.set_xlabel(x_name, fontsize=14)
    ax.set_ylabel(f"% {y_name}", fontsize=14)

    # Save and show the plot
    plt.tight_layout()
    plt.savefig(f"graphs/barplot_of_{x_variable}.png")
    plt.show()
    plt.close()

def generate_boxplot(x_variable, y_variable, data, field_name=None):
    if field_name is None:
        field_name = x_variable.replace("_", " ").title()

    # Ensure the 'graphs' directory exists
    os.makedirs("graphs", exist_ok=True)

    fig, ax = plt.subplots(2, 1, figsize=(12,8), sharex=True)

    ax[0].set_title(f"Box Plot of {field_name}", fontsize=14)
    sns.boxplot(x=x_variable, data=data, ax=ax[0])

    ax[0].grid()

    ax[1].set_title(f"Box Plot of {field_name}, Default Status", fontsize=14)
    sns.boxplot(x=x_variable, data=data, hue=y_variable, ax=ax[1])

    ax[1].grid()
    ax[1].legend(title='Default', loc='lower left')

    plt.xlabel(f"{field_name}", fontsize=12)

    plt.tight_layout()
    plt.savefig(f"graphs/boxplot_of_{x_variable}.png")
    plt.show()
    plt.close()
    
def clean_string(field, df):
    series = pd.Series(df[field])

    # Remove apostrophes
    series = series.str.replace("'", '', regex=False)

    # Replace all non-alphanumeric characters (except underscores) with underscores
    special_char_pat = r'[^\w\s]|[^\w_]'
    special_char_repl = '_'

    series = series.str.replace(special_char_pat, special_char_repl, regex=True)

    # Remove any leading or trailing whitespaces
    series = series.str.strip()

    # Replace any whitespace character with an underscore
    white_space_pat = r'\s+'
    white_space_repl = '_'

    series = series.str.replace(white_space_pat, white_space_repl, regex=True)

    # Replace multiple underscores with a single underscore
    multi_us_pat = r'_+'
    multi_us_repl = '_'

    series = series.str.replace(multi_us_pat, multi_us_repl, regex=True)

    # Cast values to upper
    series = series.str.upper()

    return series

def clean_binary(variable, df):
    series = pd.Series(df[variable])
    series = series.str.upper()

    mapping = {"NO": 0.0, "YES": 1.0}

    series = series.map(mapping)

    return series

def scale_data(field, data, scaler):
    if scaler == "standard":
        scaler = StandardScaler()
    elif scaler == "ordinal":
        scaler = OrdinalEncoder()

    series = pd.Series(data[field])
    transformed_series = scaler.fit_transform(X=series.to_frame()).flatten()

    return transformed_series

def select_most_important_features(x_variable, y_variable, data):
    X = data[[x for x in data.columns if f"{x_variable}" in x]]

    clf = ExtraTreesClassifier(n_estimators=50)
    clf.fit(X, y_variable)

    sfm = SelectFromModel(clf, prefit=True)
    important_features = X.loc[:, sfm.get_support()]

    return important_features

def select_all_features(x_variables, y_variable, data):
    X_dataframe = pd.DataFrame()

    for variable in x_variables:
        important_features = select_most_important_features(
            variable, y_variable, data
        )
        