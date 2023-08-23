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


if __name__ == '__main__':
    unittest.main()
