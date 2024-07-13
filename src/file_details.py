#this class finds and loads the input datasets and metrics associated with it

import os
import glob
import yaml

class File_details:

    def __init__(self, parameters_path) -> None:
        self.parameters_path = parameters_path
        self.parameters = self.load_parameters()

    def load_parameters(self):
        with open(self.parameters_path, 'r') as file:
            return yaml.safe_load(file)
    
    def get_csv_paths(self):
        # Define paths to 'current' and 'reference' folders
        parent_folder = os.path.join('..', 'data', 'dataset', self.parameters['folder'])
        current_folder = os.path.join(parent_folder, 'current')
        reference_folder = os.path.join(parent_folder, 'reference')

        # Check if 'current' and 'reference' folders exist
        if not os.path.isdir(current_folder):
            raise FileNotFoundError(f"'{current_folder}' folder does not exist.")
        if not os.path.isdir(reference_folder):
            raise FileNotFoundError(f"'{reference_folder}' folder does not exist.")

        current_csv_file = glob.glob(os.path.join(current_folder, '*.csv'))
        reference_csv_file = glob.glob(os.path.join(reference_folder, '*.csv'))

        if not current_csv_file:
            raise FileNotFoundError(f"No CSV files found in '{current_folder}' folder.")
        if not reference_csv_file:
            raise FileNotFoundError(f"No CSV files found in '{reference_folder}' folder.")

        return current_csv_file[0], reference_csv_file[0]

    def get_input(self):

        # Access the parameters
        folder = self.parameters['folder']
        cur_filename, ref_filename = self.get_csv_paths()
        target = self.parameters['target']
        prediction = self.parameters['prediction']
        type = self.parameters['report_type']
        numerical_columns = self.parameters['numerical_columns']
        categorical_columns = self.parameters['categorical_columns']
        return folder, ref_filename, cur_filename, target, prediction, type, numerical_columns, categorical_columns


