#this class finds and loads the input datasets and metrics associated with it

import os

class File_details:

    def __init__(self, parameters_path) -> None:
        self.parameters_path = parameters_path
        self.curr_dir = os.getcwd()

    def parse_line(self, line):
        key, value = line.split('=')
        key = key.strip()
        value = value.strip()
        
        # Convert value to a list if it contains commas, otherwise leave it as a single value
        if key == 'numerical' or key == 'categorical':
            if value == '':
                value = None  # Set to None if value is empty
            else:
                value = [item.strip() for item in value.split(',')]
        return key, value

    def get_input(self):
        # Dictionary to store the parameters
        parameters = {}
        # Open the file and read the lines into the dictionary
        with open(self.parameters_path, 'r') as file:
            for line in file:
                key, value = self.parse_line(line)
                parameters[key] = value

        # Access the parameters
        ref_filename = parameters.get('ref_filename')
        cur_filename = parameters.get('cur_filename')
        target = parameters.get('target')
        prediction = parameters.get('prediction')
        type = parameters.get('model_type')
        numerical_columns = parameters.get('numerical')
        categorical_columns = parameters.get('categorical')
        print(ref_filename)
        return ref_filename, cur_filename, target, prediction, type, numerical_columns, categorical_columns
        # dataset_location = os.path.join(self.curr_dir, "data\\dataset")


