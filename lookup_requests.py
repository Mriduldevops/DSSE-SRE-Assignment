import requests
import json
import argparse

API_URL = "https://www.travel-advisory.info/api"

def lookup_country_name(country_code):
    response = requests.get(f"{API_URL}?countrycode={country_code}")
    data = response.json()
    country_name = data['data'][country_code]['name']
    return country_name

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def main():
    parser = argparse.ArgumentParser(description="Country Code Lookup CLI")
    parser.add_argument("--countryCode", nargs='+', help="Country code(s) to look up", required=True)
    parser.add_argument("--saveToFile", help="Save API data to a file")
    parser.add_argument("--loadFromFile", help="Load API data from a file")

    args = parser.parse_args()

    if args.loadFromFile:
        api_data = load_from_file(args.loadFromFile)
    else:
        api_data = requests.get(API_URL).json()
        if args.saveToFile:
            save_to_file(api_data, args.saveToFile)

    for country_code in args.countryCode:
        country_name = lookup_country_name(country_code)
        print(f"{country_code}: {country_name}")

if __name__ == "__main__":
    main()
