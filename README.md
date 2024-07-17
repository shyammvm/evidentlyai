# Evidently AI POC
## Overview
This project demonstrates the use of Evidently AI for generating various types of reports based on your datasets. Evidently AI helps evaluate, test, and monitor data and machine learning (ML) systems. Evidently AI reports compute different metrics on data and ML quality, facilitating visual analysis and debugging, as well as serving as a computational layer for monitoring dashboards. The reports are saved in .json format, making them easy to visualize with tools like Tableau. Below are the types of reports that can be generated using this project:

| **Metric**          | **Description**                                      | **Requirements**                       |
|---------------------|------------------------------------------------------|----------------------------------------|
| **Data Quality**    | Shows the dataset statistics and feature behavior.   | Model inputs                           |
| **Data Drift**      | Explores the distribution shift in the model features.| Model inputs, a reference dataset      |
| **Target Drift**    | Explores the distribution shift in the model predictions or target.| Model predictions and/or target, a reference dataset |
| **Classification**  | Evaluates the classification model quality and errors.| Model predictions and true labels      |
| **Regression**      | Evaluates the regression model quality and errors.   | Model predictions and actuals          |

## Setup Instructions
Follow the steps below to set up the project and generate the reports.

### Copy the Dataset Folder:
Copy your dataset folder to the data/dataset directory.
The dataset folder should contain two subdirectories: current and reference.

### Organize the Datasets:
Place the current dataset CSV file in the current directory.
Place the reference dataset CSV file in the reference directory.
Ensure that both current and reference datasets contain the same columns.

### Edit the Configuration File:
Navigate to the data directory and edit the parameter.yaml file to include all the required input details.

### YAML Configuration Details (parameter.yaml)
<b> folder: </b> The dataset folder name<br>
<b> target: </b>The target value column<br>
<b>prediction: </b> The predicted value column<br>
<b>report_type:</b> The type of report to be generated.<br>Options include:
  - classification<br>
  - regression<br>
  - data_quality<br>
  - data_drift<br>
  - target_drift<br>

<b>numerical_columns:</b> Columns containing numerical values<br>
<b>categorical_columns:</b> Columns containing categorical values<br>

you can create multiple inputs by mentioning different folder names and their corresponding values

### Example Configuration (parameter.yaml)
```
  - folder: "adult"
    target: "income"
    prediction: "predicted_income"
    report_type: "data_quality"
    numerical_columns:
      - "age"
      - "fnlwgt"
      - "education-num"
      - "capital-gain"
      - "capital-loss"
      - "hours-per-week"
    categorical_columns:
      - "workclass"
      - "education"
      - "marital-status"
      - "occupation"
      - "relationship"
      - "race"
      - "sex"
      - "native-country"
      - "class"
  - folder :
    ------
```
### Ensure Consistency:
Verify that both the current and reference datasets have the same columns.

### Run the Script:
Execute the src/main.py script to generate the report.
<code>
python src/main.py
</code>

### Access the Report:
The generated report will be saved as JSON file in the reports folder within the data directory. A new folder with the dataset name will be created inside which all the corresponding reports will be saved.

### Directory Structure
The directory structure should look like this:

```
evidentlyai/
├── data/
│   ├── dataset/
│   │   └── <dataset_folder>/
│   │       ├── current/
│   │       │   └── <current_dataset>.csv
│   │       └── reference/
│   │           └── <reference_dataset>.csv
│   └── parameter.yaml
├── reports/
│   └── <dataset_folder>/
│       └── <generated_report_timestamp>.json
├── src/
│   ├── main.py
│   ├── file_details.py
│   └── reports.py
└── README.md
└── requirements.txt
```

### Requirements
- Python 3.8+<br>
- pandas library<br>
- PyYAML library<br>
- glob library<br>

### Install Dependencies
In the root folder of the project, run the following command

<code>pip install -r requirements.txt</code>

### Script Descriptions
<code>src/main.py</code>
This is the main script that orchestrates the report generation process. It reads inputs from the parameter.yaml file, loads the datasets, and generates the specified report.

<code>src/file_details.py</code>
This script handles the loading and validation of the input datasets based on the configuration provided in the parameter.yaml file.

<code>src/reports.py</code>
This script contains the logic for generating various types of reports using Evidently AI.

### Running the Example
- Place your dataset folders in the data/dataset directory.

- Edit the parameter.yaml file to include your dataset details.

- Run the main script: <code>python src/main.py</code>
The report will be generated and saved in the reports folder inside your dataset folder.

## Troubleshooting
### File Not Found: 
Ensure the paths in parameter.yaml are correct and the datasets are placed in the respective directories.
### Invalid File Format:
Ensure the datasets are in CSV format and the columns match between the current and reference datasets.
For further assistance, please refer to the Evidently AI documentation.