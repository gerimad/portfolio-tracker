"""
Asset class definition.
"""

class Asset:
    def __init__(self, name, asset_type, sector, industry) -> None:
        self.name = name
        self.asset_type = asset_type
        self.sector = sector
        self.industry = industry
        