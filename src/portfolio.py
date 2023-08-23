"""
Portfolio class definition.
"""
from asset import Asset
from typing import Tuple

class Portfolio:
    def __init__(self):
        self.assets = {}
        self.quantities = {}
        self.prices = {}
    
    def add_asset(self, asset: Asset, quantity: int, price: float) -> None:
        """
        Add asset to portfilio.
        """
        if asset.name not in self.assets:
            self.assets[asset.name] = asset
            self.quantities[asset.name] = quantity
            self.prices[asset.name] = price

    def update_price(self, asset_name: str, new_price: float) -> None:
        """
        Update the price of an asset.
        """
        if asset_name in self.prices:
            self.prices[asset_name] = new_price

    def get_asset_info(self, asset_name: str) -> tuple[str, int, float]:
        """
        Get the quantity and price for an asset.
        """
        if asset_name in self.assets:
            if asset_name in self.quantities:
                quantity = self.quantities[asset_name]
                price = self.prices[asset_name]
                return (asset_name, quantity, price)

    
    def calculate_portfolio_value(self) -> float:
        """
        Sum up the values of all assets to calculate the total portfolio value.
        """
        total_value = 0
        for asset_name, _ in self.quantities.items():
            if asset_name in self.prices:
                total_value += self.quantities[asset_name] * self.prices[asset_name]
        return total_value
    
    def calculate_gain_loss(self):
        """
        Calculate the gain or loss for each asset by subtracting the initial purchase price from the current price.
        """
        gain_loss = {}
        for asset_name, initial_price in self.prices.items():
            if asset_name in self.assets:
                if asset_name in self.quantities:
                    current_price = self.assets[asset_name].current_price()
                    quantity = self.quantities[asset_name]
                    gain_loss[asset_name] = (current_price - initial_price) * quantity
        return gain_loss
    
    def calculate_portfolio_performance(self):
        """
        Calculate the overall performance of the portfolio, such as the total gain/loss and percentage return.
        """
        gain_loss = self.calculate_gain_loss()
        total_gain_loss = sum(gain_loss.values())

        initial_investment = sum(self.quantities[asset_name] * self.prices[asset_name] for asset_name in self.assets.keys())
        precentage_return = (total_gain_loss / initial_investment) * 100 if initial_investment != 0 else 0

        return {
            "total_gain_loss" : total_gain_loss,
            "percentage_return": precentage_return,
        }
