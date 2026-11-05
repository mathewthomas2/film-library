from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text, TIMESTAMP, func
from datetime import date, datetime

class MovieLibrary(Base):
    __tablename__ = "movie_library"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    watched_date: Mapped[date]
    rating: Mapped[float]
    review: Mapped[str | None]
    worth_rewatch: Mapped[bool | None]
    posted_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())