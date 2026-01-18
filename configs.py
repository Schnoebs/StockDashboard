import requests
from datetime import datetime

# variables
date = datetime.now()

# generate an api call 
API_KEY = "TIV2UpbrPdPKybwA5txxkGTHEiqP1xV2"


# paths
txt_file_path = "api_response.txt"
csv_file_path = "//csv"+f"data-{str(date)}"+".csv"
