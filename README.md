 # Comic Inventory API

API para la gestión del inventario de cómics.

## Requisitos

- Python instalado.
- Entorno virtual creado en `.venv`.
- Dependencias del proyecto instaladas.

## Linter y formateo

Para comprobar el código con Ruff:

```powershell
.\.venv\Scripts\python.exe -m ruff check .
```

Para corregir automáticamente los problemas detectados:

```powershell
.\.venv\Scripts\python.exe -m ruff check . --fix
```

Para formatear el código:

```powershell
.\.venv\Scripts\python.exe -m ruff format .
```

## Qué revisa Ruff

La configuración actual de Ruff en `pyproject.toml` está enfocada en calidad y estilo de Python:

| Área | Configuración | Descripción |
| --- | --- | --- |
| Longitud de línea | `100` | La línea máxima recomendada es de 100 caracteres. |
| Versión objetivo | `py313` | Se apunta a Python 3.13. |
| Lint seleccionado | `E`, `W`, `F`, `N`, `I`, `B`, `UP` | Revisa errores, warnings, imports, convenciones de nombres, bugs comunes y mejoras de Python moderno. |
| Lint ignorado | `B008` | Se ignora el patrón estándar de FastAPI `Depends(...)` en valores por defecto. |
| Nombre de clases | `classmethod-decorators = []` | Los modelos de SQLAlchemy usan atributos en minúsculas y no requieren decoradores de clase específicos para nombres. |
| Formato de comillas | `double` | Se usa comillas dobles al formatear. |
| Estilo de indentación | `space` | Se usa indentación con espacios. |

## Análisis de seguridad

El proyecto incluye dos herramientas de análisis que solo generan informes y no aplican correcciones automáticas.

### Vulnerabilidades de dependencias

`pip-audit` consulta la base de vulnerabilidades conocida para las dependencias de producción definidas en `requirements.txt` y muestra el paquete, la versión afectada y las vulnerabilidades detectadas.

```powershell
.\.venv\Scripts\python.exe -m pip_audit -r requirements.txt --desc
```

El comando termina con un código de error si encuentra vulnerabilidades. No modifica `requirements.txt`, el entorno virtual ni actualiza paquetes.

### Análisis estático de código

`bandit` revisa patrones de seguridad habituales en Python, como ejecución de comandos, uso inseguro de funciones de evaluación, deserialización y configuración criptográfica. La configuración en `pyproject.toml` excluye los entornos virtuales y archivos compilados.

```powershell
.\.venv\Scripts\python.exe -m bandit -c pyproject.toml -r app
```

Para guardar un informe JSON para revisarlo o consumirlo en integración continua:

```powershell
.\.venv\Scripts\python.exe -m bandit -c pyproject.toml -r app -f json -o bandit-report.json
```

`bandit-report.json` contiene resultados generados; no se debe versionar. Ningún comando de Bandit modifica el código.

## Ejecución

Si el proyecto fue recién clonado, crea el entorno virtual e instala las dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

Desde la raíz del proyecto, ejecuta:

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

La opción `--reload` reinicia automáticamente el servidor cuando detecta cambios en el código.

Una vez iniciada, la API estará disponible en:

- http://127.0.0.1:8000
- Documentación interactiva: http://127.0.0.1:8000/docs
- Documentación alternativa: http://127.0.0.1:8000/redoc
