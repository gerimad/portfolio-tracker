"""
Portfolio class definition.
"""

class Portfolio:
    def __init__(self):
        self.assets = {}
        self.quantities = {}
        self.prices = {}
    
    def add_asset(self, asset, quantity, price):
        if asset.name not in self.assets:
            self.assets[asset.name] = asset
            self.quantities[asset.name] = quantity
            self.prices[asset.name] = price

    def update_price(self, asset_name, new_price):
        if asset_name in self.prices:
            self.prices[asset_name] = new_price
    
    def calculate_portfolio_value(self):
        total_value = 0
        for asset_name, quantity in self.quantities.items():
            if asset_name in self.prices:
                total_values += self.quantities[asset_name] * self.prices[asset_name]
        return total_value