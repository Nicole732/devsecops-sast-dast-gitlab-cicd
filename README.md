# DevSecOps Bootcamp: Use AWS SSM to Deploy Application to EC2 Instance

## Project Details
**Part 1**: Create new EC2 role to allow more secure access from GitLab CI using AWS SSM instead of SSH.

## Table of contents

- [Technologies used](#Technologies-Used)
- [Project Description](#Project-Description)
- [Initial Project](Initial-Project)
- [Contributors](#contributors)
- [Licensing](#licensing)

## Technologies Used
AWS IAM, Git, GitLab CI/CD, Docker, AWS ECR

## Project Description:
**Part 1**
- Create AWS IAM user for GitLab CI and assign permission policy for ECR access only
- Configure the GitLab CI user with only AWS CLI access 
- Create AWS CLI access keys for the GitLab CI user 
- Update GitLab CI to use the GitLab CI user access keys instead of the admin user keys

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
