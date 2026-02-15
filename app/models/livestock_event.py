import enum
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
from app.database.base import Base


class LivestockType(str, enum.Enum):
    large = "large"
    small = "small"


class EventDirection(str, enum.Enum):
    exit = "exit"
    loading = "loading"


class LivestockEvent(Base):
    __tablename__ = "livestock_events"

    id = Column(String, primary_key=True)

    camera_id = Column(String, ForeignKey("cameras.id"), nullable=False)

    livestock_type = Column(String, nullable=False)
    direction = Column(String, nullable=False)

    track_id = Column(Integer, nullable=True)

    image_path = Column(String, nullable=True)
    vehicle_image_path = Column(String, nullable=True)

    confidence = Column(Float, nullable=True)

    event_time = Column(DateTime, default=datetime.utcnow)

    created_at = Column(DateTime, default=datetime.utcnow)
