from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    user_type = Column(String, nullable=False)  # "passenger" or "pilot"

    rides = relationship("Ride", back_populates="pilot", lazy="joined", foreign_keys="Ride.pilot_id")

class Ride(Base):
    __tablename__ = "rides"

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, default="requested")  # "requested", "accepted", "completed"

    passenger_id = Column(Integer, nullable=False)
    pilot_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    pilot = relationship("User", back_populates="rides", lazy="joined", foreign_keys=[pilot_id])
