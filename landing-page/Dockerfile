# Estágio de desenvolvimento - para instalar dependências e construir o projeto
FROM node:lts-alpine AS builder

# Definindo diretório de trabalho
WORKDIR /app

# Copiar arquivos de configuração do projeto
COPY package.json package-lock.json* ./

# Instalar dependências
RUN npm ci

# Copiar código fonte do projeto
COPY . .

# Configurar ambiente para Docker
ENV DEPLOYMENT_ENV=docker

# Construir o projeto Next.js para produção
RUN npm run build

# Estágio de produção - imagem final mais leve
FROM node:20-alpine AS runner

WORKDIR /app

# Definir para ambiente de produção
ENV NODE_ENV=production
ENV DEPLOYMENT_ENV=docker

# Adicionar usuário não-root para segurança
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

# Copiar arquivos de build e dependências necessárias para executar
COPY --from=builder /app/next.config.mjs ./
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

# Mudar para o usuário não-root
USER nextjs

# Expor porta que o servidor Next.js vai utilizar
EXPOSE 3000

# Variável de ambiente que define o hostname interno
ENV HOSTNAME "0.0.0.0"

# Comando para iniciar a aplicação
CMD ["node", "server.js"]