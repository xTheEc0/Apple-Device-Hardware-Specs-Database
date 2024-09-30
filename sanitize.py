import requests
import json
import sys

def sanitize_gist(gist_url, output_file):
    response = requests.get(gist_url)
    response.raise_for_status()

    device_data = {}
    skip_lines = ["i386", "x86_64", "arm64"] 

    for line in response.text.splitlines():
        if any(skip_value in line for skip_value in skip_lines):
            continue
        if line.strip() and not line.startswith("Watch"):  # Exclude "Watch" lines
            key, value = line.split(' : ', 1)
            device_data[key.strip()] = value.strip()

    # Manually add AppleTV values
    device_data.update({
        "AppleTV1,1": "Apple TV 1st Gen",
        "AppleTV2,1": "Apple TV 2nd Gen",
        "AppleTV3,1": "Apple TV 3rd Gen (Early 2012)",
        "AppleTV3,2": "Apple TV 3rd Gen (Late 2013)",
        "AppleTV5,3": "Apple TV (HD) 4th Gen",
        "AppleTV6,2": "Apple TV 4K 1st Gen",
        "AppleTV11,1": "Apple TV 4K 2nd Gen",
        "AppleTV14,1": "Apple TV 4K 3rd Gen"
    })

    with open(output_file, 'w') as f:
        json.dump(device_data, f, indent=2)

if __name__ == "__main__":
    gist_url = sys.argv[1]
    output_file = sys.argv[2]
    sanitize_gist(gist_url, output_file)
