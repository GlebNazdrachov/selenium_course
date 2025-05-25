# Final Project: Selenium Auto Tests (Stepik course)

This project is an automated testing suite for a demo online store using **Selenium** and **PyTest**.  
The tests follow the **Page Object Model** and are split between guest and authorized user scenarios.

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
**python -m pytest -v --tb=line --language=en -m need_review**

This will run 13 tests.
3 tests: test_user_can_add_product_to_basket, test_guest_cant_see_product_in_basket_opened_from_product_page, test_guest_can_go_to_login_page_from_product_page
10 test: test_guest_can_add_product_to_basket for all promo ofers from promo=offer0 to promo=offer10, except promo=offer7-xfail
