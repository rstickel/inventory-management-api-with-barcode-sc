from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Inventory Management API", description="REST API for inventory management with barcode scanning", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root():
    return {"message": "Inventory Management API", "docs": "/docs", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}
