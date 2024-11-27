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
    prueba: str

    @staticmethod
    def from_dict(source):
        return CedulaImageRequest(
            anverso=source.get('anverso'),
            reverso=source.get('reverso'),
            prueba=source.get('prueba')
        )

    def to_dict(self):
        return {
            "anverso": self.anverso,
            "reverso": self.reverso,
            "prueba":  self.prueba
        }