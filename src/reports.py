import pandas as pd
import numpy as np
import os
import datetime

from sklearn import datasets, ensemble, model_selection

from evidently import ColumnMapping
from evidently.test_suite import TestSuite

# from evidently.test_preset import NoTargetPerformanceTestPreset
# from evidently.test_preset import DataQualityTestPreset
# from evidently.test_preset import DataStabilityTestPreset
# from evidently.test_preset import DataDriftTestPreset
# from evidently.test_preset import RegressionTestPreset
# from evidently.test_preset import MulticlassClassificationTestPreset
# from evidently.test_preset import BinaryClassificationTopKTestPreset
# from evidently.test_preset import BinaryClassificationTestPreset
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset, DataQualityPreset, ClassificationPreset, RegressionPreset


class Reports:
    
    def __init__(self, folder, ref_file, cur_file, target, prediction, numerical_columns, categorical_columns, type) -> None:
        self.folder = folder
        self.ref_file = pd.read_csv(ref_file)
        self.cur_file = pd.read_csv(cur_file)
        self.target = target
        self.prediction = prediction
        self.numerical_cols = numerical_columns
        self.categorical_cols = categorical_columns
        self.type = type
    
    def db_check(self): #check if the columns of the current and reference files are the same
        if list(self.ref_file.columns) != list(self.cur_file.columns):
            raise ValueError("Make sure the databases have the same columns")
        return True

    def columnmapping(self): #column mapping for generating report
        columnmapping = ColumnMapping()
        columnmapping.target = self.target
        columnmapping.prediction = self.prediction
        columnmapping.numerical_features = self.numerical_cols
        columnmapping.categorical_features = self.categorical_cols
        return columnmapping
    
    def classification_performance_report_generator(self): #classification report
        classification_performance_report = Report(metrics=[ClassificationPreset()])
        classification_performance_report.run(
            reference_data = self.ref_file,
            current_data = self.cur_file,
            column_mapping = self.columnmapping()
        )
        return classification_performance_report 
    
    def regression_performance_report_generator(self): #regression report
        regression_performance_report = Report(metrics=[RegressionPreset()])
        regression_performance_report.run(
            reference_data = self.ref_file,
            current_data = self.cur_file,
            column_mapping = self.columnmapping()
        )
        return regression_performance_report
    
    def target_drift_report_generator(self): #target drift report
        target_drift_report = Report(metrics=[TargetDriftPreset()])
        target_drift_report.run(
            reference_data=self.ref_file,
            current_data=self.cur_file,
            column_mapping=self.columnmapping()
        )
        return target_drift_report

    def data_drift_report_generator(self): #data drift report
        data_drift_report = Report(metrics=[DataDriftPreset()])
        data_drift_report.run(
            reference_data = self.ref_file,
            current_data = self.cur_file,
            column_mapping=self.columnmapping()
        )
        return data_drift_report
  
    def data_quality_report_generator(self): #data quality report
        data_quality_report = Report(metrics=[DataQualityPreset()])
        data_quality_report.run(
            reference_data=self.ref_file,
            current_data=self.cur_file,
            column_mapping=self.columnmapping()
        )
        return data_quality_report

    def save_report(self, report):
        reportname = self.folder + '_' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.json' #concatenate the dataset name with the current timestamp 
        report_folder = os.path.join('..', 'data', 'reports', self.folder)
        if not os.path.exists(report_folder): #create a folder inside the reports directory with the name of the dataset
            os.makedirs(report_folder)
        report_path = os.path.join(report_folder, reportname)
        report.save_json(report_path) #save report

    def get_report(self):
        report_generators = {
            'classification': self.classification_performance_report_generator,
            'regression': self.regression_performance_report_generator,
            'data_quality': self.data_quality_report_generator,
            'target_drift': self.target_drift_report_generator,
            'data_drift': self.data_drift_report_generator
        }

        if self.db_check() and self.type in report_generators: #check type in the parameters.yaml to find the type of report
            report = report_generators[self.type]()
            return report
        else:
            # Handle the case where type is not recognized or db_check fails
            raise ValueError(f"Invalid report type '{self.type}' or database check failed.")
    
    