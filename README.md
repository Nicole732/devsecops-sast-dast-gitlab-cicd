# DevSecOps Bootcamp: Use AWS SSM to Deploy Application to EC2 Instance

## Project Details
**Part 1**: Create new EC2 role to allow more secure access from GitLab CI using AWS SSM instead of SSH.
**Part 2**: Congigure Access with IAM roles and short-lived credentials

## Table of contents

- [Technologies used](#Technologies-Used)
- [Project Description](#Project-Description)
- [Initial Project](Initial-Project)
- [Contributors](#contributors)
- [Licensing](#licensing)

## Technologies Used
AWS IAM, Git, GitLab CI/CD, AWS EC2

## Project Description:
**Part 1**
-  Remove SSH firewall rule from AWS EC2 security group 
-  Create new IAM role for EC2 instance with ‘SSMManagedInstanceCore’ policy, assign this role to EC2 instance for SSM permission
- Remove SSH commands from GitLab CI pipeline
- Add SSM access policy to GitLab‘s IAM user permissions Update GitLab CI deploy job to:
    a. Connect to private AWS ECR repository
    b. Run Docker image pull, stop, and run commands
    c. Connect to EC2 instance with SSM, and run Docker application deployment commands
**Part 2**
- Remove static AWS credentials from configuration:
    - create a new IAM role for gitlab runner with SSM full access and AmazonEC2ContainerRegistryFullAccess
    - update appserver role to grant AmazonEC2ContainerRegistryFullAccess
    - update self-managed gitlab runner and app server instances to use the updated roles
- Configure pipeline to use role and delete static credentials


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
