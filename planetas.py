import numpy as np # algebra lineal
import pandas as pd # procesado de daros, ficheros CSV
import math

def cargarDatos ():
  planetas = pd.read_csv("Planetas.csv")
  return planetas

def calcularGravedad (longitud,tiempo):
  gravedad= (2*longitud)/(tiempo*tiempo)
  return gravedad

def determinarPlaneta (longitud,tiempo):
  gravedad= calcularGravedad (longitud,tiempo)
  planetas= cargarDatos()
  diferencia= 1000000000000000
  candidato= ""
  for indice in planetas.index:
    if abs(gravedad-planetas["Gravedad"][indice])<diferencia:
      diferencia= abs(gravedad-planetas["Gravedad"][indice])
      candidato= planetas["Planeta"][indice]
  return candidato,gravedad
      
