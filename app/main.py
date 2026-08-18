from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import comics, editoriales

app = FastAPI(
    title="Comic Inventory API",
    description="API for managing a comic book collection backed by Azure SQL",
    version="0.1.0",
)

# Open CORS for local development; restrict before going to production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(comics.router)
app.include_router(editoriales.router)


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
