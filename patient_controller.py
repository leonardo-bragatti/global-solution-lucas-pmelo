from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from auth import create_access_token, hash_password
from database.crud import create_patient

from schemas import (
    PatientCreateInput,
    TokenData
)

patient_router = APIRouter(prefix='/patients')


@patient_router.post('/', description='Create a new patient')
async def patient_create(patient_input: PatientCreateInput):
    try:
        patient_input.password = hash_password(patient_input.password)
        doctor = await create_patient(patient_input)
        token = create_access_token(
            data=TokenData(id=doctor.id, name=doctor.name))

        response = {'message': 'Sua conta foi criada com sucesso!'}
        response.set_cookie("session", token, httponly=False,
                            secure=True, samesite="none")
        return response
    except Exception:
        raise HTTPException(
            500, content={"message": "Houve um erro ao criar seu usuário"})


@patient_router.post('/tests', description='Send a new test')
async def send_test():
    try:
        # Aqui poderia ser feito o upload da imagem para o S3 e salvaria o link no banco de dados
        # A IA que irá processar a imagem e retornar o resultado é uma outra API (entrega da materia AI e Chatbot)
        # porém, essa função (feita em flask) está no arquivo ia.py para o entendimento do projeto.

        return {'message': 'ok'}
    except Exception:
        raise HTTPException(
            500, detail={"message": "Houve um erro ao enviar o exame"})
