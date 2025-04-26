FROM node:lts-slim AS builder

LABEL version="1.0.0" 
LABEL description="FURIA Fanbot API - CS2 Team Data"
LABEL maintainer="github.com/pedrosmaxy"

# Configura usuário não privilegiado para segurança
RUN groupadd -r nodejs && useradd -g nodejs -s /bin/bash -d /home/nodejs -m nodejs

# Define diretório de trabalho e permissões
WORKDIR /home/nodejs/app
RUN mkdir -p /home/nodejs/app/node_modules && chown -R nodejs:nodejs /home/nodejs/app

# Configura ambiente - ALTERADO: removi NODE_ENV=production no build
ENV NPM_CONFIG_LOGLEVEL=warn

# Copia arquivos de configuração
COPY --chown=nodejs:nodejs package*.json tsconfig.json ./

# Instala dependências como usuário não privilegiado, incluindo as de desenvolvimento
USER nodejs
RUN npm ci && npm cache clean --force

# Copia código fonte
COPY --chown=nodejs:nodejs src/ ./src/

# Compila TypeScript para JavaScript
RUN npm run build

# Estágio de produção com imagem menor
FROM node:lts-slim AS production

# Configura usuário não privilegiado
RUN groupadd -r nodejs && useradd -g nodejs -s /bin/bash -d /home/nodejs -m nodejs

# Define diretório e ambiente
WORKDIR /home/nodejs/app

# CORREÇÃO: Crie e configure as permissões do diretório node_modules
RUN mkdir -p /home/nodejs/app/node_modules && chown -R nodejs:nodejs /home/nodejs/app

ENV NODE_ENV=production

# Copia arquivos de configuração
COPY --chown=nodejs:nodejs package*.json ./

# Instala apenas dependências de produção
USER nodejs
RUN npm ci --omit=dev && npm cache clean --force

# Copia arquivos compilados do estágio de build
COPY --chown=nodejs:nodejs --from=builder /home/nodejs/app/dist ./dist

# Porta que o serviço utilizará
EXPOSE 3000

# Comando para iniciar a aplicação
CMD ["node", "dist/server.js"]