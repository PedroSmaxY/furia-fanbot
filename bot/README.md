# 🔥 FURIA CS2 - Fanbot

<div align="center">
    <img src="../assets/furia-logo.png" alt="FURIA Logo" width="200"/>
    <h3>📊 O Bot Oficial da FURIA no Telegram 📊</h3>
    <p><i>Interaja com seu time favorito: estatísticas, resultados e novidades em tempo real!</i></p>
    <p><b>Ideal para fãs, comunidades, e eventos de CS2</b></p>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Telebot](https://img.shields.io/badge/Telebot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white) ![httpx](https://img.shields.io/badge/httpx-003366?style=for-the-badge&logo=python&logoColor=white) ![dotenv](https://img.shields.io/badge/dotenv-3A3A3A?style=for-the-badge&logo=python&logoColor=white) ![Pandascore](https://img.shields.io/badge/Pandascore-1B1B1B?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnPjxwYXRoIGQ9J00gMCAwaCAxMDAwdjEwMDBIMHonIGZpbGw9JyNGRkMnLz48L3N2Zz4=)

</div>

## 📑 Índice

- [🔥 FURIA CS2 - Fanbot](#-furia-cs2---fanbot)
  - [📑 Índice](#-índice)
  - [🚀 Tecnologias Utilizadas](#-tecnologias-utilizadas)
  - [📃 Instalação e Execução](#-instalação-e-execução)
    - [Pré-requisitos](#pré-requisitos)
    - [Instalação Padrão](#instalação-padrão)
    - [🐳 Execução com Docker](#-execução-com-docker)
  - [🎮 Funcionalidades Disponíveis](#-funcionalidades-disponíveis)
  - [📆 Exemplos de Resposta](#-exemplos-de-resposta)
    - [/start](#start)
    - [/resumo](#resumo)
    - [/elenco](#elenco)
    - [/partidas](#partidas)
  - [📱 Screenshots](#-screenshots)
  - [🔌 Integrações de API](#-integrações-de-api)
  - [🛡️ Tratamento de Erros](#️-tratamento-de-erros)
  - [🏆 Status do Projeto](#-status-do-projeto)
  - [👨‍💻 Desenvolvedor](#-desenvolvedor)

## 🚀 Tecnologias Utilizadas

| Tecnologia                 | Descrição                                     |
| -------------------------- | --------------------------------------------- |
| 👉 **Python 3.13**         | Linguagem base do projeto                     |
| 👉 **Telebot**             | Biblioteca para criação do bot Telegram       |
| 👉 **httpx**               | Requisições HTTP assíncronas                  |
| 👉 **dotenv**              | Gerenciamento de variáveis de ambiente        |
| 👉 **Pandascore API**      | Dados esportivos atualizados                  |
| 👉 **API Própria (FURIA)** | Dados extras HLTV/estatísticas personalizadas |

## 📃 Instalação e Execução

### Pré-requisitos

- Python 3.13+
- Conta de Bot criada no Telegram (@BotFather)

### Instalação Padrão

```bash
# Clone o repositório
git clone https://github.com/PedroSmaxY/furia-fanbot.git

# Navegue até a pasta do bot
cd furia-fanbot/bot/

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas credenciais

# Execute o bot
python ./main.py
```

### 🐳 Execução com Docker

Para maior portabilidade e facilidade de implantação, você pode utilizar Docker:

```bash
# Construa a imagem Docker
docker build -t furia-bot .

# Execute o container
docker run -d --env-file .env --name furia-chatbot furia-bot
```

✅ O bot estará ativo e pronto para uso!

Link do Bot no Telegram: [https://t.me/furiacs2_pedrosmaxy_bot](https://t.me/furiacs2_pedrosmaxy_bot)

## 🎮 Funcionalidades Disponíveis

| Comando             | Função                                     |
| ------------------- | ------------------------------------------ |
| `/start`            | Introdução ao Bot e opções iniciais        |
| `/resumo`           | Estatísticas gerais e conquistas           |
| `/elenco`           | Jogadores atuais da equipe                 |
| `/news`             | Últimas notícias e atualizações            |
| `/partidas`         | Resultados recentes                        |
| `/proximaspartidas` | Próximos jogos agendados (mock caso vazio) |
| `/notificacoes`     | Ativa/Desativa alertas de novas partidas   |
| `/info`             | Informações gerais da organização          |

## 📆 Exemplos de Resposta

### /start

```plaintext
🏆 BEM-VINDO AO BOT OFICIAL DA FURIA ESPORTS! 🏆
Escolha uma opção ou digite um comando:
• /resumo • /elenco • /news • /partidas • /proximaspartidas • /notificacoes • /info
```

### /resumo

```plaintext
🎴 Estatísticas Gerais:
- 1355 mapas jogados
- 806 vitórias
- K/D Ratio: 1.07

Top Mapas:
- Mirage (60.8% Winrate)
- Inferno (59.1% Winrate)
- Nuke (56.1% Winrate)
```

### /elenco

```plaintext
👥 Titulares:
- yuurih (BR)
- KSCERATO (BR)
- FalleN (BR)
...
```

### /partidas

```plaintext
🎾 Resultados Recentes:
- FURIA 11x13 The MongolZ (Nuke)
- FURIA 9x13 The MongolZ (Mirage)
...
```

## 📱 Screenshots

<div align="center">
    <img src="https://github.com/user-attachments/assets/bfc749b0-9940-47c7-87e3-c8b2c7020b64" alt="Comando /start" width="300"/>
    <p><i>Tela inicial do bot após o comando /start</i></p>
</div>

<div align="center">
    <img src="https://github.com/user-attachments/assets/09de3160-f7de-44cd-8a29-9cb4d31bf1e8" alt="Comando /elenco" width="300"/>
    <p><i>Visualização do elenco atual da FURIA /elenco</i></p>
</div>

<div align="center">
    <img src="https://github.com/user-attachments/assets/423b5301-b60d-4ca0-92df-b746227cc844" alt="Comando /partidas" width="300"/>
    <p><i>Resultados das partidas recentes /partidas</i></p>
</div>

## 🔌 Integrações de API

| API                      | Uso                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------- |
| 🔥 **API Própria FURIA** | API customizada com dados exclusivos e estatísticas personalizadas                     |
| 🐼 **PandaScore API**    | API externa para complementar informações de torneios, partidas e estatísticas globais |

## 🛡️ Tratamento de Erros

O bot implementa um robusto sistema de tratamento de erros:

- ⚠️ Mensagens amigáveis em caso de falha na API funcional
- 🕑 Indicação quando os dados estão sendo atualizadosAPI própria
- ✅ Validação de respostas HTTP com tratamento de exceções

## 🏆 Status do Projeto

O bot implementa um robusto sistema de tratamento de erros:

- ✅ Bot 100% funcional
- ✅ Integração completa com Pandascore + API própria
- ✅ Código organizado e profissional afio Experiência Conversacional FURIA, demonstrando habilidades em integração de APIs esportivas, arquitetura escalável e experiência conversacional para fãs.
- ✅ Pronto para demonstração e apresentação

## 👨‍💻 Desenvolvedor

**Pedro Henrique Novais**  
GitHub: [PedroSmaxY](https://github.com/PedroSmaxY)

<div align="center">
    <h3>
      🔥 FURIA CS2 FANBOT - Telegram 🔥
    </h3>
    <p><i>Este projeto foi desenvolvido para o desafio Experiência Conversacional FURIA, demonstrando habilidades em integração de APIs esportivas, arquitetura escalável e experiência conversacional para fãs.</i></p>
</div>
