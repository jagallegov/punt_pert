from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_excel("punt_pert.xlsx")

@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando"
    }

@app.get("/programas")
def obtener_programas():
    return df.to_dict(orient="records")

@app.get("/programas/{codigo_snies}")
def obtener_programa(codigo_snies: int):

    fila = df[
        df["codigo_snies"] == codigo_snies
    ]

    if fila.empty:
        return {
            "error": "Código SNIES no encontrado"
        }

    return fila.iloc[0].to_dict()