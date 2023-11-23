from datetime import datetime
from schemas import PatientCreateInput, DoctorCreateInput
from sqlalchemy.ext.asyncio.session import async_session
from database.models import Patients, Doctors
from database.__init__ import async_session
from sqlalchemy.future import select

async def create_doctor(doctor: DoctorCreateInput):
    async with async_session() as session:
        new_doctor = Doctors(
            name=doctor.name,
            email=doctor.email,
            password=doctor.password,
            phone=doctor.phone,
            document=doctor.document,
            crm=doctor.crm,
            address=doctor.address,
            city=doctor.city,
            state=doctor.state,
            zip_code=doctor.zip_code,
            birthday=doctor.birthday,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        session.add(new_doctor)
        await session.commit()
        await session.refresh(new_doctor)
        return new_doctor
    
async def get_doctor_by_email(email: str):
    async with async_session() as session:
        query = await session.execute(select(Doctors).where(Doctors.email == email))
        return query.scalars().first()
    
async def get_patient_by_email(email: str):
    async with async_session() as session:
        query = await session.execute(select(Patients).where(Patients.email == email))
        return query.scalars().first()
    
async def get_doctor_by_id(id: int):
    async with async_session() as session:
        query = await session.execute(select(Doctors).where(Doctors.id == id))
        return query.scalars().first()
    
async def create_patient(patient: PatientCreateInput):
    async with async_session() as session:
        new_patient = Patients(
            name=patient.name,
            email=patient.email,
            password=patient.password,
            phone=patient.phone,
            document=patient.document,
            address=patient.address,
            city=patient.city,
            state=patient.state,
            zip_code=patient.zip_code,
            birthday=patient.birthday,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        session.add(new_patient)
        await session.commit()
        await session.refresh(new_patient)
        return new_patient
    
async def get_all_patients(doctor_id: int):
    async with async_session() as session:
        query = await session.execute(select(Patients).where(Patients.doctor_id == doctor_id))
        return query.scalars().all()