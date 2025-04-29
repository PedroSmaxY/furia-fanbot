# Imagem base Python 3.13 Alpine para menor tamanho
FROM python:3.13-alpine

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Criar diretório de trabalho
WORKDIR /app

# Instalar dependências de compilação (se necessário)
RUN apk add --no-cache gcc musl-dev

# Copiar arquivos de dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código-fonte
COPY . .

# Criar usuário não-root para segurança
RUN addgroup -S botuser && adduser -S botuser -G botuser
USER botuser

# Comando para iniciar o bot
CMD ["python", "main.py"]