from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, crud, database
from app.database import get_db

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"message": "mentoria com Fernanda e Yara."}


@app.get("/usuarios/total/")
def total_users(db: Session = Depends(database.get_db)):
    todos = crud.get_total(db)
    return {"todos": todos}

@app.get("/usuarios/busca/")
def search_users(nome: str ,db: Session = Depends(database.get_db)):
    users = crud.get_for_name(db, nome=nome)
    if not users:
        raise HTTPException(status_code=404, detail="nome não encontrado")
    return {"users": [nome[0] for nome in users]}
    
@app.get("/usuarios/")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/usuarios/{user_id}")
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@app.post("/usuarios/")
def create_user(nome: str, email: str, idade: int, db: Session = Depends(database.get_db)):
    new_user = models.User(nome=nome, email=email, idade=idade)
    user = crud.create_user(db, new_user)
    return user

@app.put("/usuarios/{user_id}")
def update_user(user_id: int, nome: str, email: str, idade: int, db: Session = Depends(database.get_db)):
    user = crud.update_user(db, user_id, nome, email, idade)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@app.delete("/usuarios/{user_id}")
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    success = crud.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário deletado com sucesso"}
