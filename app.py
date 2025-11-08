# app.py
from fastapi import FastAPI
import os

app = FastAPI(title="SimpleHelloAPI")

@app.get("/")
def read_root(name: str = "Mundo"):
    """
    Endpoint que devuelve un saludo personalizado.
    """
    ambiente = os.getenv("AMBIENTE_DESPLIEGUE", "Local")
    saludo = f"Hola, {name}, Jose y Arturo! Saludos desde la arquitectura Serverless en ambiente: {ambiente}"
    return {"message": saludo}