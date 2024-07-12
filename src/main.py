from file_details import File_details
from reports import Reports
import os

def main():
    #get input parameters
    parameters_path = os.path.join('..', 'data', 'parameters.txt')
    input_details = File_details(parameters_path)
    ref_filename, cur_filename, target, prediction, type, numerical_columns, categorical_columns = input_details.get_input()

    #get report
    report_obj = Reports(cur_file=cur_filename, ref_file=ref_filename, target=target, prediction=prediction, numerical_columns=numerical_columns, categorical_columns=categorical_columns, type=type)
    report = report_obj.get_report()
    print(report)


if __name__ == "__main__":
    main()