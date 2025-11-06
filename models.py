from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List

class Room(BaseModel):
    id: int
    building_id: int
    room_number: str
    type: str
    occupied: bool = False

class Staff(BaseModel):
    id: int
    name: str
    role: str
    tasks_completed: int = 0

class Reservation(BaseModel):
    id: int
    room_id: int
    pax: int
    checkin: date
    checkout: date
    active: bool = True

class HotelConfig(BaseModel):
    name: str
    num_buildings: int
    rooms_per_building: int
