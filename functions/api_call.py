import configs
import requests

def generate_api_call():
    api_url = "https://api.massive.com/v3/reference/dividends?apiKey=" + configs.API_KEY

    try:
        # Make the GET request
        response = requests.get(api_url)

        # Check if the request was successful (status code 200-299)
        if response.ok:
            # Parse the JSON response into a Python dictionary
            data = response.json()
            print("API Call Successful!")
            #write data to txt file and store it in an api_response.txt file
            with open("api_response.txt", "w") as file:
                file.write(str(data))
            return data
        else:
            print(f"API Call Failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle any network-related errors (e.g., connection issues)
        print(f"An error occurred: {e}")