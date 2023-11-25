from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth_controller import auth_router
from doctor_controller import doctor_router
from patient_controller import patient_router

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost",
    "localhost",
    "http://localhost:8080",
    "http://127.0.0.1:3000",
    "127.0.0.1:3000",
    "http://127.0.0.1:3000/",
    "127.0.0.1:3000/"
    "https://neurohub.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE"],
    allow_headers=["*"],
    max_age=3600,
    expose_headers=["set-cookie"]
)

app.include_router(auth_router)
app.include_router(doctor_router)
app.include_router(patient_router)

# !!! Redimencionar imagem com AWS Lambda (serverless) com um trigger numa pasta do S3 seria uma ideia para um projeto completo (se houvesse tempo) !!!
