Programacion-IV
Proyecto Final

El comprimido es el codigo FlaskWebProjectSQL.rar.
Entrar en la carpeta y hacer pip install requirements.txt
Script.Sql es el script de la base de datos completa.
Tarea de pruebas de rendimiento entre Base de Datos Sql server 2014 R2 y Mongo DB 4.0.12
Archivo llamado Pruebas.py
Como se creo la BD para el proyecto solo se agrega una tablas de pruebas script:
USE [Evalueacion] GO SET ANSI_NULLS ON GO

SET QUOTED_IDENTIFIER ON GO

CREATE TABLE [dbo].[Pruebas]( [Id] [bigint] IDENTITY(1,1) NOT NULL, [Nombre] varchar NOT NULL, [Apellido] varchar NOT NULL, [Cedula] varchar NOT NULL, CONSTRAINT [PK_Prubas] PRIMARY KEY CLUSTERED ( [Id] ASC )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY] ) ON [PRIMARY] GO

Tarea del portal de saludos
Archivo comprimmido PortalSaludo.rar, descomprimir y adentro hay un archivo requirements.txt que contiene los modulos necesarios para que el proyecto.
Script de la base de datos del portal de saludos, llamado Saludos.sql
