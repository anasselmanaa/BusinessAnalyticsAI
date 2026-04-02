from fastapi import FastAPI
from backend_core.routes_upload import router as upload_router
from backend_core.routes_eda import router as eda_router
from backend_core.routes_kmeans import router as kmeans_router
from backend_core.routes_export import router as export_router
from backend_core.database import init_db  # ← ADD THIS

app = FastAPI(
    title="RetailIQ Backend",
    version="2.0"
)

# Create all DB tables on startup
init_db()  # ← ADD THIS

app.include_router(upload_router)
app.include_router(eda_router)
app.include_router(kmeans_router)
app.include_router(export_router)


@app.get("/")
def root():
    return {"status": "ok", "message": "RetailIQ Backend is running"}