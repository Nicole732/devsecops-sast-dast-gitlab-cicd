import requests

headers = {
    'Authorization': 'Token e71f520d6cb842d4465dab1b1d9b97e04d7a231f'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'scan_type': 'Gitleaks Scan',
    'minimum_severity': 'Low',
    'engagement': 19
}

files = {
    'file': open('gitleaks.json', 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan results imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')