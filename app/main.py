from fastapi import FastAPI

app = FastAPI(
    title="Nexora Business API",
    description="Business data and KPI API by Nexora Technologies.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Nexora Business API is running",
        "version": "1.0.0"
    }


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "online",
        "service": "Nexora Business API",
        "version": "1.0.0"
    }
