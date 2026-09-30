# Omega Infinite OS v4

Prototipo web interactivo del organismo **Belentani / Omega**: WebGL, glassmorphism y matriz de codigo.

## Que es

Una sola pagina que reune la estetica del ecosistema Omega en formato prototipo:
escena WebGL, capas de cristal y un fondo de codigo animado. Es la version 4.

## Estructura

| Archivo | Funcion |
|---|---|
| `index.html` | Pagina unica: escena WebGL, capas glass y matriz |
| `backend.py` | Servidor auxiliar de desarrollo |
| `pyproject.toml` / `requirements.txt` | Dependencias Python |
| `start-omega.ps1` | Arranque en Windows |

## Arranque

```powershell
.\start-omega.ps1
```

O sirviendo la carpeta como estatico:

```bash
python -m http.server 8000
```

## Licencia

MIT - ver `LICENSE`.
