from fastapi import FastAPI
from api.routes import health_assistant

app = FastAPI(title="Health Assistant API", description="An API for predictive health diagnostics", version="1.0")

# Include routes
app.include_router(health_assistant.router, prefix="/health", tags=["Health Assistant"])

@app.get("/")
def root():
    return {"message": "Health Assistant API is running!"}
