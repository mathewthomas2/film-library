from fastapi import FastAPI, Depends, status, HTTPException, Response
from schemas import MovieAdd, MovieResponse
from typing import Annotated
from database import engine, get_db, Base
from sqlalchemy import select
from sqlalchemy.orm import Session
import models

app = FastAPI()


dbDep = Annotated[Session, Depends(get_db)]


Base.metadata.create_all(bind=engine)


@app.get("/movies", response_model=list[MovieResponse])
def get_movies(db: dbDep):
    stmt = select(models.MovieLibrary)
    movies = db.scalars(stmt).all()
    return movies



@app.post("/movies", status_code=status.HTTP_201_CREATED, response_model=MovieAdd)
def add_movie(db: dbDep, movie: MovieAdd):
    new_movie = models.MovieLibrary(**movie.model_dump())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


@app.get("/movies/{id}", response_model=MovieResponse)
def get_movie_by_ID(id: int, db: dbDep):

    movie = db.get(models.MovieLibrary, id)   #use for primary key lookups

    # OR

    # stmt = select(models.MovieLibrary).where(models.MovieLibrary.id == id)
    # movie = db.scalars(stmt).first()

    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with id: {id} is not found")

    return movie


@app.delete("/movies/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(id: int, db: dbDep):
    movie = db.get(models.MovieLibrary, id)

    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with id: {id} is not found")

    db.delete(movie)
    db.commit()


