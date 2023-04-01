from fastapi import FastAPI
from app.api.routers.ai_store import router
from database import Base, engine
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/images", tags=["images"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)