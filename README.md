# 🔥 FURIA CS2 FANBOT - Projeto Completo

<div align="center">
  <img src="assets/furia-logo.png" alt="FURIA Logo" width="200"/>
  <h3>🤖 Experiência Conversacional para Fãs da FURIA Esports 🤖</h3>
  <p><i>Solução completa de interação para fãs do time de CS2 FURIA</i></p>
  
  <a href="https://t.me/furiacs2_pedrosmaxy_bot" target="_blank">
    <img src="https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot" />
  </a>
  <a href="https://furia-fanbot.vercel.app/" target="_blank">
    <img src="https://img.shields.io/badge/Vercel-Landing_Page-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Landing Page" />
  </a>
</div>

## 📋 Visão Geral do Projeto

Este projeto é uma solução completa para fãs da FURIA Esports, composta por três componentes principais que trabalham em conjunto:

1. **[Bot de Telegram](#-bot-telegram)**: Chatbot interativo com informações em tempo real
2. **[API Backend](#-api-backend)**: Serviço que fornece dados atualizados da equipe
3. **[Landing Page](#-landing-page)**: Site promocional para divulgação do bot

## 🚀 Subprojetos

### 🤖 Bot Telegram

Bot interativo para Telegram que oferece aos fãs acesso rápido a:

- Últimas notícias da FURIA
- Resultados de partidas recentes
- Próximos jogos e torneios
- Estatísticas detalhadas dos jogadores
- Notificações automáticas de novas partidas

**Tecnologias**: Python, Telebot, APIs externas  
**[Documentação completa do Bot →](./bot/README.md)**

### ⚙️ API Backend

API robusta que alimenta o bot com dados atualizados sobre a FURIA:

- Scraping otimizado de dados de CS2
- Sistema de cache para respostas rápidas
- Endpoints completos para todas as necessidades do bot
- Tratamento de erros e respostas consistentes

**Tecnologias**: Node.js, TypeScript, Fastify, Docker  
**[Documentação completa da API →](./backend/README.md)**

### 🌐 Landing Page

Site moderno e responsivo para divulgação do bot:

- Design Mobile First
- Interface atraente e responsiva
- Apresentação dos recursos do bot
- Chamada para ação para uso do bot
- Integração com redes sociais

**Tecnologias**: Next.js, React, TypeScript, TailwindCSS, Shadcn/UI  
**[Documentação completa da Landing Page →](./landing-page/README.md)**  
**[Ver Landing Page no ar →](https://furia-fanbot.vercel.app/)**

## 📸 Demonstração

<div align="center">
  <h3>📱 Bot em Ação</h3>
  <div style="display: flex; justify-content: center; gap: 20px;">
    <div>
      <img src="https://github.com/user-attachments/assets/bfc749b0-9940-47c7-87e3-c8b2c7020b64" alt="Bot - Tela Inicial" width="250"/>
      <p><i>Menu principal do bot</i></p>
    </div>
    <div>
      <img src="https://github.com/user-attachments/assets/09de3160-f7de-44cd-8a29-9cb4d31bf1e8" alt="Bot - Elenco" width="250"/>
      <p><i>Informações sobre o elenco</i></p>
    </div>
  </div>
  
  <h3>🖥️ Landing Page</h3>
  <img src="https://github.com/user-attachments/assets/5e6e5f1c-6410-4c58-a10f-9f5819e74520" alt="Landing Page - Desktop" width="800"/>
</div>

## 🛠️ Arquitetura do Projeto

```
furia-fanbot/
├── bot/                # Bot de Telegram em Python
│   ├── main.py         # Ponto de entrada do bot
│   ├── src/            # Código fonte do bot
│   └── README.md       # Documentação específica do bot
│
├── backend/            # API em Node.js/TypeScript
│   ├── src/            # Código fonte da API
│   ├── Dockerfile      # Configuração para containerização
│   └── README.md       # Documentação específica da API
│
├── landing-page/       # Site em Next.js
│   ├── src/            # Código fonte do site
│   ├── public/         # Assets estáticos
│   └── README.md       # Documentação específica da landing page
│
└── README.md           # Documentação principal (este arquivo)
```

## 🏁 Como Iniciar

Para executar o projeto completo localmente:

1. **Clone o repositório**

   ```bash
   git clone https://github.com/PedroSmaxY/furia-fanbot.git
   cd furia-fanbot
   ```

2. **Inicie a API**

   ```bash
   cd backend
   npm install
   npm run dev
   ```

3. **Configure e inicie o Bot**

   ```bash
   cd ../bot
   pip install -r requirements.txt
   # Configure o arquivo .env com suas credenciais
   python main.py
   ```

4. **Inicie a Landing Page**
   ```bash
   cd ../landing-page
   npm install
   npm run dev
   ```

## 🐳 Usando Docker (Recomendado)

Para maior facilidade, você pode usar Docker para executar todos os componentes:

```bash
# API Backend
cd backend
docker build -t furia-api .
docker run -p 3000:3000 furia-api

# Bot Telegram
cd ../bot
docker build -t furia-bot .
docker run --env-file .env furia-bot

# Landing Page
cd ../landing-page
docker build -t furia-landing .
docker run -p 3001:3000 furia-landing
```

## 🐳 Docker Compose (Solução Integrada)

Para facilitar ainda mais, o projeto inclui um arquivo `docker-compose.yml` que orquestra todos os serviços juntos:

### Preparação para o Docker Compose

Antes de executar o Docker Compose, certifique-se de configurar corretamente os arquivos de variáveis de ambiente:

1. **Para o Bot Telegram**
```bash
# Na pasta bot, crie um arquivo .env com:
TELEGRAMBOT_KEY=seu_token_do_telegram_bot
PANDASCORE_API_KEY=seu_token_do_pandascore_api
```

```bash
# Na raiz do projeto, execute:
docker-compose up -d
```

### Serviços Configurados

| Serviço          | Porta | Descrição                        |
| ---------------- | ----- | -------------------------------- |
| **backend**      | 3000  | API com dados da FURIA           |
| **bot**          | N/A   | Bot Telegram integrado com a API |
| **landing-page** | 3001  | Site de divulgação               |

### Comandos Úteis

```bash
# Iniciar todos os serviços
docker-compose up -d

# Ver logs em tempo real
docker-compose logs -f

# Ver logs de um serviço específico
docker-compose logs -f bot

# Parar todos os serviços
docker-compose down

# Reconstruir as imagens (após alterações)
docker-compose build --no-cache
```

### Comunicação entre Serviços

Os serviços estão configurados em uma rede interna `furia-network`, permitindo que o bot se comunique automaticamente com a API backend através do hostname `http://backend:3000`.

## 👨‍💻 Desenvolvedor

**Pedro Henrique Novais**  
GitHub: [PedroSmaxY](https://github.com/PedroSmaxY)

## 🏆 Status do Projeto

Este projeto foi desenvolvido para o desafio Experiência Conversacional FURIA:

✅ Bot de Telegram 100% funcional  
✅ API robusta com dados completos  
✅ Landing Page moderna e responsiva  
✅ Integrações entre todos os componentes  
✅ Documentação detalhada

---

<div align="center">
  <h3>🔥 FURIA CS2 FANBOT 🔥</h3>
  <p><i>Este projeto foi desenvolvido para o desafio Experiência Conversacional FURIA, demonstrando habilidades técnicas em desenvolvimento fullstack.</i></p>
</div>
