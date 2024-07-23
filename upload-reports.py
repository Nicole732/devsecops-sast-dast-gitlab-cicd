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

headers = {
    'Authorization': 'Token d2f4239f6d357913c2587c5601cb2cdbaf85e47b'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    
    'active': True,
    'verified': True,
    'scan_type': scan_type,
    'minimum_severity': 'Low',
    'engagement': 24
}

files = {
    'file': open(file_name, 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')