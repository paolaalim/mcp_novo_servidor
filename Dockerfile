# Etapa 1: imagem base
FROM python:3.11-slim

# Etapa 2: definir diretório de trabalho
WORKDIR /app

# Etapa 3: copiar arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server ./server
COPY public ./public

# FastAPI serve estático da pasta public + FastMCP
COPY start.sh .
RUN chmod +x start.sh

# Etapa 4: expor porta
EXPOSE 8000

# Etapa 5: comando de inicialização
CMD ["./start.sh"]
