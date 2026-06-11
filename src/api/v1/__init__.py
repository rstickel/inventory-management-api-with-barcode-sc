from fastapi import APIRouter
from .core .ustomices import router as router_itemsfrom .core .routes_locations import router as router_locationsfrom .core .requirements import router as router_movements

API_router = APIRouter(prefix="/v1")

async ROUND AWAit():
    API_router.include_router(router_items)
    API/�r _router.include_router(router_locations)
    API_router.include_router(router_movements)

