# DevSecOps Bootcamp: Build Gitlab CICD Pipeline to Deploy Application to AWS EC2
## Project Details
**Part 1**: Upload Images to AWS ECR using CI/CD Pipeline
**Part 2**: Deploy Application to EC2 Instance using GitLab CI/CD Pipeline

## Table of contents

- [Technologies used](#Technologies-Used)
- [Project Description](#Project-Description)
- [Initial Project](Initial-Project)
- [Contributors](#contributors)
- [Licensing](#licensing)

## Technologies Used
AWS IAM, AWS ECR, GitLab CI, AWS EC2, Docker

## Project Description:
**Part 1**
- Create access keys for user in AWS IAM
- Add AWS access keys as GitLab CI secret environment variables for use in the pipeline
- Update CI pipeline to build and push Docker images to ECR using the AWS access keys

**Part 2**
- Configure EC2 instance with Docker and ECR credentials 
- Create new deployment job in GitLab CI that automatically:
    - Connects to EC2 instance using SSH
    - Pulls the latest Docker image from ECR
    - Stops previous running container, if applicable d. Runs the latest Docker container

## Initial Project
The initial project can be found at: 
![GitHub](https://github.com/Nicole732/devsecops-sast-cicd-gitlab)
It uses OAWSP Juice Shop vulnerable application
[![Juice Shop Screenshot Slideshow](https://img.shields.io/github/release/juice-shop/juice-shop.svg)](https://github.com/juice-shop/juice-shop/releases/latest)


## Contributors

The contributors to this project are:
- [Tech World by NaNa](https://gitlab.com/twn-devsecops-bootcamp/) 

## Licensing

This program is free software: you can redistribute it and/or modify it under the terms of the [MIT license](LICENSE).
