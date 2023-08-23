"""
Portfolio class definition.
"""
from asset import Asset

class Portfolio:
    def __init__(self):
        self.assets = {}
        self.quantities = {}
        self.prices = {}
    
    def add_asset(self, asset: Asset, quantity: int, price: float) -> None:
        if asset.name not in self.assets:
            self.assets[asset.name] = asset
            self.quantities[asset.name] = quantity
            self.prices[asset.name] = price

    def update_price(self, asset_name: str, new_price: float) -> None:
        if asset_name in self.prices:
            self.prices[asset_name] = new_price
    
    def calculate_portfolio_value(self) -> float:
        total_value = 0
        for asset_name, _ in self.quantities.items():
            if asset_name in self.prices:
                total_value += self.quantities[asset_name] * self.prices[asset_name]
        return total_value