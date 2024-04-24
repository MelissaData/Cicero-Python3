import json
from threading import local
import requests
import argparse
import urllib.parse

def main():
  base_service_url = "https://app.cicerodata.com/"
  service_endpoint = "v3.1/official"

  # Create an ArgumentParser object
  parser = argparse.ArgumentParser(description='Cicero command line arguments parser')

  # Define the command line arguments
  parser.add_argument('--license', '-l', type=str, help='License key')
  parser.add_argument('--lat', type=str, help='Latitude')
  parser.add_argument('--long', type=str, help='Longitude')
  parser.add_argument('--location', type=str, help='Search Location')
  parser.add_argument('--max', type=str, help='Max')

  # Parse the command line arguments
  args = parser.parse_args()

  # Access the values of the command line arguments
  license = args.license
  latitude = args.lat
  longitude = args.long
  location = args.location
  max = args.max

  call_api(base_service_url, service_endpoint, license, latitude, longitude, location, max)

def get_contents(base_service_url, request_query):
    url = urllib.parse.urljoin(base_service_url, request_query)
    response = requests.get(url)
    obj = json.loads(response.text)
    pretty_response = json.dumps(obj, indent=4)

    print("\n============================================= OUTPUT =============================================\n")

    print("API Call: ")

    for i in range(0, len(url), 70):
        if i + 70 < len(url):
            print(url[i:i+70])
        else:
            print(url[i:len(url)])
    print("\nAPI Response:")
    print(pretty_response)

def call_api(base_service_url, service_endpoint, license, latitude, longitude, location, max):
    print("\n=============================== WELCOME TO MELISSA CICERO CLOUD API ==============================\n")

    should_continue_running = True
    while should_continue_running:
        input_latitude = ""
        input_longitude = ""
        input_location = ""
        input_max = ""
        if not latitude and not longitude and not location:
            print("\nFill in each value to see results")
            input_latitude = input("Latitude: ")
            input_longitude = input("Longitude: ")
            input_location = input("Search Location: ")
            input_max = input("Max Return: ")
        else:
            input_latitude = latitude
            input_longitude = longitude
            input_location = location
            input_max = max

        while not input_latitude or not input_longitude or not input_location or not input_max:
            print("\nFill in each value to see results")
            if not input_latitude:
                input_latitude = input("\nLatitude: ")
            if not input_longitude:
                input_longitude = input("\nLongitude: ")
            if not input_location:
                input_location = input("\nSearch Location: ")
            if not input_max:
                input_max = input("\nMax Return: ")

        inputs = {
            "format": "json",
            "max": input_max,
            "lat": input_latitude,
            "lon": input_longitude,
            "search_loc": input_location
        }

        print("\n============================================= INPUTS =============================================\n")
        print(f"\t   Base Service Url: {base_service_url}")
        print(f"\t  Service End Point: {service_endpoint}")
        print(f"\t           Latitude: {input_latitude}")
        print(f"\t          Longitude: {input_longitude}")
        print(f"\t    Search Location: {input_location}")
        print(f"\t                Max: {input_max}")

       # Create Service Call
        # Set the License String in the Request
        rest_request = f"&key={urllib.parse.quote_plus(license)}"

        # Set the Input Parameters
        for k, v in inputs.items():
            rest_request += f"&{k}={urllib.parse.quote_plus(v)}"

        # Build the final REST String Query
        rest_request = service_endpoint + f"?{rest_request}"

        # Submit to the Web Service.
        success = False
        retry_counter = 0

        while not success and retry_counter < 5:
            try: #retry just in case of network failure
                get_contents(base_service_url, rest_request)
                print()
                success = True
            except Exception as ex:
                retry_counter += 1
                print(ex)
                return

        is_valid = False;

        if (latitude is not None) and (longitude is not None) and (location is not None) and (max is not None):
            inputline = latitude + longitude + location
        else:
            inputline = None

        if inputline is not None and inputline != "":
            is_valid = True
            should_continue_running = False

        while not is_valid:
            test_another_response = input("\nTest another record? (Y/N)")
            if test_another_response != '':
                test_another_response = test_another_response.lower()
                if test_another_response == 'y':
                    is_valid = True
                elif test_another_response == 'n':
                    is_valid = True
                    should_continue_running = False
                else:
                    print("Invalid Response, please respond 'Y' or 'N'")

    print("\n============================= THANK YOU FOR USING MELISSA CLOUD API ==============================\n")

main()
