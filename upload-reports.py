import requests
import sys

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
elif file_name == 'trivy.json':
    scan_type = 'Trivy Scan'

headers = {
    'Authorization': 'Token 548afd6fab3bea9794a41b31da0e9404f733e222'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    
    'active': True,
    'verified': True,
    'scan_type': scan_type,
    'minimum_severity': 'Low',
    'engagement': 23
}

files = {
    'file': open(file_name, 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')