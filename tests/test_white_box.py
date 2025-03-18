"""
White-box unit testing examples.
"""
import unittest
from src.white_box import (
    is_even,
    divide,
    get_grade,
    is_triangle,
    check_number_status,
    validate_password,
    calculate_total_discount,
    calculate_order_total,
    calculate_items_shipping_cost,
    validate_login,
    verify_age,
    categorize_product,
    validate_email,
    celsius_to_fahrenheit,
    validate_credit_card,
    validate_date,
    check_flight_eligibility,
    validate_url,
    calculate_quantity_discount,
    check_file_size,
    check_loan_eligibility,
    calculate_shipping_cost,
    grade_quiz,
    authenticate_user,
    get_weather_advisory,
    VendingMachine,
    TrafficLight,
    UserAuthentication,
    DocumentEditingSystem,
    ElevatorSystem,
    BankingSystem,
    Product,
    ShoppingCart,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(2))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(11))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)
        self.assertEqual(divide(5, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")
        self.assertEqual(get_grade(100), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")
        self.assertEqual(get_grade(89), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")
        self.assertEqual(get_grade(79), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")
        self.assertEqual(get_grade(0), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")
        self.assertEqual(is_triangle(5, 12, 13), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")
        self.assertEqual(is_triangle(1, 1, 2), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")
        self.assertEqual(is_triangle(1, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")
        self.assertEqual(is_triangle(5, 2, 2), "No, it's not a triangle.")

    def test_check_number_status_positive(self):
        """
        Checks if a number is positive.
        """
        self.assertEqual(check_number_status(5), "Positive")
        self.assertEqual(check_number_status(100), "Positive")

    def test_check_number_status_negative(self):
        """
        Checks if a number is negative.
        """
        self.assertEqual(check_number_status(-5), "Negative")
        self.assertEqual(check_number_status(-100), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks if a number is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

    def test_validate_password_valid(self):
        """
        Checks if a password is valid.
        """
        self.assertTrue(validate_password("Password1!"))
        self.assertTrue(validate_password("Secure123#"))

    def test_validate_password_invalid(self):
        """
        Checks if a password is invalid.
        """
        self.assertFalse(validate_password("pass"))
        self.assertFalse(validate_password("password"))

    def test_calculate_total_discount_no_discount(self):
        """
        Checks if no discount is applied.
        """
        self.assertEqual(calculate_total_discount(50), 0)

    def test_calculate_total_discount_10_percent(self):
        """
        Checks if a 10% discount is applied.
        """
        self.assertEqual(calculate_total_discount(200), 20)

    def test_calculate_total_discount_20_percent(self):
        """
        Checks if a 20% discount is applied.
        """
        self.assertEqual(calculate_total_discount(600), 120)

    def test_calculate_order_total_no_discount(self):
        """
        Checks the total price with no discount.
        """
        items = [{"quantity": 3, "price": 10}]
        self.assertEqual(calculate_order_total(items), 30)

    def test_calculate_order_total_5_percent_discount(self):
        """
        Checks the total price with a 5% discount.
        """
        items = [{"quantity": 7, "price": 20}]
        self.assertEqual(calculate_order_total(items), 133)

    def test_calculate_order_total_10_percent_discount(self):
        """
        Checks the total price with a 10% discount.
        """
        items = [{"quantity": 15, "price": 10}]
        self.assertEqual(calculate_order_total(items), 135)

    def test_calculate_items_shipping_cost_standard(self):
        """
        Checks the shipping cost for standard delivery.
        """
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_express(self):
        """
        Checks the shipping cost for express delivery.
        """
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_validate_login_success(self):
        """
        Checks if login is successful.
        """
        self.assertEqual(validate_login("user123", "password123"), "Login Successful")

    def test_validate_login_failed(self):
        """
        Checks if login fails.
        """
        self.assertEqual(validate_login("usr", "pass"), "Login Failed")

    def test_verify_age_eligible(self):
        """
        Checks if a person is eligible.
        """
        self.assertEqual(verify_age(25), "Eligible")
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_not_eligible(self):
        """
        Checks if a person is not eligible.
        """
        self.assertEqual(verify_age(17), "Not Eligible")
        self.assertEqual(verify_age(66), "Not Eligible")

    def test_categorize_product_category_a(self):
        """
        Checks if a product is in Category A.
        """
        self.assertEqual(categorize_product(25), "Category A")
        self.assertEqual(categorize_product(50), "Category A")

    def test_categorize_product_category_b(self):
        """
        Checks if a product is in Category B.
        """
        self.assertEqual(categorize_product(75), "Category B")
        self.assertEqual(categorize_product(100), "Category B")

    def test_categorize_product_category_c(self):
        """
        Checks if a product is in Category C.
        """
        self.assertEqual(categorize_product(150), "Category C")
        self.assertEqual(categorize_product(200), "Category C")

    def test_categorize_product_category_d(self):
        """
        Checks if a product is in Category D.
        """
        self.assertEqual(categorize_product(250), "Category D")
        self.assertEqual(categorize_product(5), "Category D")


    def test_validate_email_valid(self):
        """
        Checks if an email is valid.
        """
        self.assertEqual(validate_email("test@example.com"), "Valid Email")
        self.assertEqual(validate_email("user@domain.com"), "Valid Email")

    def test_validate_email_invalid(self):
        """
        Checks if an email is invalid.
        """
        self.assertEqual(validate_email("test"), "Invalid Email")
        self.assertEqual(validate_email("user@domain"), "Invalid Email")

    def test_celsius_to_fahrenheit_valid(self):
        """
        Checks the conversion from Celsius to Fahrenheit.
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_invalid(self):
        """
        Checks if the temperature is invalid.
        """
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    def test_validate_credit_card_valid(self):
        """
        Checks if a credit card number is valid.
        """
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_validate_credit_card_invalid(self):
        """
        Checks if a credit card number is invalid.
        """
        self.assertEqual(validate_credit_card("123"), "Invalid Card")
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_validate_date_valid(self):
        """
        Checks if a date is valid.
        """
        self.assertEqual(validate_date(2023, 10, 15), "Valid Date")
        self.assertEqual(validate_date(2000, 1, 1), "Valid Date")

    def test_validate_date_invalid(self):
        """
        Checks if a date is invalid.
        """
        self.assertEqual(validate_date(2023, 13, 15), "Invalid Date")
        self.assertEqual(validate_date(2023, 10, 32), "Invalid Date")

    def test_check_flight_eligibility_eligible(self):
        """
        Checks if a passenger is eligible to book a flight.
        """
        self.assertEqual(check_flight_eligibility(25, False), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")

    def test_check_flight_eligibility_not_eligible(self):
        """
        Checks if a passenger is not eligible to book a flight.
        """
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")

    def test_validate_url_valid(self):
        """
        Checks if a URL is valid.
        """
        self.assertEqual(validate_url("http://example.com"), "Valid URL")
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_validate_url_invalid(self):
        """
        Checks if a URL is invalid.
        """
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")
        self.assertEqual(validate_url("example.com"), "Invalid URL")

    def test_calculate_quantity_discount_no_discount(self):
        """
        Checks if no discount is applied.
        """
        self.assertEqual(calculate_quantity_discount(3), "No Discount")

    def test_calculate_quantity_discount_5_percent(self):
        """
        Checks if a 5% discount is applied.
        """
        self.assertEqual(calculate_quantity_discount(7), "5% Discount")

    def test_calculate_quantity_discount_10_percent(self):
        """
        Checks if a 10% discount is applied.
        """
        self.assertEqual(calculate_quantity_discount(15), "10% Discount")

    def test_check_file_size_valid(self):
        """
        Checks if a file size is valid.
        """
        self.assertEqual(check_file_size(500000), "Valid File Size")
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_check_file_size_invalid(self):
        """
        Checks if a file size is invalid.
        """
        self.assertEqual(check_file_size(2000000), "Invalid File Size")
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_check_loan_eligibility_not_eligible(self):
        """
        Checks if a person is not eligible for a loan.
        """
        self.assertEqual(check_loan_eligibility(25000, 750), "Not Eligible")

    def test_check_loan_eligibility_standard_loan(self):
        """
        Checks if a person is eligible for a standard loan.
        """
        self.assertEqual(check_loan_eligibility(40000, 750), "Standard Loan")
        self.assertEqual(check_loan_eligibility(60000, 700), "Standard Loan")

    def test_check_loan_eligibility_premium_loan(self):
        """
        Checks if a person is eligible for a premium loan.
        """
        self.assertEqual(check_loan_eligibility(70000, 800), "Premium Loan")

    def test_calculate_shipping_cost_small_package(self):
        """
        Checks the shipping cost for a small package.
        """
        self.assertEqual(calculate_shipping_cost(0.5, 5, 5, 5), 5)

    def test_calculate_shipping_cost_medium_package(self):
        """
        Checks the shipping cost for a medium package.
        """
        self.assertEqual(calculate_shipping_cost(3, 15, 15, 15), 10)

    def test_calculate_shipping_cost_large_package(self):
        """
        Checks the shipping cost for a large package.
        """
        self.assertEqual(calculate_shipping_cost(10, 35, 35, 35), 20)

    def test_grade_quiz_pass(self):
        """
        Checks if a quiz grade is a pass.
        """
        self.assertEqual(grade_quiz(8, 1), "Pass")

    def test_grade_quiz_conditional_pass(self):
        """
        Checks if a quiz grade is a conditional pass.
        """
        self.assertEqual(grade_quiz(6, 3), "Conditional Pass")

    def test_grade_quiz_fail(self):
        """
        Checks if a quiz grade is a fail.
        """
        self.assertEqual(grade_quiz(4, 4), "Fail")

    def test_authenticate_user_admin(self):
        """
        Checks if the user is an admin.
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_regular_user(self):
        """
        Checks if the user is a regular user.
        """
        self.assertEqual(authenticate_user("user123", "password123"), "User")

    def test_authenticate_user_invalid(self):
        """
        Checks if the user is invalid.
        """
        self.assertEqual(authenticate_user("user", "pass"), "Invalid")

    def test_get_weather_advisory_high_temp_humidity(self):
        """
        Checks the weather advisory for high temperature and humidity.
        """
        self.assertEqual(
            get_weather_advisory(35, 75), "High Temperature and Humidity. Stay Hydrated."
        )

    def test_get_weather_advisory_low_temp(self):
        """
        Checks the weather advisory for low temperature.
        """
        self.assertEqual(get_weather_advisory(-5, 50), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_no_advisory(self):
        """
        Checks if no specific advisory is given.
        """
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks if the vending machine accepts coins successfully.
        """
        vm = VendingMachine()
        self.assertEqual(vm.insert_coin(), "Coin Inserted. Select your drink.")
        self.assertEqual(vm.state, "Dispensing")

    def test_vending_machine_insert_coin_error(self):
        """
        Checks if the vending machine fails to accept coins when not ready.
        """
        vm = VendingMachine()
        vm.state = "Dispensing"
        self.assertEqual(vm.insert_coin(), "Invalid operation in current state.")
        self.assertEqual(vm.state, "Dispensing")

    def test_vending_machine_select_drink_success(self):
        """
        Checks if the vending machine dispenses a drink successfully.
        """
        vm = VendingMachine()
        vm.insert_coin()
        self.assertEqual(vm.select_drink(), "Drink Dispensed. Thank you!")
        self.assertEqual(vm.state, "Ready")

    def test_vending_machine_select_drink_error(self):
        """
        Checks if the vending machine fails to dispense a drink when no coin is inserted.
        """
        vm = VendingMachine()
        self.assertEqual(vm.select_drink(), "Invalid operation in current state.")
        self.assertEqual(vm.state, "Ready")

    def test_traffic_light_change_state(self):
        """
        Checks if the traffic light changes state correctly.
        """
        tl = TrafficLight()
        self.assertEqual(tl.get_current_state(), "Red")
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Green")
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Yellow")
        tl.change_state()
        self.assertEqual(tl.get_current_state(), "Red")

    def test_user_authentication_login_success(self):
        """
        Checks if the user can log in successfully.
        """
        ua = UserAuthentication()
        self.assertEqual(ua.login(), "Login successful")
        self.assertEqual(ua.state, "Logged In")

    def test_user_authentication_logout_success(self):
        """
        Checks if the user can log out successfully.
        """
        ua = UserAuthentication()
        ua.login()
        self.assertEqual(ua.logout(), "Logout successful")
        self.assertEqual(ua.state, "Logged Out")

    def test_user_authentication_login_error(self):
        """
        Checks if the user cannot log in when already logged in.
        """
        ua = UserAuthentication()
        ua.login()
        self.assertEqual(ua.login(), "Invalid operation in current state")
        self.assertEqual(ua.state, "Logged In")

    def test_user_authentication_logout_error(self):
        """
        Checks if the user cannot log out when already logged out.
        """
        ua = UserAuthentication()
        self.assertEqual(ua.logout(), "Invalid operation in current state")
        self.assertEqual(ua.state, "Logged Out")

    def test_document_editing_system_save_document(self):
        """
        Checks if the document is saved successfully.
        """
        des = DocumentEditingSystem()
        self.assertEqual(des.save_document(), "Document saved successfully")
        self.assertEqual(des.state, "Saved")

    def test_document_editing_system_edit_document(self):
        """
        Checks if the document is edited successfully.
        """
        des = DocumentEditingSystem()
        des.save_document()
        self.assertEqual(des.edit_document(), "Editing resumed")
        self.assertEqual(des.state, "Editing")

    def test_document_editing_system_save_error(self):
        """
        Checks if the document cannot be saved when already saved.
        """
        des = DocumentEditingSystem()
        des.save_document()
        self.assertEqual(des.save_document(), "Invalid operation in current state")
        self.assertEqual(des.state, "Saved")

    def test_document_editing_system_edit_error(self):
        """
        Checks if the document cannot be edited when already being edited.
        """
        des = DocumentEditingSystem()
        self.assertEqual(des.edit_document(), "Invalid operation in current state")
        self.assertEqual(des.state, "Editing")

    def test_elevator_system_move_up(self):
        """
        Checks if the elevator moves up successfully.
        """
        es = ElevatorSystem()
        self.assertEqual(es.move_up(), "Elevator moving up")
        self.assertEqual(es.state, "Moving Up")

    def test_elevator_system_move_down(self):
        """
        Checks if the elevator moves down successfully.
        """
        es = ElevatorSystem()
        self.assertEqual(es.move_down(), "Elevator moving down")
        self.assertEqual(es.state, "Moving Down")

    def test_elevator_system_stop(self):
        """
        Checks if the elevator stops successfully.
        """
        es = ElevatorSystem()
        es.move_up()
        self.assertEqual(es.stop(), "Elevator stopped")
        self.assertEqual(es.state, "Idle")

    def test_elevator_system_move_up_error(self):
        """
        Checks if the elevator cannot move up when already moving.
        """
        es = ElevatorSystem()
        es.move_up()
        self.assertEqual(es.move_up(), "Invalid operation in current state")
        self.assertEqual(es.state, "Moving Up")

    def test_elevator_system_move_down_error(self):
        """
        Checks if the elevator cannot move down when already moving.
        """
        es = ElevatorSystem()
        es.move_down()
        self.assertEqual(es.move_down(), "Invalid operation in current state")
        self.assertEqual(es.state, "Moving Down")

    def test_elevator_system_stop_error(self):
        """
        Checks if the elevator cannot stop when already idle.
        """
        es = ElevatorSystem()
        self.assertEqual(es.stop(), "Invalid operation in current state")
        self.assertEqual(es.state, "Idle")


    def test_banking_system_authenticate_success(self):
        """
        Checks if the user is authenticated successfully.
        """
        bs = BankingSystem()
        self.assertTrue(bs.authenticate("user123", "pass123"))

    def test_banking_system_authenticate_failure(self):
        """
        Checks if the user authentication fails.
        """
        bs = BankingSystem()
        self.assertFalse(bs.authenticate("user123", "wrongpass"))

    def test_banking_system_transfer_money_success(self):
        """
        Checks if the money transfer is successful.
        """
        bs = BankingSystem()
        bs.authenticate("user123", "pass123")
        self.assertTrue(bs.transfer_money("user123", "receiver", 100, "regular"))

    def test_banking_system_transfer_money_failure(self):
        """
        Checks if the money transfer fails.
        """
        bs = BankingSystem()
        self.assertFalse(bs.transfer_money("user123", "receiver", 100, "regular"))

    def test_product_view(self):
        """
        Checks if the product details are displayed correctly.
        """
        product = Product("Laptop", 1000)
        self.assertEqual(product.view_product(), "The product Laptop has a price of 1000")

    def test_shopping_cart_add_product(self):
        """
        Checks if a product is added to the shopping cart.
        """
        cart = ShoppingCart()
        product = Product("Laptop", 1000)
        cart.add_product(product, 2)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]["quantity"], 2)

    def test_shopping_cart_remove_product(self):
        """
        Checks if a product is removed from the shopping cart.
        """
        cart = ShoppingCart()
        product = Product("Laptop", 1000)
        cart.add_product(product, 2)
        cart.remove_product(product, 1)
        self.assertEqual(cart.items[0]["quantity"], 1)

    def test_shopping_cart_checkout(self):
        """
        Checks if the shopping cart checkout works.
        """
        cart = ShoppingCart()
        product = Product("Laptop", 1000)
        cart.add_product(product, 2)
        self.assertEqual(cart.checkout(), None)  


if __name__ == "__main__":
    unittest.main()