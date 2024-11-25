from openai import OpenAI
from dotenv import load_dotenv
from schemas import CedulaSchema
import os

from schemas import CedulaImageRequest

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    organization=os.getenv('OPENAI_ORG_ID'),
    project=os.getenv('OPENAI_PROJECT_ID'),
)


def analize_cedula(images: CedulaImageRequest):
    instructions = _get_instructions(1)
    messages = _get_message(instructions, images)


    response = client.beta.chat.completions.parse(
        model=os.getenv('OPENAI_MODEL') or 'gpt-4o-mini',
        messages=messages,
        response_format=CedulaSchema,
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    return response.choices[0].message.parsed


def _get_instructions(document_type):
    if document_type == 1:
        return "Extrae el texto de las imagenes, las cuales son el anverso y reverso de una cedula de identidad. Entregala en formato JSON siguiendo el siguiente json schema: {\"$schema\":\"http://json-schema.org/draft-07/schema#\",\"title\":\"Cedula\",\"type\":\"object\",\"properties\":{\"nombre\":{\"type\":\"string\"},\"numero\":{\"type\":\"string\"},\"fechaNacimiento\":{\"type\":\"string\",\"format\":\"date\"},\"lugarNacimiento\":{\"type\":\"string\"},\"estadoCivil\":{\"type\":\"string\"},\"profesion\":{\"type\":\"string\"},\"domicilio\":{\"type\":\"string\"},\"serie\":{\"type\":\"string\"},\"seccion\":{\"type\":\"string\"},\"fechaEmision\":{\"type\":\"string\",\"format\":\"date\"},\"fechaExpiracion\":{\"type\":\"string\",\"format\":\"date\"}},\"required\":[\"nombre\",\"numero\",\"fechaNacimiento\",\"lugarNacimiento\",\"estadoCivil\",\"profesion\",\"domicilio\",\"serie\",\"seccion\",\"fechaEmision\",\"fechaExpiracion\"],\"additionalProperties\":false}\n"
    elif document_type == 2:
        return "Extrae el texto de las imagenes, las cuales son el anverso y reverso de una licencia de conducir. Entregala en formato JSON siguiendo el siguiente json schema:"


def _get_message(instructions, images: CedulaImageRequest):
    return [
        {
            "role": "system",
            "content": [
                {
                    "text": instructions,
                    "type": "text"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": images.anverso
                    }
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": images.reverso
                    }
                }
            ]
        }
    ]
