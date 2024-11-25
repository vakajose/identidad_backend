from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import image
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Identidad Backend API",
    description="API para la gestión de Identidad",
    version="1.0.0",
    contact={
        "name": "José Luis Vaca Fernández",
        "email": "vakajose@gmail.com",
    }
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origins
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

#Incluir los routers
app.include_router(image.router, prefix="/image", tags=["image"])


@app.get("/", summary="Endpoint de Bienvenida", response_description="Mensaje de bienvenida")
async def root():
    """
    Endpoint principal de bienvenida de la API.
    """
    return {"message": "Welcome to Identity Backend"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)