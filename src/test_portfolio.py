import unittest
from asset import Asset
from portfolio import Portfolio

class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.portfolio = Portfolio()

    def test_add_asset(self):
        asset1 = Asset("Apple Inc.", "Stock", "Technology", "Consumer Electronics")

        self.portfolio.add_asset(asset1, quantity=100, price=105.0)

        self.assertIn(asset1.name, self.portfolio.assets)
        self.assertIn(asset1.name, self.portfolio.prices)
        self.assertIn(asset1.name, self.portfolio.quantities)

        self.assertEqual(self.portfolio.assets[asset1.name], asset1)
        self.assertEqual(self.portfolio.prices[asset1.name], 105.0)
        self.assertEqual(self.portfolio.quantities[asset1.name], 100)
        # TODO test if already in, stuff doesnt change

    def test_update_price(self):
        asset1 = Asset("Apple Inc.", "Stock", "Technology", "Consumer Electronics")
        self.portfolio.add_asset(asset1, quantity=50, price=100.0)
        self.portfolio.update_price(asset_name=asset1.name, new_price=150)

        self.assertEqual(self.portfolio.prices[asset1.name], 150)

    def test_calc_portfolio(self):
        asset1 = Asset("Apple Inc.", "Stock", "Technology", "Consumer Electronics")
        asset2 = Asset("Microsoft Corp.", "Stock", "Technology", "Software")
        asset3 = Asset("US Treasury Bond", "Bond", "Government", "Finance")
        
        self.portfolio.add_asset(asset1, quantity=50, price=100.0)
        self.portfolio.add_asset(asset2, quantity=100, price=150.0)
        self.portfolio.add_asset(asset3, quantity=10, price=300.0)

        self.assertEqual(self.portfolio.calculate_portfolio_value(), 23000.0)






        

if __name__ == '__main__':
    unittest.main()
