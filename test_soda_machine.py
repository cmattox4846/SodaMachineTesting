import unittest
from cans import Cola
from soda_machine import SodaMachine
import coins

class TestFillRegister(unittest.TestCase):
    """ Test the fill register method """

    def setUp(self):
        self.register = SodaMachine()

    def test_fill_register(self):
        """ Test the length of the register object """
        length = len(self.register.register)
        self.assertEqual(88,length)

class TestFillInventory(unittest.TestCase):
    """ Test the fill inventory method """

    def setUp(self):
        self.inventory = SodaMachine()

    def test_fill_register(self):
        """ Test the length of the register object """
        length = len(self.inventory.inventory)
        self.assertEqual(30,length)

class TestGetCoinFromRegister(unittest.TestCase):
    """ Test the get coin from register method """

    def setUp(self):
        self.coins_from_register = SodaMachine()

    def test_get_coins_from_register_quarter(self):
        """ Test that Quarter can be returned from register """
        coin = self.coins_from_register.get_coin_from_register('Quarter')
        self.assertEqual('Quarter', coin.name)

    def test_get_coins_from_register_dime(self):
        """ Test that Dime can be returned from register """
        coin = self.coins_from_register.get_coin_from_register('Dime')
        self.assertEqual('Dime', coin.name)
    
    def test_get_coins_from_register_nickel(self):
        """ Test that Nickel can be returned from register """
        coin = self.coins_from_register.get_coin_from_register('Nickel')
        self.assertEqual('Nickel', coin.name)
    
    def test_get_coins_from_register_penny(self):
        """ Test that Penny can be returned from register """
        coin = self.coins_from_register.get_coin_from_register('Penny')
        self.assertEqual('Penny', coin.name)

    def test_get_coins_from_register_none(self):
        """ Test that None type can be returned from register """
        coin = self.coins_from_register.get_coin_from_register('test_coin')
        self.assertIsNone(coin)
        

class TestRegisterHasCoins(unittest.TestCase):
    """ Test types of coins that can be returned from the register"""
        
    def setUp(self):
            self.register_has_coins = SodaMachine() 

    def test_register_has_coins(self):
        """ Test that Quarter type can be returned from register """
        answer = self.register_has_coins.register_has_coin('Quarter')
        self.assertTrue(answer)

    def test_register_has_coins(self):
        """ Test that Dime type can be returned from register """
        answer = self.register_has_coins.register_has_coin('Dime')
        self.assertTrue(answer)

    def test_register_has_coins(self):
        """ Test that Nickel type can be returned from register """
        answer = self.register_has_coins.register_has_coin('Nickel')
        self.assertTrue(answer)

    def test_register_has_coins(self):
        """ Test that Penny type can be returned from register """
        answer = self.register_has_coins.register_has_coin('Penny')
        self.assertTrue(answer)

    def test_register_has_coins(self):
        """ Test that False type can be returned from register """
        answer = self.register_has_coins.register_has_coin('test_coin')
        self.assertFalse(answer)


class TestDetermineChangevalue(unittest.TestCase):
    """ Test types of coins that can be returned from the register"""
        
    def setUp(self):
            self.determine_change_value = SodaMachine() 

    def test_determine_change_value_total_higher(self):
        """Test to ensure change value is correct """
        amount = self.determine_change_value.determine_change_value(20, 5)
        self.assertEquals(amount,15)
    
    def test_determine_change_value_soda_higher(self):
        """Test to ensure change value is correct """
        amount = self.determine_change_value.determine_change_value(5, 8)
        self.assertEquals(amount,-3)

    def test_determine_change_value_equal(self):
        """Test to ensure change value is correct """
        amount = self.determine_change_value.determine_change_value(5,5)
        self.assertEquals(amount,0)
 


class TestCalcuateCoinValue(unittest.TestCase):
    """Test takes a can and adds it back into inventory"""
    def setUp(self):
            self.calculate_coin_value = SodaMachine() 

    def test_calculate_coin_value(self):
        """Test the calculation  of coin value"""
        Quarter = coins.Quarter()
        Dime = coins.Dime()
        Nickel = coins.Nickel()
        Penny = coins.Penny()
        coinlist = [Quarter,Dime,Nickel,Penny]
        value_of_coins = self.calculate_coin_value.calculate_coin_value(coinlist)
        self.assertEqual(.41,value_of_coins)

    def test_calculate_coin_value_empty(self):
        """Test the calculation  of coin value with empty list"""
       
        coinlist = []
        value_of_coins = self.calculate_coin_value.calculate_coin_value(coinlist)
        self.assertEqual(0,value_of_coins)

class TestGetInventorySoda(unittest.TestCase):
    """ Test types of coins that can be returned from the register"""
        
    def setUp(self):
            self.get_inventory_soda = SodaMachine()

    def test_get_inventory_soda_cola(self):
        """ Test if result matches soda added 'Cola' """
        ResultCola = self.get_inventory_soda.get_inventory_soda("Cola")
        self.assertEqual(ResultCola.name,"Cola")
    
    def test_get_inventory_soda_rootbeer(self):
        """ Test if result matches soda added 'Root Beer' """
        ResultRootBeer = self.get_inventory_soda.get_inventory_soda("Root Beer")
        self.assertEqual(ResultRootBeer.name,"Root Beer")

    def test_get_inventory_soda_orangesoda(self):
        """ Test if result matches soda added 'Orange Soda' """
        ResultOrangeSoda = self.get_inventory_soda.get_inventory_soda("Orange Soda")
        self.assertEqual(ResultOrangeSoda.name,"Orange Soda")

    
    def test_get_inventory_soda_none(self):
        """ Test if result will return none """
        ResultOrangeSoda = self.get_inventory_soda.get_inventory_soda("Mountain Dew")
        self.assertEqual(ResultOrangeSoda, None)

class TestReturnInventroy(unittest.TestCase):
    """Test returns a soda to the inventory"""
    def setUp(self):
        self.inventory = SodaMachine()

    def test_return_inventory(self):
        """Test adds the can to the total amount of cans"""
        soda = Cola
        self.inventory.return_inventory(soda)
        length = len(self.inventory.inventory)
        self.assertEqual(31,length)



class TestDepositCoinsIntoRegister(unittest.TestCase):
    """ Test types of coins that can be returned from the register"""
        
    def setUp(self):
            self.deposit_coins_into_register = SodaMachine()

    def deposit_coins_into_register(self):
        """Test the calculation  of coin value"""
        Quarter = coins.Quarter()
        Dime = coins.Dime()
        Nickel = coins.Nickel()
        Penny = coins.Penny()
        coinlist = [Quarter,Dime,Nickel,Penny]
        self.deposit_coins_into_register(coinlist)
        self.assertEqual(len(self.register),97)


if __name__ == '__main__':
    unittest.main()