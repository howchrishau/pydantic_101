from pydantic import BaseModel, Field

class FactorScore(BaseModel):
    ticker:    str   = Field(min_length=1, max_length=10)
    momentum:  float = Field(ge=-10.0, le=10.0)  # -10 ≤ x ≤ 10
    value:     float = Field(ge=-10.0, le=10.0)
    quality:   float = Field(ge=-10.0, le=10.0)
    z_score:   float = Field(description="Combined z-score, unbounded")

# This will raise: momentum must be ≤ 10
FactorScore(ticker="AAPL", momentum=99.9, value=1.2, quality=0.5, z_score=3.1)
