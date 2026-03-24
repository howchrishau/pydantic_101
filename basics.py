from pydantic import BaseModel
from datetime import date
from typing import Optional


class PriceBar(BaseModel):
    ticker: str
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int
    adj_close: Optional[float] = None

bar = PriceBar(**{
    "ticker": "AAPL",
    "date": "2026-03-23",
    "open": "150.00",
    "high": 150.00,
    "low": 150.00,
    "close": 150.00,
    "volume": 58_000_000,
    "adj_close": 150.00,
})

print(bar.close)
print(bar.date)
print(type(bar.date))
print(bar.adj_close)
print(bar.open)
print(type(bar.open))
print(bar.volume)
print(type(bar.volume))
print(bar.model_dump())

# pydantic is lenient with the data types to start
# below raises errors

class PriceBar(BaseModel):
    ticker: str
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int
    adj_close: Optional[float] = None

bar = PriceBar(**{
    "ticker": "AAPL",
    "date": "not-a-date",
    "open": "oops",
    "high": 150.00,
    "low": 150.00,
    "close": 150.00,
    "volume": 58_000_000,
    "adj_close": 150.00,
})

print(bar.close)
print(bar.date)
print(type(bar.date))
print(bar.adj_close)
print(bar.open)
print(type(bar.open))
print(bar.volume)
print(type(bar.volume))
print(bar.model_dump())

# pydantic is lenient with the data types to start


