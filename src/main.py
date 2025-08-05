from fastapi import FastAPI
import sqlite3

from src.routes import (
    fields,
    treatments,
    incomes,
    expenses,
    inventory,
    dropdowns,
)

app = FastAPI(title="Agri Manager")


@app.on_event("startup")
def startup() -> None:
    app.state.db = sqlite3.connect("agri_manager.db")


@app.on_event("shutdown")
def shutdown() -> None:
    app.state.db.close()


app.include_router(fields.router)
app.include_router(treatments.router)
app.include_router(incomes.router)
app.include_router(expenses.router)
app.include_router(inventory.router)
app.include_router(dropdowns.router)


__all__ = ["app"]
