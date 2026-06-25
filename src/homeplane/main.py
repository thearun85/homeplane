from fastapi import FastAPI

app = FastAPI(title="Homeplane")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/public/status")
def public_status() -> dict[str, list[dict[str, str]]]:
    return {
        "services": [
            {
                "name": "portfolio-web",
                "status": "healthy",
                "version": "a83f92c",
            }
        ]
    }
