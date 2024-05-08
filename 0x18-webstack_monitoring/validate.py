import requests

# Set your Datadog API and application keys
api_key = '730e39d6b64e9bea0fe3cf5a61123438'
app_key = 'ba5818222fe929bea9a78455b613d62d5921df16'

# Datadog API endpoint for listing hosts
url = 'https://api.datadoghq.com/api/v1/hosts'

# Set the hostname to search for
hostname_to_search = '515230-web-01'

# Set headers with authentication information
headers = {
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

# Make GET request to list hosts
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    hosts = response.json().get('hosts', [])
    
    # Check if any hosts match the expected hostname
    for host in hosts:
        if host['name'] == hostname_to_search:
            print(f"Host {hostname_to_search} found in Datadog!")
            break
    else:
        print(f"Host {hostname_to_search} not found in Datadog.")
else:
    print("Error:", response.text)
