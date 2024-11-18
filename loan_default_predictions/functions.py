import pandas as pd
import numpy as np
import scipy.stats as stats
import json
import os

import matplotlib.pyplot as plt
import seaborn as sns

import re
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split

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

def select_most_important_features(x_variable, y_variable, data, threshold="mean"):
    X = data[[x for x in data.columns if f"{x_variable}" in x]]
    
    # Initialize and fit ExtraTreesClassifier
    clf = ExtraTreesClassifier(n_estimators=100, random_state=42, class_weight="balanced")
    clf.fit(X, y_variable)
    
    # Select features based on importance threshold
    sfm = SelectFromModel(clf, threshold=threshold, prefit=True)
    important_features = X.loc[:, sfm.get_support()]
    
    return important_features

def select_all_features(categorical_variables, y_variable, df, threshold="mean"):
    X_dataframe = pd.DataFrame()
    
    for categorical_variable in categorical_variables:
        important_features = select_most_important_features(categorical_variable, y_variable, df, threshold=threshold)
        X_dataframe = pd.concat([X_dataframe, important_features], axis=1)
    
    X_dataframe.sort_index(axis=1, inplace=True)
    X_dataframe.reset_index(drop=True, inplace=True)
    return X_dataframe

def split_data(X, y):
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    X_test, X_val, y_test, y_val = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)

    print(f"Percent in Training Set: {len(X_train) / len(X) * 100:.2f}%")
    print(f"Percent in Test Set: {len(X_test) / len(X) * 100:.2f}%")
    print(f"Percent in Validation Set: {len(X_val) / len(X) * 100:.2f}%")

    return X_train, X_test, X_val, y_train, y_test, y_val

def bin_continuous_variable(field, num_cuts, df):
    try:
        # Perform equal-frequency binning
        series, bin_edges = pd.qcut(df[field], q=num_cuts, retbins=True, labels=np.arange(num_cuts))
    except ValueError as e:
        print(f"Error while binning {field}: {e}")
        return None

    # Create a dictionary of bin ranges
    bin_dict = {}
    for i in range(num_cuts):
        left_bound = bin_edges[i]
        right_bound = bin_edges[i + 1]
        bin_dict[f"bin_{i}"] = {"lower_bound": left_bound, "upper_bound": right_bound}

    # Save the bin information as a JSON file
    os.makedirs("json_bins", exist_ok=True)
    file_name = f"json_bins/{field}_binned.json"

    with open(file_name, "w") as f:
        json.dump(bin_dict, f, indent=4)

    print(f"Binning information for {field} saved to {file_name}")

    return series