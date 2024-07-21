import requests

headers = {
    'Authorization': 'Token 548afd6fab3bea9794a41b31da0e9404f733e222'
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
    print('Scan imported successfully')
else:
    print('Failed to import scan results: {response.content}')