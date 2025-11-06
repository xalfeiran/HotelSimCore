import asyncio
import random
from datetime import datetime, timedelta
from data.seeds import load_config, generate_rooms, generate_staff
from models import Reservation

rooms = []
staff = []
reservations = []
cfg = None

async def start_simulation():
    global rooms, staff, reservations, cfg
    cfg = load_config()
    rooms = generate_rooms(cfg)
    staff = generate_staff(cfg)
    print(f"🏨 {cfg['hotel']['name']} iniciado con {len(rooms)} habitaciones.")
    asyncio.create_task(simulate_reservations())

async def simulate_reservations():
    global reservations
    interval = cfg["simulation"]["reservation_interval_seconds"]
    avg_stay = cfg["simulation"]["avg_stay_days"]
    rid = 1
    while True:
        free_rooms = [r for r in rooms if not r.occupied]
        if free_rooms:
            room = random.choice(free_rooms)
            room.occupied = True
            res = Reservation(
                id=rid,
                room_id=room.id,
                pax=random.randint(1, 4),
                checkin=datetime.now().date(),
                checkout=(datetime.now() + timedelta(days=avg_stay)).date()
            )
            reservations.append(res)
            print(f"🛏️ Nueva reserva #{rid}: Habitación {room.room_number} ({room.type}) hasta {res.checkout}")
            rid += 1
        else:
            print("⚠️ No hay habitaciones disponibles, esperando...")
        await asyncio.sleep(interval)
