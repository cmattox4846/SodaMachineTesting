import unittest
from coins import Dime, Nickel, Penny, Quarter
import user_interface
from cans import Cola, OrangeSoda, RootBeer


class TestValidateMainMenu(unittest.TestCase):
    """Tests validates main menu user input"""
    def test_validate_main_menu(self):
        """Test validates that input 1 is true and functions"""
        answer_one = user_interface.validate_main_menu(1)
        self.assertEqual(answer_one, (True, 1))
    def test_validate_main_menu_two(self):
        """Test validates that input 2 is true and functions"""
        answer_two = user_interface.validate_main_menu(2)
        self.assertEqual(answer_two, (True, 2))
    def test_validate_main_menu_three(self):
        """Test validates that input 3 is true and functions"""
        answer_three = user_interface.validate_main_menu(3)
        self.assertEqual(answer_three, (True, 3))
    def test_validate_main_menu_four(self):
        """Test validates that input 4 is true and functions"""
        answer_four = user_interface.validate_main_menu(4)
        self.assertEqual(answer_four, (True, 4))
    def test_validate_main_menu_five(self):
        """Test validates that input 5 is false and tells you to enter a proper input"""
        answer_five = user_interface.validate_main_menu(5)
        self.assertEqual(answer_five, (False, None))

class TestTryParseInt(unittest.TestCase):
    """Test to turn string into integer"""
    def test_try_parse_int(self):
        """Test to see if number string changes to integer"""
        answer = user_interface.try_parse_int("10")
        self.assertEqual(answer, 10)
    def test_try_parse_int_word(self):
        """Test to see if entering anything orther than a number string will return 0"""
        answer = user_interface.try_parse_int("hello")
        self.assertEqual(answer, 0)

class TestGetUniqueCanNames(unittest.TestCase):
    """Test to get names of sodas"""
    def test_get_unique_can_names(self):
        """Test takes list of sodas and shows the name of cans"""
        cola = Cola()
        root_beer = RootBeer()
        orange_soda = OrangeSoda()
        list_of_soda = [cola, cola, orange_soda, orange_soda, root_beer, root_beer]
        unique_cans = user_interface.get_unique_can_names(list_of_soda)
        self.assertEqual(len(unique_cans), 3)

    def test_get_unique_can_names_no_cans(self):
        """Test will show no names if no cans are present"""
        list_of_soda = []
        unique_cans = user_interface.get_unique_can_names(list_of_soda)
        self.assertEqual(len(unique_cans), 0)

class TestDisplayPaymentValue(unittest.TestCase):
    """Test disp0lays total payment value"""
    def test_display_payment_value(self):
        """Test adds money entered and shows how much you have entered"""
        penny = Penny()
        nickel = Nickel()
        dime = Dime()
        quarter = Quarter()
        list_of_money = [penny, nickel, dime, quarter]
        total_value = user_interface.display_payment_value(list_of_money)
        self.assertEqual(total_value, .41) 

    def test_display_payment_value_of_nothing(self):
        """Test displays zero when no money entered"""
        list_of_money = []
        total_value = user_interface.display_payment_value(list_of_money)
        self.assertEqual(total_value, 0) 


class TestValidateCoinSelection(unittest.TestCase):
    """Test to validate if a coin is entered"""
    def test_validate_coin_selection(self):
        """Test to accept Quarters"""
        answer_one = user_interface.validate_coin_selection(1)
        self.assertEqual(answer_one, (True, "Quarter"))
    def test_validate_coin_selection_two(self):
        """Test to accept Dimes"""
        answer_two = user_interface.validate_coin_selection(2)
        self.assertEqual(answer_two, (True, "Dime"))
    def test_validate_coin_selection_three(self):
        """Test to accept Nickels"""
        answer_three = user_interface.validate_coin_selection(3)
        self.assertEqual(answer_three, (True, "Nickel"))
    def test_validate_coin_selection_four(self):
        """Test to accept Pennies"""
        answer_four = user_interface.validate_coin_selection(4)
        self.assertEqual(answer_four, (True, "Penny"))
    def test_validate_coin_selection_five(self):
        """Test allows you to finish"""
        answer_five = user_interface.validate_coin_selection(5)
        self.assertEqual(answer_five, (True, "Done"))
    def test_validate_coin_selection_six(self):
        """Test to not allow another input"""
        answer_six = user_interface.validate_coin_selection(6)
        self.assertEqual(answer_six, (False, None))

if __name__ == '__main__':
    unittest.main()