import os

from fastapi import APIRouter, HTTPException, status
from schemas import CedulaSchema, CedulaImageRequest
from services import open_ai


router = APIRouter()


# Ruta para recibir las imágenes en base64
@router.post("/procesar-cedula", response_model=CedulaSchema)
async def procesar_cedula(images: CedulaImageRequest):
    """
        Procesa las imágenes de la cédula enviadas en base64,
        las envía al servicio de OpenAI, y devuelve el JSON resultante.
    """

    # Validar los campos existen
    if not images.anverso or not images.reverso:
        raise HTTPException(status_code=400, detail="Faltan imágenes: anverso y/o reverso.")

    return open_ai.analize_cedula(images)
