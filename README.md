# OrangeHRM Test Automation Framework

This project showcases an automated testing framework for the OrangeHRM demo site, designed to validate its critical functionalities efficiently and effectively. The framework is built using Python and Selenium, following industry-standard practices to ensure scalability, maintainability, and reliability.

## Project Objective
To automate key workflows of the OrangeHRM demo site to:
- Reduce manual testing effort.
- Ensure consistency and reliability of key functionalities.
- Enhance testing efficiency with detailed reporting.

## Features Tested
1. **Login Module**
   - Valid login with correct credentials.
   - Error validation for invalid credentials.
   - Field validation for empty inputs.

2. **PIM Module**
   - Adding a new employee.
   - Editing employee details.
   - Deleting an employee.

3. **Admin Module**
   - Adding and managing user roles.
   - Validating job categories.

4. **Logout Functionality**
   - Validating successful logout.
   - Ensuring session expiry after logout.

## Tools and Technologies
- **Programming Language:** Python
- **Automation Tool:** Selenium WebDriver
- **Testing Framework:** Pytest
- **Reporting Tool:** Allure Reports (optional)
- **Version Control:** Git

## Framework Design
The framework follows the **Page Object Model (POM)** design pattern to:
- Separate test logic from UI element locators.
- Enhance code reusability and readability.

### Project Structure
```
project/
├── tests/
│   ├── test_login.py
│   ├── test_pim.py
│   ├── test_admin.py
│   └── test_logout.py
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── pim_page.py
├── utils/
│   ├── base_test.py
│   ├── logger.py
│   └── config.py
├── requirements.txt
└── README.md
```

### Key Components
1. **Pages**
   - Contains classes and methods for each page to encapsulate locators and actions.
2. **Tests**
   - Includes test scripts to validate workflows.
3. **Utils**
   - Utility files for shared configurations and logging.

## Setup and Installation

### Prerequisites
- Python 3.8+
- Chrome Browser
- ChromeDriver (compatible with your Chrome version)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/orangehrm-test-automation.git
   cd orangehrm-test-automation
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run tests:
   ```bash
   pytest
   ```

5. Generate Allure Reports (optional):
   ```bash
   pytest --alluredir=reports/
   allure serve reports/
   ```

## Sample Test Case
**Test:** Login with valid credentials

```python
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

class TestLogin:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login_button()
        assert "dashboard" in self.driver.current_url, "Failed to login with valid credentials."
```

## Challenges Addressed
- **Dynamic Elements:** Handled dynamic locators using Selenium's WebDriverWait.
- **Synchronization Issues:** Implemented implicit and explicit waits for stable test execution.
- **Scalability:** Designed a modular framework to accommodate future enhancements easily.

## Key Achievements
- Automated end-to-end testing for core OrangeHRM functionalities.
- Reduced manual testing effort by 60%.
- Ensured comprehensive test coverage with data-driven testing.

## Future Enhancements
- Add cross-browser testing.
- Integrate CI/CD pipelines for automated test execution.
- Enhance reporting with screenshots for failed test cases.

## Author
**Safiqur Rahman**

Feel free to reach out for collaboration or feedback!
