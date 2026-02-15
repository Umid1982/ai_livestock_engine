import enum
from datetime import datetime

from sqlalchemy import Column, String, Boolean, Integer, DateTime
from app.database.base import Base


class CameraMode(str, enum.Enum):
    exit = "exit"
    loading = "loading"


class Camera(Base):
    __tablename__ = "cameras"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    source_type = Column(String, nullable=False, default="rtsp")
    source_path = Column(String, nullable=False)

    mode = Column(String, nullable=False, default=CameraMode.exit.value)

    is_active = Column(Boolean, default=True)

    fps_hint = Column(Integer, default=10)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

