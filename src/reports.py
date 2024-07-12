import pandas as pd
import numpy as np
import os
import datetime

from sklearn import datasets, ensemble, model_selection

from evidently import ColumnMapping
from evidently.test_suite import TestSuite

from evidently.test_preset import NoTargetPerformanceTestPreset
from evidently.test_preset import DataQualityTestPreset
from evidently.test_preset import DataStabilityTestPreset
from evidently.test_preset import DataDriftTestPreset
from evidently.test_preset import RegressionTestPreset
from evidently.test_preset import MulticlassClassificationTestPreset
from evidently.test_preset import BinaryClassificationTopKTestPreset
from evidently.test_preset import BinaryClassificationTestPreset
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset, DataQualityPreset, ClassificationPreset, RegressionPreset


class Reports:
    
    def __init__(self, ref_file, cur_file, target, prediction, numerical_columns, categorical_columns, type) -> None:
        dataset_path = os.path.join('..', 'data', 'dataset')
        self.ref_file = pd.read_csv(os.path.join(dataset_path, ref_file))
        self.cur_file = pd.read_csv(os.path.join(dataset_path, cur_file))
        self.target = target
        self.prediction = prediction
        self.numerical_cols = numerical_columns
        self.categorical_cols = categorical_columns
        self.type = type
    
    def db_check(self):
        if self.ref_file.shape != self.cur_file.shape:
            raise ValueError('Make sure the databases have the same shape')
        return True

    def columnmapping(self):
        columnmapping = ColumnMapping()
        columnmapping.target = self.target
        columnmapping.prediction = self.prediction
        columnmapping.numerical_features = self.numerical_cols
        columnmapping.categorical_features = self.categorical_cols
        return columnmapping

    def classification_performance_report_generator(self):
        classification_performance_report = Report(metrics=[ClassificationPreset()])
        classification_performance_report.run(
            reference_data = self.ref_file,
            current_data = self.cur_file,
            column_mapping = self.columnmapping()
        )
        return classification_performance_report 
    
    def regression_performance_report_generator(self):
        regression_performance_report = Report(metrics=[RegressionPreset()])
        regression_performance_report.run(
            reference_data = self.ref_file,
            current_data = self.cur_file,
            column_mapping = self.columnmapping()
        )
        return regression_performance_report
  
    def get_report(self):
        if self.type == 'binary_classification':
            if self.db_check():
                report = self.classification_performance_report_generator()
        elif self.type == 'regression':
            if self.db_check():
                report = self.regression_performance_report_generator()       
        reportname = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.json'
        report_path = os.path.join('..', 'data', 'reports', reportname)
        report.save_json(report_path)