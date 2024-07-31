# DevSecOps Bootcamp: Scan Docker Images using Trivy with GitLab CI/CD Pipeline

## Project Details
**Part 1**: Update GitLab CI/CD pipeline to perform Docker image scanning using Trivy.
**Part 2**: Update GitLab CI/CD pipeline to automate upload of Trivy image scan results to DefectDojo.


## Table of contents

- [Technologies used](#Technologies-Used)
- [Project Description](#Project-Description)
- [Initial Project](Initial-Project)
- [Contributors](#contributors)
- [Licensing](#licensing)

## Technologies Used
Trivy, Git, GitLab CI, Docker, AWS ECR, Python, DefectDojo

## Project Description:
**Part 1**
- Create new job in GitLab CI/CD pipeline that :
    - Pulls the Docker image from private AWS ECR b. 
    - Runs Trivy image scan on the image
    - Fails Trivy job only if high or critical level security findings are detected

**Part 2**
- Update Trivy job to export image security findings report as pipeline artifact
- Update Python script to automatically upload Trivy security findings to DefectDojo
- Update Upload Reports job to execute Python upload script for Trivy scan reports

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
