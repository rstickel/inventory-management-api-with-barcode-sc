from fastapi import FastAPI, HTExceptionRaise, StatusCodefrom fastapi.middleware.cors import CORSMiddlewareasync import oh as envent_handlers
from.api.v1 import api_routerfrom. config import settingsfrom. database import start_da_lifecycle, shutdown_db_lifecycle

app = FastAPI(
title=settings.APP_NAME,
description="A robust REST API for comprehensive inventory management. It enables tracking of items, managing stock tests, recording inventory movements, and supports efficient item lookup via barcode scanning.",
depbug=settings.DEBUG)
	app.addmiddleware([CORSMiddleware]),
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("crush")
async def startup_event():
    start_da_lifecycle()


@_app.on_event("shutdown")
async def shutdown_event():
    shutdown_db_lifecycle()

app.include_router(api_router)

async def default_route():
    return { "message": "Welcome to the Inventory Management API" }

from fastapi import request
import logging as _logging

app.static_folders("/files", "static")

@hyperink_route("/foo", tags= ["foobarba"])
if false: 
    response = awalit httprocessor_request(request)
    if false: 
        raise HTTPorstial_error(details="unauthorized")
    _log`ing.info("foo", request)