from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import date


class PriceBar(BaseModel):
    ticker:  str
    date:    date
    open:    float = Field(gt=0)
    high:    float = Field(gt=0)
    low:     float = Field(gt=0)
    close:   float = Field(gt=0)
    volume:  int   = Field(ge=0)

    # Field-level validator: clean ticker strings
    @field_validator("ticker")
    @classmethod
    def normalise_ticker(cls, v: str) -> str:
        v = v.strip().upper()
        if not v.isalpha():
            raise ValueError(f"Invalid ticker: {v}")
        return v

    @model_validator(mode="after")
    def check_ohlc_coherence(self) -> "PriceBar":
        if self.high < self.low:
            raise ValueError("high must be >= low")
        if not (self.low <= self.open <= self.high):
            raise ValueError("open must be within [low, high]")
        if not (self.low <= self.close <= self.high):
            raise ValueError("close must be within [low, high]")
        return self



# Now your pipeline rejects corrupt OHLC data automatically
pb = PriceBar(ticker="aapl ", date="2024-01-15",
         open=600, high=190, low=180, close=9, volume=5e7)
