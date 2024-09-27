from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.models.modelosApp import Usuario
from app.api.schemas.DTO import GastoDTOPeticion, GastoDTORespuesta
from app.api.models.modelosApp import Gasto
from app.api.schemas.DTO import CategoriaDTOPeticion, CategoriaDTORespuesta
from app.api.models.modelosApp import Categoria
from app.api.schemas.DTO import MetodoPagoDTOPeticion, MetodoPagoDTORespuesta
from app.api.models.modelosApp import MetodoPago
from app.database.configuration import sessionLocal, engine

#Para que un API funcione debe tener un archivo enrutador

rutas=APIRouter()  #ENDPOINT 

#Crear una función para establecer cuando yo quiera y necesite conexión hacia la BD

def getDataBase():
    baseDatos=sessionLocal()
    try:
        yield baseDatos
    except Exception as error:
        baseDatos.rollback()
        raise error
    finally:
        baseDatos.close()

#Programación de cada uno de los servicios que ofrecerá nuestra API

#Servicio para registrar o guardar un usuario en la BD

@rutas.post("/usuarios")
def guardarUsuario(datosPeticion:UsuarioDTOPeticion, db:Session=Depends(getDataBase)): #db activa la conexión a la BD
    try:
        usuario=Usuario(
            nombres=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        ) 
        db.add(usuario) #agrego
        db.commit() #ejecuto
        db.refresh(usuario) #refresco
        return usuario #retorno el usuario registrado
    except Exception as error:
        db.rollback() #frena la operacion
        raise HTTPException()

@rutas.post("/gastos")
def guardarGastos(datosPeticion:GastoDTOPeticion, db:Session=Depends(getDataBase)): #db activa la conexión a la BD
    try:
        gasto=Gasto(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            nombre=datosPeticion.nombre,
        ) 
        db.add(gasto) #agrego
        db.commit() #ejecuto
        db.refresh(gasto) #refresco
        return gasto #retorno el usuario registrado
    except Exception as error:
        db.rollback() #frena la operacion
        raise HTTPException()
    
@rutas.post("/categorias")
def guardarCategoria(datosPeticion:CategoriaDTOPeticion, db:Session=Depends(getDataBase)): #db activa la conexión a la BD
    try:
        categoria=Categoria(
            nombreCategoria=datosPeticion.nombreCategoria,
            descripcion=datosPeticion.descripcion,
            fotoicono=datosPeticion.fotoicono,
        ) 
        db.add(categoria) #agrego
        db.commit() #ejecuto
        db.refresh(categoria) #refresco
        return categoria #retorno el usuario registrado
    except Exception as error:
        db.rollback() #frena la operacion
        raise HTTPException()
    
@rutas.post("/metodos_pagos")
def guardarMetodoPago(datosPeticion:MetodoPagoDTOPeticion, db:Session=Depends(getDataBase)): #db activa la conexión a la BD
    try:
        metodoPago=MetodoPago(
            nombreMetodo=datosPeticion.nombreMetodo,
            descripcion=datosPeticion.descripcion
        )
        db.add(metodoPago) #agrego
        db.commit() #ejecuto
        db.refresh(metodoPago) #refresco
        return metodoPago #retorno el usuario registrado
    except Exception as error:
        db.rollback() #frena la operacion
        raise HTTPException()

    
