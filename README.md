Evidently AI POC
Overview
This project demonstrates the use of Evidently AI for generating various types of reports based on your datasets. Follow the steps below to set up the project and generate the reports.

Setup Instructions

Copy the Dataset Folder:
Copy your dataset folder to the data/dataset directory.
The dataset folder should contain two subdirectories: current and reference.

Organize the Datasets:
Place the current dataset CSV file in the current directory.
Place the reference dataset CSV file in the reference directory.
Ensure that both current and reference datasets contain the same columns.

Edit the Configuration File:
Navigate to the data directory and edit the parameter.yaml file to include all the required input details.

YAML Configuration Details (parameter.yaml)
folder: The dataset folder name
target: The target value column
prediction: The predicted value column
report_type: The type of report to be generated. Options include:
classification
regression
data_quality
data_drift
target_drift
numerical_columns: Columns containing numerical values
categorical_columns: Columns containing categorical values

Example Configuration (parameter.yaml)
yaml
Copy code
folder: "adult"
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
  
Ensure Consistency:
Verify that both the current and reference datasets have the same columns.

Run the Script:
Execute the src/main.py script to generate the report.
sh
Copy code
python src/main.py

Access the Report:
The generated report will be saved in the reports folder within the given dataset folder.

Directory Structure
The directory structure should look like this:

php
Copy code
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
│       └── <generated_report>.json
├── src/
│   ├── main.py
│   ├── file_details.py
│   └── reports.py
└── README.md

Requirements
Python 3.8+
pandas library
PyYAML library
glob library
Install Dependencies
sh
Copy code
pip install pandas pyyaml glob2

Script Descriptions
src/main.py
This is the main script that orchestrates the report generation process. It reads inputs from the parameter.yaml file, loads the datasets, and generates the specified report.

src/file_details.py
This script handles the loading and validation of the input datasets based on the configuration provided in the parameter.yaml file.

src/reports.py
This script contains the logic for generating various types of reports using Evidently AI.

Running the Example
Place your dataset folders in the data/dataset directory.

Edit the parameter.yaml file to include your dataset details.

Run the main script:

sh
Copy code
python src/main.py
The report will be generated and saved in the reports folder inside your dataset folder.

Troubleshooting
File Not Found: Ensure the paths in parameter.yaml are correct and the datasets are placed in the respective directories.
Invalid File Format: Ensure the datasets are in CSV format and the columns match between the current and reference datasets.
For further assistance, please refer to the Evidently AI documentation.