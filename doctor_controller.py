from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from auth import create_access_token, hash_password
from database.crud import create_doctor

from schemas import (
    DoctorCreateInput,
    TokenData
)

doctor_router = APIRouter(prefix='/doctors')


@doctor_router.post('/', description='Create a new doctor')
async def doctor_create(doctor_input: DoctorCreateInput):
    try:
        doctor_input.password = hash_password(doctor_input.password)
        doctor = await create_doctor(doctor_input)
        token = create_access_token(
            data=TokenData(id=doctor.id, name=doctor.name))

        response = {'message': 'Sua conta foi criada com sucesso!'}
        response.set_cookie("session", token, httponly=False,
                            secure=True, samesite="none")
        return response
    except Exception:
        raise HTTPException(
            500, detail={"message": "Houve um erro ao criar seu usuário"})


@doctor_router.get('/tests', description='Get all tests')
async def get_tests():
    try:
        # Aqui retornaria todos os exames para o médico avaliar
        # Essa função está aqui apenas para o entendimento do projeto, pois a API de AI e Chatbot irá retornar os exames
        # porém, essa função (feita em flask) está no arquivo ia.py para o entendimento do projeto.
        return {'message': 'ok'}
    except Exception:
        raise HTTPException(
            500, detail={"message": "Houve um erro ao retornar os exames"})
