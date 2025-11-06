from fastapi import APIRouter
from simulation import rooms, staff, reservations

router = APIRouter()

@router.get("/rooms")
def get_rooms():
    return rooms

@router.get("/staff")
def get_staff():
    return staff

@router.get("/reservations")
def get_reservations():
    return reservations
