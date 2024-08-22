# DevSecOps Bootcamp: Configure Automated DAST Scan in GitLab CI/CD Pipeline

## Project Details
**Part 1**: 
Create ZAP job in GitLab CI/CD pipeline to run automated Dynamic Application Security Testing (DAST) scans.

## Table of contents

- [Technologies used](#Technologies-Used)
- [Project Description](#Project-Description)
- [Initial Project](Initial-Project)
- [Contributors](#contributors)
- [Licensing](#licensing)

## Technologies Used
ZAP, Gitlab CI, Docker, AWS 

## Project Description:
**Part 1**
- Configure GitLab CI pipeline to deploy to test and prod environments
- Create a DAST job in GitLab CI to:
    a. Run automated ZAP scans against Docker application deployed on EC2 instance
    b. Fail the ZAP job for security findings above the warning severity level
    c. Export the ZAP scan results as a pipeline artifact


## Initial Project
This project build on previous one: 
![GitHub](https://github.com/Nicole732/devsecops-sast-cicd-gitlab)
It uses OAWSP Juice Shop vulnerable application as the application code:
[![Juice Shop Screenshot Slideshow](https://img.shields.io/github/release/juice-shop/juice-shop.svg)](https://github.com/juice-shop/juice-shop/releases/latest)

We use ZAP - Zep Attack Proxy open source Dynamic Application Security Testing Open Source tool. For more configuration options for ZAP, visit [!ZapProxy Blog](https://www.zaproxy.org/docs/docker/baseline-scan/)

## Contributors

The contributors to this project are:
- [Tech World by NaNa](https://gitlab.com/twn-devsecops-bootcamp/) 

## Licensing

This program is free software: you can redistribute it and/or modify it under the terms of the [MIT license](LICENSE).
