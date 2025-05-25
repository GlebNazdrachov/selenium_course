# Final Project: Selenium Auto Tests (Stepik course)

This project is an automated testing suite for a demo online store using **Selenium** and **PyTest**.  
The tests follow the **Page Object Model** and are split between guest and authorized user scenarios.

Project structure
selenium_course/
├── conftest.py
├── requirements.txt
├── test_main_page.py
├── test_product_page.py
└── pages/
├── init.py
├── base_page.py
├── main_page.py
├── login_page.py
├── product_page.py
├── basket_page.py
└── locators.py

## ✅ Setup instructions

1. **Clone the repository** and navigate to the project folder:
   
git clone https://github.com/GlebNazdrachov/selenium_course
cd selenium_course

2. (Optional) Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Mac/Linux

3. Install dependencies
pip install -r requirements.txt

How to run tests
To run all tests marked for review:
python -m pytest -v --tb=line --language=en -m need_review

