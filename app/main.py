from datetime import date
from typing import Optional

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

app = FastAPI()


class SHotelSearchArgs:
    def __init__(self,
                 date_from: date,
                 date_to: date,
                 location: str,
                 has_spa: Optional[bool] = None,
                 stars: Optional[int] = Query(None, ge=1, le=5)
                 ):
        self.date_from = date_from
        self.date_to = date_to
        self.location = location
        self.has_spa = has_spa
        self.stars = stars


@app.get("/hotels")
def get_hotels(search_args: SHotelSearchArgs = Depends()):
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/booking")
def add_booking(booking: SBooking):
    pass
