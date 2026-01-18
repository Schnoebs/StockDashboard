import configs
import csv

#this function will convert a txt file to a json file
def txt_to_json(txt_file_path):
    import json
    with open(txt_file_path, 'r') as file:
        data = file.read()
    json_data = json.loads(data)
    return json_data

#generate a function that will take a json response and parse it into a csv
def parse_json_to_csv(json_data, csv_file_path):
    # Open the CSV file for writing
    with open(configs.csv_file_path, mode='w', newline='') as csv_file:
        if not json_data:
            print("No data to write to CSV.")
            return

        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write the header row (keys of the first dictionary)
        header = json_data[0].keys()
        csv_writer.writerow(header)

        # Write the data rows
        for entry in json_data:
            csv_writer.writerow(entry.values())

    print(f"Data successfully written to {configs.csv_file_path}")
    