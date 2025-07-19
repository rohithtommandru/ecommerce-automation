# 🛒 eCommerce Website Automation using Selenium and Pytest

This project is an end-to-end automation suite for the [automationexercise.com](https://automationexercise.com) eCommerce demo site.

## 🚀 Features

- 🔍 Navigate product listings
- 🛒 Add products to cart
- ✅ Verify cart contents
- ⚙️ Uses Page Object Model (POM)
- 🧪 Test framework: Pytest
- 🌐 Browser automation: Selenium

## 🧰 Tech Stack

- Python 3.x
- Selenium
- Pytest
- Chrome WebDriver

## 📁 Project Structure

<pre>
ecommerce_automation/
├── pages/
│   ├── base_page.py         # Base class for all page objects
│   ├── home_page.py         # Page object for the home page
│   └── product_page.py      # Page object for product/cart interactions
├── tests/
│   └── test_add_to_cart.py  # Main Pytest script for testing add-to-cart flow
├── utils/
│   └── driver_setup.py      # WebDriver initialization and teardown
├── requirements.txt         # Python dependencies
└── README.md                # Project overview and usage guide
</pre>



▶️ How to Run

# Clone the repo
git clone https://github.com/rohithtommandru/ecommerce-automation.git
cd ecommerce-automation

# Install dependencies
pip install -r requirements.txt

# Run the test
pytest tests/test_add_to_cart.py


🧠 Author
Rohith Tommandru
(https://github.com/rohithtommandru)



