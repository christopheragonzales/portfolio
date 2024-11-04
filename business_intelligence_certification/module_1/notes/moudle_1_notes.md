# Module 1 Notes

## Table of Contents
- [How Business Intelligence Makes an Impact](#how-business-intelligence-makes-an-impact)
- [Key Business Intelligence Documents](#key-business-intelligence-documents)
  - [Stakeholder Requirements Document](#stakeholder-requirements-document)
  - [Project Requirements Document](#project-requirements-document)
  - [Strategy Document](#strategy-document)
- [The Business Intelligence Professional's Toolbox](#the-business-intelligence-professionals-toolbox)
- [Review Technologies and Best Practices](#review-technologies-and-best-practices)
  - [Optimal Pipeline Processes](#optimal-pipeline-processes)
    - [Modular Design](#modular-design)
    - [Verify Data Accuracy and Integrity](#verify-data-accuracy-and-integrity)
    - [Creating a Testing Environment](#creating-a-testing-environment)
  - [Dynamic Dashboards](#dynamic-dashboards)
    - [Dashboards are Part of a Business Journey](#dashboards-are-part-of-a-business-journey)
  - [Effective Visualizations](#effective-visualizations)
    - [Frameworks for Organzing Your Thoughts about Visualizations](#frameworks-for-organizing-your-thoughts-about-visualizations)
    - [Pre-attentive Attributes: Marks and Channels](#pre-attentive-attributes-marks-and-channels)
    - [Design Principles](#design-principles)
    - [Avoiding Misleading or Deceptive Charts](#avoiding-misleading-or-deceptive-charts)

## How Business Intelligence Makes an Impact
- [Key Business Intelligence Documents](#key-business-intelligence-documents)

## Key Business Intelligence Documents
- [Stakeholder Requirements Document](#stakeholder-requirements-document)
- [Project Requirements Document](#project-requirements-document)
- [Strategy Document](#strategy-document)

Previously, you learned about business intelligence strategy, which is the management of the people, processes, and tools used in the business intelligence process. BI projects are complicated, and finding ways to stay organized from the beginning of a project to the end is key to success. One way to ensure that you capture the big-picture project requirements, stay organized, and make an impact at your organization is to create comprehensive BI documents. In this reading, you’ll learn about three types of documents: the Stakeholder Requirements Document, Project Requirements Document, and Strategy Document.

Each of these documents builds on the previous one. Instead of three separate documents, think about them as three phases of your project planning process. Later on, you will have an opportunity to create your own BI documents to guide your end-of-course project, so this is a great resource to get you started!

#### Stakeholder Requirements Document

The Stakeholder Requirements Document enables you to capture stakeholder requests and requirements so you understand their needs before planning the rest of the project details or strategy. It should answer the following questions:

- Business problem: What is the primary question to be answered or      problem to be solved?
- Stakeholders: Who are the major stakeholders of this project, and what are their job titles?
- Stakeholder usage details: How will the stakeholders use the BI tool?
- Primary requirements: What requirements must be met by this BI tool in order for this project to be successful?

Here are some questions BI professionals ask in order to successfully complete this document:

- What questions must be answered before starting this project?
- What does the BI team need to know before starting this project?
- What are the questions that must be answered/problems that must be solved by this project?
- What datasets are considered important to this project?
- Who should have access to the dashboard? Will the entire dashboard be visible to all stakeholders?

Typically, the Stakeholder Requirements Document is a one-pager with notes, but it can be longer and more detailed for complex projects.

Click the [link](https://docs.google.com/document/d/11K4eqc_rhZql__yg9sqDYFP5GnV1dAkHr36NqIUyG5I/template/preview) to access the stakeholder requirements document template. 

#### Project Requirements Document

Once you have established the stakeholder requirements, you can start thinking about the project requirements that need to be met to achieve the stakeholder requirements. The Project Requirements Document contains the following details:

- Purpose: Briefly describe why this project is happening and explanation of why the company should invest its resources in it.
- Key dependencies: Detail the major elements of this project. 
    - Include the team, primary contacts, and expected deliverables.
    - Are there any inter-team deliverables required?
- Stakeholder requirements: List the established stakeholder requirements, based on the Stakeholder Requirements Document. Prioritize the requirements as: R - required, D - desired, or N - nice to have.
- Success criteria: Clarify what success looks like for this project. Include explicit statements about how to measure success. Use SMART criteria.
- User journeys: Document the current user experience and the ideal future experience.
- Assumptions: Explicitly and clearly state any assumptions you are making.
- Compliance and privacy: Include compliance, privacy, or legal dimensions to consider.
- Accessibility: List key considerations for creating accessible reports for all users. Who needs to access this feature? How are they viewing and interacting with it?
- Roll-out plan: Briefly describe the expected scope, priorities and timeline. 
    - Consider at what points during the rollout will measurements be made to determine whether the feature is performing as expected? 
    - Is there a rollback plan and timeline if this feature does not meet its intended goals?

In addition, some companies will ask you to include a list of references. If so, it’s a best practice to be liberal in citing references; you can never have too many. References might include:

- Documents or websites you read and researched while working on this project
- Laws and policies: Any regulations driving the project requirements
- Project tracking: A link to tracking spreadsheet, bug hotlist, etc.
- Similar projects: A description of anything similar that has been attempted in the past or any parallel efforts.

Similar to the Stakeholder Requirements Document, the Project Requirements Document will vary depending on the complexity of the project. It might just be an email sent out to stakeholders to keep them updated on expectations and check-in points, or it could be a multi-page document with a spreadsheet that outlines the project plan and key tasks.

Click the [link](https://docs.google.com/document/d/1Vq9G_MAQRz4V6iZF_Z-v_u0AcwloB96lc6wwYzz9EDg/template/preview) to access the project requirements document template.

#### Strategy Document

Finally, you will create a Strategy Document for your project. This is the final phase of the planning process. The Strategy Document is a collaborative place to align with stakeholders about project deliverables. You will work together to establish information about dashboard functionality and associated metrics and charts.

This is a time to flesh out what metrics will be required, how metrics are calculated, and any limitations or assumptions that exist about the data. Stakeholders think through these details and help the BI professional make final project decisions. Then, the BI professional provides stakeholders with a dashboard mockup to get valuable feedback.

Generally, the BI professional will create the document and request review and sign-off from important stakeholders. Then they can begin working on the project with all of the details they need.

Click the [link](https://docs.google.com/document/d/13v9_pOAHbcv2dhEMZtPFJ6sgvZaY-9tVp1op32owAdE/template/preview) to access the strategy document template.

Staying organized and aligned with stakeholders is an important part of the BI process. Creating documents early on in a project to outline stakeholder and project requirements as well as project strategies can be an important tool for a BI professional aligning with stakeholders and planning ahead. Soon, you’ll have an opportunity to create your own documents to align with stakeholders and plan your end-of-course project!

## The Business Intelligence Professional’s Toolbox

Business intelligence (BI) has been a guiding tool for leaders for centuries, with the term dating back to 1865, when it was used to describe the success of a banker, Sir Henry Furnace, who leveraged timely data to stay ahead of competitors. Modern BI continues this tradition, now encompassing essential tools to navigate the data landscape:

- Data Model: The foundation of BI, organizing data elements and their relationships to maintain consistency and clarity across systems.
- Data Pipeline: A process that moves data from various sources to a destination for analysis. BI professionals transform data along this path, often using ETL (Extract, Transform, Load) for integrating data from multiple sources.
- Data Visualizations: Graphical representations of data, made accessible through tools like Tableau and Looker, enabling non-experts to understand insights quickly.
- Dashboards: Interactive tools that monitor live data, similar to train dashboards, allowing users to track key metrics in real time.

Iteration is a core BI principle, encouraging continuous improvement of BI tools and processes, just as railway systems are routinely evaluated and upgraded. This iterative approach helps BI professionals enhance their impact by refining and advancing their methods.

## Review Technologies and Best Practices
- [Optimal Pipeline Processes](#optimal-pipeline-processes)
  - [Modular Design](#modular-design)
  - [Verify Data Accuracy and Integrity](#verify-data-accuracy-and-integrity)
  - [Creating a Testing Environment](#creating-a-testing-environment)
- [Dynamic Dashboards](#dynamic-dashboards)
  - [Dashboards are Part of a Business Journey](#dashboards-are-part-of-a-business-journey)
- [Effective Visualizations](#effective-visualizations)
  - [Frameworks for Organzing Your Thoughts about Visualizations](#frameworks-for-organizing-your-thoughts-about-visualizations)
  - [Pre-attentive Attributes: Marks and Channels](#pre-attentive-attributes-marks-and-channels)
  - [Design Principles](#design-principles)
  - [Avoiding Misleading or Deceptive Charts](#avoiding-misleading-or-deceptive-charts)


As you continue through this program, you will be introduced to a variety of business intelligence tools that will help you create systems and processes and provide stakeholders with insights they can use to guide business decisions. Depending on the organization, you might end up using different tools over time. Luckily, the skills you are learning now can be transferred between tools. In this reading, you’ll be given some best practices for creating pipeline tools, data visualizations, and dashboards that you’ll be able to apply no matter what programs or tools your organization uses. 

### Optimal Pipeline Processes
- [Modular Design](#modular-design)
- [Verify Data Accuracy and Integrity](#verify-data-accuracy-and-integrity)
- [Creating a Testing Environment](#creating-a-testing-environment)
#### Modular Design
#### Verify Data Accuracy and Integrity
#### Creating a Testing Environment
### Dynamic Dashboards
- [Dashboards are Part of a Business Journey](#dashboards-are-part-of-a-business-journey)
#### Dashboards are Part of a Business Journey
### Effective Visualizations
- [Frameworks for Organzing Your Thoughts about Visualizations](#frameworks-for-organizing-your-thoughts-about-visualizations)
- [Pre-attentive Attributes: Marks and Channels](#pre-attentive-attributes-marks-and-channels)
- [Design Principles](#design-principles)
- [Avoiding Misleading or Deceptive Charts](#avoiding-misleading-or-deceptive-charts)
#### Frameworks for Organizing Your Thoughts about Visualizations
#### Pre-attentive Attributes: Marks and Channels
#### Design Principles
#### Avoiding Misleading or Deceptive Charts
