from datetime import date
from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/hotels")
def get_hotels(date_from: date,
               date_to: date,
               location: str,
               has_spa: Optional[bool] = None,
               stars: Optional[int] = Query(None, ge=1, le=5)):
    return date_from, date_to
