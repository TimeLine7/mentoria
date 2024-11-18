from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, crud, database
from app.database import get_db

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return{"message": "Bem vindo a mentoria Educafro"}

@app.get("/usuarios/")
def read_users(skip: int=0, limit:int=10,db: Session = Depends(database.get_db)):
    users = crud.get_users(db,skip=skip, limit=limit)
    return users

@app.get("/usuarios/{usar_id}")
def read_user(user_id:int,db: Session = Depends(database.get_db)):
    user = crud.get_user(db,user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return user

@app.get("/usuarios/{usar_id}")
def create_user(nome:str,email:str,idade:int, db: Session= Depends(database.get_db)):
    new_user = models.User(nome=nome,email=email,idade=idade)
    user = crud.create_user(db, new_user)
    return user

@app.get("/usuarios/{usar_id}")
def update_user(user_id:int, nome:str,email:str,idade:int, db: Session= Depends(database.get_db)):
    user = crud.create_user(db,user_id,email,idade)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return user

@app.get("/usuarios/{usar_id}")
def delete_user(user_id:int, db: Session= Depends(database.get_db)):
    sucess = crud.delete_user(db, user_id)
    if not sucess:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return {"message": "Usuario deletado com sucesso"}