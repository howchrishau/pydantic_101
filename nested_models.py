from pydantic import BaseModel, Field
from typing import List, Literal
from datetime import date
from enum import Enum

class AssetClass(str, Enum):
    EQUITY  = "equity"
    FUTURE  = "future"
    FX      = "fx"

class Position(BaseModel):
    ticker:      str
    asset_class: AssetClass
    quantity:    float
    entry_price: float = Field(gt=0)
    currency:    str   = "USD"

    @property
    def notional(self) -> float:
        return self.quantity * self.entry_price

class Portfolio(BaseModel):
    fund_id:    str
    as_of:      date
    positions:  List[Position]   # list of validated Position objects
    base_ccy:   str = "USD"

    @property
    def gross_notional(self) -> float:
        return sum(abs(p.notional) for p in self.positions)

# Pydantic validates each Position in the list automatically
portfolio = Portfolio(
    fund_id="FUND_A",
    as_of="2024-01-15",
    positions=[
        {"ticker": "AAPL", "asset_class": "equity", "quantity": 1000, "entry_price": 182.3},
        {"ticker": "ESZ4",  "asset_class": "future", "quantity": -5,   "entry_price": 4785.0},
    ]
)

print(portfolio.gross_notional)     # 206225.0
print(portfolio.positions[0].asset_class)  # AssetClass.EQUITY
