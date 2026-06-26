from fastapi import FastAPI
from pydantic import BaseModel


class Service(BaseModel):
    name: str
    status: str
    version: str


class StatusResponse(BaseModel):
    services: list[Service]


app = FastAPI(title="Homeplane")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/public/status")
def public_status() -> StatusResponse:
    return StatusResponse(
        services=[Service(name="portfolio-web", status="healthy", version="a83f92c")]
    )
