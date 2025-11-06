import random
from models import Room, Staff
import yaml

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def generate_rooms(cfg):
    rooms = []
    total_rooms = cfg["hotel"]["num_buildings"] * cfg["hotel"]["rooms_per_building"]
    types = cfg["room_types"]

    for i in range(total_rooms):
        building = (i // cfg["hotel"]["rooms_per_building"]) + 1
        r_type = random.choices(types, weights=[t["ratio"] for t in types])[0]["type"]
        rooms.append(Room(id=i+1, building_id=building, room_number=f"{building}-{i%100+1}", type=r_type))
    return rooms

def generate_staff(cfg):
    staff = []
    sid = 1
    for _ in range(cfg["staff"]["supervisors"]):
        staff.append(Staff(id=sid, name=f"Supervisor {sid}", role="supervisor"))
        sid += 1
    for _ in range(cfg["staff"]["housekeepers"]):
        staff.append(Staff(id=sid, name=f"Camarista {sid}", role="housekeeper"))
        sid += 1
    return staff
