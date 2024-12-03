from sqlalchemy.orm import Session
from . import models

def get_total(db: Session):
    return db.query(models.User).all()

def get_for_name(db: Session, nome: str):
    return db.query(models.User.nome).filter(models.User.nome.ilike(f"%{nome}%")).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0,limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: models.User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, user_id: int, nome: str, email:str, idade:int):
    user = get_user(db, user_id)
    if user:
        user.nome = nome
        user.email = email
        user.idade = idade
        db.commit()
        db.refresh(user)
        return user
    return None

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
