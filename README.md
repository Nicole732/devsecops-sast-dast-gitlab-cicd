# DevSecOps Bootcamp: Application Vulnerability Scanning
## Project Details
**Part 1**: Setup Secrets Scanning in GitLab CI and Pre-Commit Script using GitLeaks
**Part 2**: Setup Static Application Secret Testing (SAST) in GitLab CI pipeline using NJSScan and Semgrep.
**Part 3**: Upload Security Scan Results Automatically to DefectDojo
**Part 4**: Remediate Weak Cryptography and SQL Injection Vulnerabilities in Application based on Security Findings
**Part 5**: Setup SCA Scanning using RetireJS and Upload Findings to DefectDojo

## Table of contents

- [Technologies used](#Technologies-Used)
- [Project Description](#Project-Description)
- [OWASP Juice Shop](#OWASP-Juice-Shop)
- [Contributors](#contributors)
- [Licensing](#licensing)

## Technologies Used
GitLab CI, JavaScript, Git, NJSScan, Semgrep, Gitleaks, DefectDojo, Python

## Project Description:
**Part 1**
- Configure GitLeaks job in GitLab CI to check commits for secrets
- Create a Git pre-commit hook script that runs GitLeaks using Docker, and performs GitLeaks scan before code is committed

**Part 2**
- Configure NJSScan in GitLab CI pipeline to run SAST scan against repository code
- Configure Semgrep in GitLab CI pipeline to run additional SAST scan against respository code

**Part 3**
- Create Python script that connects to DefectDojo via API key
- Create Python script to upload GitLeaks, Semgrep, and NJSScan files from GitLab CI security scanning jobs to DefectDojo
- Add a new job in GitLab CI pipeline to run the Python script to upload findings to DefectDojo as part of the pipeline execution

**Part 4**
- Update application code to remediate weak hash function, based on NJSScan security finding in DefectDojo
- Update application code to remediate SQL injection vulnerability, based on Semgrep security finding in DefectDojo

**Part 5**
- Create new GitLab CI pipeline job for automated SCA scanning using RetireJS
- Configure the job to save the SCA scan reports as an artifact
- Upload the RetireJS scan report to DefectDojo using Python automation script

## OWASP Juice Shop

![Juice Shop Logo](https://raw.githubusercontent.com/juice-shop/juice-shop/master/frontend/src/assets/public/images/JuiceShop_Logo_100px.png) OWASP Juice Shop

[![OWASP Flagship](https://img.shields.io/badge/owasp-flagship%20project-48A646.svg)](https://owasp.org/projects/#sec-flagships)
[![GitHub release](https://img.shields.io/github/release/juice-shop/juice-shop.svg)](https://github.com/juice-shop/juice-shop/releases/latest)
[![Twitter Follow](https://img.shields.io/twitter/follow/owasp_juiceshop.svg?style=social&label=Follow)](https://twitter.com/owasp_juiceshop)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/owasp_juiceshop?style=social)](https://reddit.com/r/owasp_juiceshop)

![CI/CD Pipeline](https://github.com/juice-shop/juice-shop/workflows/CI/CD%20Pipeline/badge.svg?branch=master)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6206c8f3972bcc97a033/test_coverage)](https://codeclimate.com/github/juice-shop/juice-shop/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/6206c8f3972bcc97a033/maintainability)](https://codeclimate.com/github/juice-shop/juice-shop/maintainability)
[![Code Climate technical debt](https://img.shields.io/codeclimate/tech-debt/juice-shop/juice-shop)](https://codeclimate.com/github/juice-shop/juice-shop/trends/technical_debt)
[![Cypress tests](https://img.shields.io/endpoint?url=https://dashboard.cypress.io/badge/simple/3hrkhu/master&style=flat&logo=cypress)](https://dashboard.cypress.io/projects/3hrkhu/runs)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/223/badge)](https://bestpractices.coreinfrastructure.org/projects/223)
![GitHub stars](https://img.shields.io/github/stars/juice-shop/juice-shop.svg?label=GitHub%20%E2%98%85&style=flat)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)

> [The most trustworthy online shop out there.](https://twitter.com/dschadow/status/706781693504589824)
> ([@dschadow](https://github.com/dschadow)) —
> [The best juice shop on the whole internet!](https://twitter.com/shehackspurple/status/907335357775085568)
> ([@shehackspurple](https://twitter.com/shehackspurple)) —
> [Actually the most bug-free vulnerable application in existence!](https://youtu.be/TXAztSpYpvE?t=26m35s)
> ([@vanderaj](https://twitter.com/vanderaj)) —
> [First you 😂😂then you 😢](https://twitter.com/kramse/status/1073168529405472768)
> ([@kramse](https://twitter.com/kramse)) —
> [But this doesn't have anything to do with juice.](https://twitter.com/coderPatros/status/1199268774626488320)
> ([@coderPatros' wife](https://twitter.com/coderPatros))

We used the OWASP Juice Shop project as a start point. 
OWASP Juice Shop is probably the most modern and sophisticated insecure web application! It can be used in security
trainings, awareness demos, CTFs and as a guinea pig for security tools! Juice Shop encompasses vulnerabilities from the
entire
[OWASP Top Ten](https://owasp.org/www-project-top-ten) along with many other security flaws found in real-world
applications!

![Juice Shop Screenshot Slideshow](screenshots/slideshow.gif)

For a detailed introduction, full list of features and architecture overview please visit the official project page:
<https://owasp-juice.shop>

## Contributors

The contributors to this project are:

- [Tech World by NaNa](https://gitlab.com/twn-devsecops-bootcamp/) 

## Licensing

This program is free software: you can redistribute it and/or modify it under the terms of the [MIT license](LICENSE).
