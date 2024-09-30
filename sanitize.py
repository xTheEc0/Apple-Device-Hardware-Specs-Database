import requests
import json
import sys

def sanitize_gist(gist_url, output_file):
    response = requests.get(gist_url)
    response.raise_for_status()

    device_data = {}
    skip_lines = ["i386", "x86_64", "arm64"]  # Values to skip

    for line in response.text.splitlines():
        if any(skip_value in line for skip_value in skip_lines):
            continue  # Skip lines containing the specified values
        if line.strip(): 
            key, value = line.split(' : ', 1)
            device_data[key.strip()] = value.strip()

    with open(output_file, 'w') as f:
        json.dump(device_data, f, indent=2)

if __name__ == "__main__":
    gist_url = sys.argv[1]
    output_file = sys.argv[2]
    sanitize_gist(gist_url, output_file) 
