from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..auth import get_db, get_current_user

router = APIRouter()

@router.post("/request", response_model=schemas.RideOut)
def request_ride(
    ride_data: schemas.RideCreate, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    # Only passengers should request rides
    if current_user.user_type != "passenger":
        raise HTTPException(status_code=403, detail="Only passengers can request rides.")

    new_ride = models.Ride(
        origin=ride_data.origin,
        destination=ride_data.destination,
        price=ride_data.price,
        passenger_id=current_user.id,
        status="requested"
    )
    db.add(new_ride)
    db.commit()
    db.refresh(new_ride)

    return new_ride

@router.post("/{ride_id}/accept", response_model=schemas.RideOut)
def accept_ride(
    ride_id: int, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    # Only pilots can accept rides
    if current_user.user_type != "pilot":
        raise HTTPException(status_code=403, detail="Only pilots can accept rides.")

    ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found.")
    if ride.status != "requested":
        raise HTTPException(status_code=400, detail="Ride cannot be accepted; not in 'requested' state.")

    ride.status = "accepted"
    ride.pilot_id = current_user.id
    db.commit()
    db.refresh(ride)

    return ride

@router.post("/{ride_id}/complete", response_model=schemas.RideOut)
def complete_ride(
    ride_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    ride = db.query(models.Ride).filter(models.Ride.id == ride_id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found.")
    if ride.status != "accepted":
        raise HTTPException(status_code=400, detail="Ride is not in 'accepted' state.")

    # Only the pilot who accepted can complete
    if ride.pilot_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the pilot for this ride.")

    ride.status = "completed"
    db.commit()
    db.refresh(ride)

    return ride
