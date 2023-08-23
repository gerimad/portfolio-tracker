"""
Asset class definition.
"""

def get_stock_price_dummy():
    return 42

class Asset:
    def __init__(self, name: str, asset_type: str, sector: str, industry: str) -> None:
        self.name = name
        self.asset_type = asset_type
        self.sector = sector
        self.industry = industry

    def __repr__(self) -> str:
        return f"Asset({self.name}, {self.asset_type}, {self.sector}, {self.industry})"
        
    def current_price(self, get_price=get_stock_price_dummy) -> float:
        # TODO get real time info
        return get_price()
