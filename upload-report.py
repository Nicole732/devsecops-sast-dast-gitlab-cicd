import requests
import sys

# URL for the API endpoint
url = 'https://demo.defectdojo.org/api/v2/import-scan/'

# Report file name that will be uploaded
file_name = sys.argv[1]
scan_type = ''

if file_name == 'gitleaks.json':
    scan_type = 'Gitleaks Scan'
elif file_name == 'njsscan.sarif':
    scan_type = 'SARIF'
elif file_name == 'semgrep.json':
    scan_type = 'Semgrep JSON Report'
elif file_name == 'retire.json':
    scan_type = 'Retire.js Scan'

# Prepare the headers for the HTTP request
headers = {
    'Authorization': 'Token aff06e362affd9442cbf990fe41ef93c5ae366fa',
}

# Prepare the data for the HTTP request
# create engagement. Id is in the URL: https://demo.defectdojo.org/engagement/15
data = {
    'engagement': 15,  # the engagement ID to which the test belongs
    'scan_type': scan_type,  # the type of the scan
    'minimum_severity': 'Low',  # the minimum severity of findings to import
    'active': True,  # marks imported findings as active
    'verified': True,  # marks imported findings as verified
}

# Prepare the files for the HTTP request
files = {
    'file': open(file_name, 'rb'),  # the scan file to import
}

# Make the HTTP request
response = requests.post(url, headers=headers, data=data, files=files)

# Check the response
if response.status_code == 201:
    print('Scan results imported successfully.')
else:
    print(f'Failed to import scan results: {response.content}')
