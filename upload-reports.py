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
elif file_name == "baseline.xml":
    scan_type = 'ZAP Scan'
elif file_name == "zap.xml":
    scan_type = 'ZAP Scan'

headers = {
    'Authorization': 'Token 4a69a997739b7f50e2a7bc8a251ed7cad02728cb'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    
    'active': True,
    'verified': True,
    'scan_type': scan_type,
    'minimum_severity': 'Low',
    'engagement': 27
}

files = {
    'file': open(file_name, 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')