from fastapi import FastAPI

app = FastAPI(
    title="Inventory API",
    description="API de cadastro e gestão de produtos.",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "mensagem": "Inventory API funcionando!"
    }