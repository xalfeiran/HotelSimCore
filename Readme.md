# 🏨 Hotel Simulation Core

**Hotel Simulation Core** es un entorno simulado de operaciones hoteleras enfocado en el área de **Ama de Llaves (Housekeeping)**.  
Su objetivo es servir como base para experimentar, desarrollar e integrar sistemas de planificación, asignación de tareas y productividad dentro de un hotel virtual "vivo".

El sistema genera datos dinámicamente: habitaciones, personal, reservas y eventos simulados de check-in y check-out, todo configurable desde un archivo YAML.

---

## 🚀 Características principales

- Configuración flexible de hotel, edificios, tipos de habitación y personal.  
- Generación automática de habitaciones, personal y reservaciones.  
- Simulación continua de nuevas reservas con tiempos y estancias aleatorias.  
- API REST abierta para consultar el estado actual del hotel.  
- Arquitectura modular lista para expandirse (housekeeping, analytics, mantenimiento, etc.).  
- Construido con **FastAPI**, ideal para proyectos open source o integraciones vía API.

---

## 🧩 Estructura del proyecto

hotel-sim-core/
│
├── main.py # Punto de entrada principal
├── api.py # Endpoints REST
├── simulation.py # Lógica de simulación en tiempo real
├── models.py # Modelos de datos (habitaciones, staff, reservas)
├── config.yaml # Archivo de configuración del hotel
├── data/
│ └── seeds.py # Generadores de datos iniciales
├── requirements.txt # Dependencias de Python
└── README.md


---

## 🧠 Flujo de simulación

Este diagrama representa el ciclo principal de la simulación:  
cómo las reservas y los eventos afectan al área de Ama de Llaves y al hotel en general.

```mermaid
flowchart TD
    A[Inicio del simulador] --> B[Carga de configuración (config.yaml)]
    B --> C[Generación de habitaciones y personal]
    C --> D[Simulación de reservas]
    D -->|Cada X segundos| E[Evento: Nueva reserva]
    E --> F[Habitación marcada como ocupada]
    F --> G[Esperar checkout]
    G -->|Evento: Checkout| H[Crear tarea de limpieza]
    H --> I[Asignar camarista disponible]
    I --> J[Actualizar métricas de productividad]
    J --> D


---

## ⚙️ Requisitos

- Python **3.9 o superior**
- pip (instalador de paquetes)
- Git (opcional, para clonar el repositorio)

---

## 🧰 Instalación

### 1. Clona el repositorio
```bash
git clone https://github.com/tuusuario/hotel-sim-core.git
cd hotel-sim-core

2. Crea un entorno virtual
python3 -m venv venv

3. Activa el entorno virtual
macOS / Linux:
source venv/bin/activate

Windows:
venv\Scripts\Activate.ps1

4. Instala las dependencias
pip install -r requirements.txt

⚙️ Configuración

Edita el archivo config.yaml para personalizar tu simulación.

Ejemplo:

hotel:
  name: "Hotel Simulado Riviera"
  num_buildings: 3
  rooms_per_building: 40

room_types:
  - type: "standard"
    ratio: 0.6
    clean_time: 30
  - type: "premium"
    ratio: 0.3
    clean_time: 45
  - type: "suite"
    ratio: 0.1
    clean_time: 60

staff:
  supervisors: 2
  housekeepers: 8
  max_tasks_per_shift: 10

simulation:
  reservation_interval_seconds: 15
  avg_stay_days: 3
  seed: 42

▶️ Ejecución

Inicia el servidor local con:

python main.py


La aplicación estará disponible en:
👉 http://localhost:8000

Para probar los endpoints interactivos, abre:
👉 http://localhost:8000/docs

Endpoints disponibles:

/api/rooms → lista de habitaciones

/api/staff → lista de empleados

/api/reservations → reservas activas

🧠 Próximas fases

Fase 2: Motor de tareas de limpieza (housekeeping engine)

Fase 3: Métricas y panel visual (ocupación, productividad, eficiencia)

Fase 4: Integraciones externas (reservas, mantenimiento, IoT, etc.)

🤝 Contribuciones

El proyecto está pensado como open source.
Si deseas contribuir:

Haz un fork del repositorio.

Crea una rama para tu feature o fix (git checkout -b feature/nueva-funcionalidad).

Realiza un Pull Request describiendo tus cambios.

📄 Licencia

Distribuido bajo licencia MIT.
Consulta el archivo LICENSE
 para más detalles.

💡 Autor

Desarrollado por Xavier Alfeirán
Mindware / WebRoster Labs – 2025
Cancún, México 🌴