from datetime import datetime
from pydantic import BaseModel

class SucessAuthOutput(BaseModel):
    message: str

class ErrorOutput(BaseModel):
    message: str

class TokenData(BaseModel):
    id: int
    name: str

class DoctorCreateInput(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    document: str
    crm: str
    address: str
    city: str
    state: str
    zip_code: str
    birthday: datetime

class PatientCreateInput(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    document: str
    address: str
    city: str
    state: str
    zip_code: str
    birthday: datetime

class LoginInput(BaseModel):
    email: str
    password: str
    type: str

class VerifyTokenOutput(BaseModel):
    name: str