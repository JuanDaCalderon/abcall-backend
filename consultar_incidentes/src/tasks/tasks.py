from typing import List
from sqlalchemy.orm import Session
from ..models import models


def get(db: Session) -> List[models.Incidentes]:
    incidentes: List[models.Incidentes] = db.query(models.Incidentes).all()
    return incidentes

def getIncidenteByCliente(db: Session, client:str):
    incidentes: List[models.Incidentes] = db.query(models.Incidentes).filter(models.Incidentes.CLIENTE == client).all()
    return incidentes 

def getIncidenteByUsuario(db: Session, usuario:str):
    incidentes: List[models.Incidentes] = db.query(models.Incidentes).filter(models.Incidentes.USUARIO == usuario).all()
    return incidentes 
def reset_db(db: Session):
    db.query(models.Incidentes).delete()
    db.commit()
