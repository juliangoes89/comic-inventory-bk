# comic-inventory-bk — instrucciones para agentes de IA

API en Python (FastAPI + SQLAlchemy) para la gestión del inventario de cómics. Ver [README.md](README.md) para desarrollo y ejecución.

## Reglas de calidad y seguridad estática

Antes de dar por terminada cualquier tarea de código en este proyecto, ejecuta desde la raíz del proyecto:

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m bandit -c pyproject.toml -r app
.\.venv\Scripts\python.exe -m pip_audit -r requirements.txt --desc
```

- `ruff check .` valida estilo y calidad según `pyproject.toml`. No ejecutes `ruff check . --fix` ni `ruff format .` en código de seguridad o lógica de negocio sin revisión humana previa; úsalo solo para estilo trivial (imports, espacios).
- `bandit` analiza patrones de seguridad en `app` (inyección, uso inseguro de `eval`, deserialización, criptografía débil, etc.). No añadas `# nosec` ni excluyas reglas de `[tool.bandit]` en `pyproject.toml` para silenciar hallazgos; corrige el patrón o justifica la excepción en el mismo commit.
- `pip-audit` audita `requirements.txt` contra vulnerabilidades conocidas. Es solo informativo: no actualices versiones de dependencias para "resolver" una vulnerabilidad sin que una persona lo decida y lo pruebe.
- Si añades una dependencia nueva, agrégala con versión fijada (`==`) en `requirements.txt` o `requirements-dev.txt` y vuelve a ejecutar `pip-audit`.
- Mantén la configuración existente de Ruff y Bandit en `pyproject.toml`; no cambies `line-length`, `target-version` ni las reglas seleccionadas salvo que se pida explícitamente.

## Pruebas unitarias y cobertura

- Toda nueva lógica o corrección debe incluir o actualizar pruebas unitarias relevantes.
- Antes de dar por terminada una tarea, ejecuta `.\.venv\Scripts\python.exe -m pytest --cov=app --cov-fail-under=80 -q` y verifica que la cobertura global sea como mínimo del 80%.
- Si la cobertura queda por debajo del 80%, añade las pruebas necesarias; no reduzcas el umbral ni excluyas código para ocultar la falta de cobertura.
