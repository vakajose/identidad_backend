from pydantic import BaseModel
class CedulaSchema(BaseModel):
    nombre: str
    numero: str
    fechaNacimiento: str
    lugarNacimiento: str
    estadoCivil: str
    profesion: str
    domicilio: str
    serie: str
    seccion: str
    fechaEmision: str
    fechaExpiracion: str

class CedulaImageRequest(BaseModel):
    anverso: str
    reverso: str