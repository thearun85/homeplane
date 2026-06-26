from pathlib import Path

import yaml
from fastapi import FastAPI
from pydantic import BaseModel


class ServiceConfig(BaseModel):
    name: str
    image: str
    domain: str
    port: int
    health: str


class ServiceStatus(BaseModel):
    name: str
    status: str
    version: str


class StatusResponse(BaseModel):
    services: list[ServiceStatus]


app = FastAPI(title="Homeplane")


def load_services(path: Path) -> list[ServiceConfig]:
    raw = yaml.safe_load(path.read_text())
    return [ServiceConfig(**item) for item in raw["services"]]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/public/status")
def public_status() -> StatusResponse:
    return StatusResponse(
        services=[ServiceStatus(name="portfolio-web", status="healthy", version="a83f92c")]
    )
