from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from mcp.fast import FastMCP
from mcp import tool

app = FastAPI()
mcp = FastMCP()

@app.get("/ping")
def ping():
    return {"status": "ok"}

# Ferramenta 1
@tool()
def contar_palavras(texto: str) -> dict:
    palavras = texto.split()
    return {"quantidade": len(palavras), "palavras": palavras}

# Ferramenta 2
@tool()
def somar(a: int, b: int) -> dict:
    return {"resultado": a + b}

# Interface Web (página HTML)
app.mount("/", StaticFiles(directory="public", html=True), name="static")
app.mount("/mcp", mcp)
