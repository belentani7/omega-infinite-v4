from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil
import platform
import random
import time
import os

app = FastAPI(title="Omega Infinite OS Core API", version="10.0.4")

# Configurar CORS para permitir que el frontend se comunique con el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

START_TIME = time.time()

@app.get("/")
def read_root():
    return {"status": "OMEGA CORE ONLINE", "version": "10.0.4"}

@app.get("/api/system")
def get_system_stats():
    return {
        "cpu_usage": psutil.cpu_percent(interval=0.1),
        "ram_usage": psutil.virtual_memory().percent,
        "uptime": round(time.time() - START_TIME, 2),
        "platform": platform.system(),
        "arch": platform.architecture()[0],
        "node": platform.node()
    }

@app.get("/api/agents")
def get_agent_matrix():
    # Simula el estado de 300 agentes de OpenClaw/Manus
    agents = []
    for i in range(300):
        agents.append({
            "id": i,
            "status": "active" if random.random() > 0.85 else "idle",
            "load": round(random.uniform(0.1, 99.9), 2),
            "archetype": random.choice(["PEDRO", "MARCOS", "SANTOS", "BELENTANI", "JUDAS", "UNKNOWN"])
        })
    return {"total": 300, "nodes": agents}

@app.get("/api/repos")
def get_repos():
    # Escanea el directorio belentani-unified
    base_path = os.path.expanduser("~/belentani-unified")
    structure = {}
    if os.path.exists(base_path):
        for root, dirs, files in os.walk(base_path):
            rel_path = os.path.relpath(root, base_path)
            if rel_path == ".": continue
            structure[rel_path] = {"dirs": len(dirs), "files": len(files)}
    
    return {"unified_path": base_path, "structure": structure}

@app.post("/api/judas/ignite")
def ignite_judas():
    # Endpoint simulado para activar el motor de audio local
    return {"status": "AUDIO ENGINE IGNITED", "resonance": "MAXIMUM", "frequencies": [432, 528, 639, 741, 852]}

@app.post("/api/security/lockdown")
def trigger_lockdown():
    # Simulacro de Man-In-The-Middle defense
    return {"status": "LOCKDOWN INITIATED", "level": "CRITICAL", "message": "ALL PROTOCOLS OVERRIDDEN"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
