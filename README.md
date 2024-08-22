# DevSecOps Bootcamp: Configure Automated Secrets Scanning, SAST, SCA and DAST Scan in GitLab CI/CD Pipeline

## Project Details
Configure an end-to-end devsecops cicd pipeline with gitlab to implement a layered security approach:
- pre-commit hook - configured on local computer
- Secrets Scanning with Gitleaks
- SAST with Njscan
- SAST with Semgrep
- SCA with retire.js
- Import finding to DefectDojo
- Docker Image scan with Trivy
- COnfigure and Use self-managed gitlab runners to enhance security
- Connection to EC2 servers with AWS SSM - no ssh port open - 
- Secure deployement using only AWS IAM roles - no static credentials - no backdoor or exposed credentials risk
- DAST with ZAP

## Table of contents

- [Technologies used](#Technologies-Used)
- [Initial Project](Initial-Project)
- [Contributors](#contributors)
- [Licensing](#licensing)

## Technologies Used
ZAP, Gitlab CI, Docker, AWS, AWS CE2 , GITleaks, Njsscan, Semgrep, DefectDojo, Python, Javascript

## Initial Project
This project build on previous one: 
![GitHub](https://github.com/Nicole732/devsecops-sast-cicd-gitlab)
It uses OAWSP Juice Shop vulnerable application as the application code:
[![Juice Shop Screenshot Slideshow](https://img.shields.io/github/release/juice-shop/juice-shop.svg)](https://github.com/juice-shop/juice-shop/releases/latest)

## Contributors

The contributors to this project are:
- [Tech World by NaNa](https://gitlab.com/twn-devsecops-bootcamp/) 

## Licensing

This program is free software: you can redistribute it and/or modify it under the terms of the [MIT license](LICENSE).
