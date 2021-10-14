import unittest
from backpack import Backpack
from cans import Cola
from customer import Customer


class TestGetWalletCoin(unittest.TestCase):
    """Tests for Customer's get_wallet_coin_method"""
    def setUp(self):
        self.customer = Customer()


    def test_can_return_quarter(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.value, .25)

    def test_can_return_dime(self):
        """Pass in 'Dime', method should return a Dime instance"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.value, .10)
        
    def test_can_return_nickel(self):
        """Pass in 'Nickel', method should return a Nickel instance"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.value, .05)
       
    def test_can_return_penny(self):
        """Pass in 'Penny', method should return a Penny instance"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.value, .01)

    def test_can_return_none(self):
        """Pass in any '' other than a coin, method should return a none instance"""
        returned_coin = self.customer.get_wallet_coin('Quartr')
        self.assertIsNone(returned_coin)

class TestAddCoinsToWallet(unittest.TestCase):
    """Test's for adding coins to Customer's wallet"""

    def setUp(self):
        self.customer = Customer()

    def test_add_coins_to_wallet(self):
        """Pass in list of three coins, method should return the updated list"""
        coins = ["Quarter", "Quarter", "Dime"]
        self.customer.add_coins_to_wallet(coins)
        length = len(self.customer.wallet.money)
        self.assertEqual(length, 91)

      
        
    def test_add_nothing_to_wallet(self):
        """Pass in list of nothing, method should return the original list"""
        coins = []
        self.customer.add_coins_to_wallet(coins)
        length = len(self.customer.wallet.money)
        self.assertEqual(length, 0)

    

class TestAddACanToBAckpack(unittest.TestCase):
    """Test's for adding a can to the Customer's Backpack"""

    def setUp(self):
        self.customer = Customer()
        self.backpack = Backpack()

    def test_add_a_can_to_backpack(self):
        """Pass a can object into backpack, method should return length of can added to customers backpack"""

        cola = Cola()
        self.customer.add_can_to_backpack(cola)
        length = len(self.customer.backpack.purchased_cans)      
        self.assertEquals(length, 1)


if __name__ == '__main__':
    unittest.main()