# 🛒 eCommerce Website Automation using Selenium & Pytest

This project is a **complete end-to-end automation framework** for the demo eCommerce site **automationexercise.com**, built using **Python**, **Selenium WebDriver**, and **Pytest**.  
It follows the **Page Object Model (POM)** to ensure scalability, readability, and maintainability — matching real-time industry automation standards.

---

## 🚀 Features

### 🌐 Functional Test Coverage
- Navigate product catalog
- Open product details
- Add items to cart
- Validate cart contents
- Remove items from cart
- Verify total price & product info

### 🧰 Framework Features
- Selenium WebDriver automation
- Pytest test runner
- Page Object Model (POM)
- Utility modules for reusable logic
- Configurable driver setup
- HTML test report support (pytest-html)
- Screenshot capture on failure

---

## 🧱 Tech Stack

- **Python 3.x**
- **Selenium WebDriver**
- **Pytest**
- **ChromeDriver**
- **HTML Reporting**
- **Page Object Model (POM)** structure

---

## 📁 Project Structure

ecommerce_automation/
│
├── pages/
│ ├── base_page.py # Common reusable page methods
│ ├── home_page.py # Home page locators & actions
│ └── product_page.py # Product and cart operations
│
├── tests/
│ └── test_add_to_cart.py # Main test validating add-to-cart flow
│
├── utils/
│ ├── driver_setup.py # Browser setup/teardown
│ └── actions.py # Optional helper actions
│
├── report.html # Auto-generated HTML test report
├── conftest.py # Pytest fixtures (driver, setup)
├── requirements.txt # Project dependencies
└── README.md # Documentation

yaml
Copy code

---

## ▶️ How to Run the Tests

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/rohithtommandru/ecommerce-automation.git
cd ecommerce-automation
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Execute the test suite
To run all tests:

bash
Copy code
pytest -v
To run a specific test:

bash
Copy code
pytest tests/test_add_to_cart.py
To generate HTML report:

bash
Copy code
pytest --html=report.html
🏗️ Design Pattern — Page Object Model (POM)
This project follows POM to:

Separate test logic from UI interactions

Improve scalability

Reduce code duplication

Make automation tests cleaner and easier to maintain

Each page has its own class with:

Locators

Page actions (methods)

Assertions

📌 Future Enhancements
Add parallel execution using pytest-xdist

Add Allure reporting

Integrate with GitHub Actions CI pipeline

Add data-driven tests (CSV/Excel)

Expand test coverage

👨‍💻 Author
Rohith Babu
QA Automation Engineer | Selenium | Python | Pytest
