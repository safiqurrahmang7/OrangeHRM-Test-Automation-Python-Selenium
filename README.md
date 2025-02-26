# OrangeHRM Test Automation Framework

## Overview
This repository contains a test automation framework for OrangeHRM Open Source, built using Python, Selenium, and Pytest. The framework is designed to execute UI automation tests and generate test reports.

## Features
- Selenium WebDriver integration for browser automation
- Pytest for test execution and reporting
- Configurable properties file for environment-specific settings
- Page Object Model (POM) for maintainable test scripts
- Detailed HTML and JSON test reports

## Directory Structure
```
└── safiqurrahmang7-orangehrm-test-automation-python-selenium/
    ├── README.md               # Project documentation
    ├── pytest.ini              # Pytest configuration
    ├── requirements.txt        # Dependencies list
    ├── pages/                  # Page Object Model (POM) classes
    │   ├── __init__.py
    │   ├── base_page.py
    │   └── login_page.py
    ├── reports/                # Generated test reports
    ├── tests/                  # Test scripts
    │   ├── __init__.py
    │   ├── base_test.py
    │   ├── test_login.py
    │   └── reports/            # Test-specific reports
    ├── utils/                  # Utility functions and configurations
    │   ├── __init__.py
    │   ├── config.properties   # Configuration file
    │   ├── config_reader.py    # Reads config properties
    │   └── driver_factory.py   # WebDriver management
```

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Google Chrome / Mozilla Firefox (based on test requirements)
- ChromeDriver / GeckoDriver (matching browser versions)

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/safiqurrahmang7/orangehrm-test-automation-python-selenium.git
   cd orangehrm-test-automation-python-selenium
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running Tests
Execute tests using Pytest:
```sh
pytest --html=reports/test_report.html --self-contained-html
```

Run tests with a specific marker:
```sh
pytest -m login
```

## Configuration
- Modify `utils/config.properties` to update test configurations such as base URL, browser type, and credentials.

## Reports & Logs
- Test execution results are stored in the `reports/` directory.
- HTML and JSON reports provide detailed insights into test execution.

## Contributing
Contributions are welcome! Please create a pull request with a detailed description of changes.

## License
This project is licensed under the MIT License.

