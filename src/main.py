from file_details import File_details
from reports import Reports
import os

def main():
    #get input parameters
    parameters_path = os.path.join('..', 'data', 'parameters.yaml')
    input_details = File_details(parameters_path) # initialize the file parameters processing class
    inputs = input_details.get_input() # get inputs as a list of lists, each element contains the details of each dataset

    #get report
    for input in inputs: #iterate over all the input datasets
        folder, ref_filename, cur_filename, target, prediction, type, numerical_columns, categorical_columns = input
        report_obj = Reports(folder=folder, cur_file=cur_filename, ref_file=ref_filename, target=target, prediction=prediction, numerical_columns=numerical_columns, categorical_columns=categorical_columns, type=type) # initialize the report class
        report = report_obj.get_report() #generate the report
        report_obj.save_report(report) #save the report

if __name__ == "__main__":
    main()