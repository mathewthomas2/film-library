from typing import Annotated
from datetime import date, datetime
from pydantic import BaseModel, Field, field_validator, ConfigDict, StringConstraints


class BaseMovie(BaseModel):
    title: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    watched_date: date
    rating: Annotated[float, Field(ge=0.5, le=5.0)]
    review: Annotated[str | None, Field(max_length=100)] = None
    worth_rewatch: bool | None = None

class MovieAdd(BaseMovie):

    @field_validator("watched_date")
    @classmethod
    def check_date(cls, v: date)-> date:
        if v > date.today():
            raise ValueError(f"Watched date cannot be beyond {date.today()}. Enter a valid date")
        return v

    @field_validator("rating")
    @classmethod
    def checkrating(cls, v: float) -> float:
        if (v*2) % 1 != 0:
            raise ValueError("Rating must be in steps of 0.5")
        return v
    
class MovieResponse(BaseMovie):
    model_config = ConfigDict(from_attributes=True)
    id: int
    posted_at: datetime
    
