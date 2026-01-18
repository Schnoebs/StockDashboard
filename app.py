import configs
from functions.api_call import generate_api_call
from functions.parsing_functions import parse_json_to_csv, txt_to_json
from functions.db_connection import connect_to_db

#generate api call and save response to txt file
connect_to_db()
# #convert txt filet to json 
# json_data = txt_to_json(configs.txt_file_path)
# #parse json to csv
# parse_json_to_csv(json_data, configs.csv_file_path)