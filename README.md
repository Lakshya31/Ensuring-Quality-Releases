# Quality Assurance using CI/CD

This project implements IaC (Infrastructure as Code) using Terraform to deploy azure app services.

There is an Azure Pipeline implemented in the project which deploys code into the given app service, and performs Load Testing, UI Testing & API Testing.


To run UI Tests:
- Install Python 3.7
- Install pip
- Install selenium using `pip install selenium` preferably in a virtual environment.
- Run `python <path to login.py>`


To run API Tests:
- Install npm
- Install newman using `npm install -g newman`
- Run `newman run StarterAPIs.json`

To run Load Tests:
- Install Jmeter
- Run ``

To trigger pipeline:
- Push a commit to master branch