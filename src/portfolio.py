
class Portfolio:
    def __init__(self):
        self.assets = {}
        self.quantities = {}
        self.prices = {}
    
    def add_asset(self, asset, quantity, price):
        if asset.name