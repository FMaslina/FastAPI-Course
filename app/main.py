from datetime import date
from typing import Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels", response_model=list[SHotel])
def get_hotels(date_from: date,
               date_to: date,
               location: str,
               has_spa: Optional[bool] = None,
               stars: Optional[int] = Query(None, ge=1, le=5)):

    hotels = [
        {
            "address": "Test",
            "name": "Test name",
            "stars": 5
        }
    ]

    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/booking")
def add_booking(booking: SBooking):
    pass
