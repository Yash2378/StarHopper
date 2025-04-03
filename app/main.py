from fastapi import FastAPI
from .routes import users, rides
from .database import Base, engine

# Create all tables (for quickstart/demo).
# In production, use Alembic migrations instead.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="StarHopper")

@app.get("/")
def root():
    return {"message": "Welcome to StarHopper. Explore the cosmos!"}

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(rides.router, prefix="/rides", tags=["rides"])
