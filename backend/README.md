# 🔥 FURIA CS2 - API

<div align="center">
  <img src="../assets/furia-logo.png" alt="FURIA Logo" width="200"/>
  <h3>📊 Dados e Estatísticas para Fãs da FURIA Esports 📊</h3>
  <p><i>API completa e atualizada sobre o time de CS2 FURIA Esports</i></p>
  <p><b>Ideal para chatbots, aplicações web e mobile de fãs</b></p>

![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![Fastify](https://img.shields.io/badge/Fastify-202020?style=for-the-badge&logo=fastify&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</div>

## 📋 Descrição

API robusta desenvolvida para fornecer informações completas e atualizadas sobre o time de CS2 FURIA Esports.
Perfeita para integrações com chatbots, aplicações web ou mobile dedicadas aos fãs.

## 🚀 Tecnologias Utilizadas

| Tecnologia                  | Descrição                                        |
| --------------------------- | ------------------------------------------------ |
| ⚙️ **Node.js + TypeScript** | Base de desenvolvimento com tipagem segura       |
| 🚄 **Fastify**              | Servidor web de alta performance                 |
| 🔍 **HLTV Scraping**        | Utilizando a biblioteca gigobyte/HLTV para dados |
| 💾 **In-memory Cache**      | Para resposta ultrarrápida                       |
| 🐳 **Docker**               | Containerização para fácil implantação           |

## 📚 Instalação e Execução

### Pré-requisitos

- [Node.js](https://nodejs.org/) (v22.14.0 ou superior)
- npm (geralmente vem com o Node.js)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/furia-fanbot.git
# OU baixe e extraia o arquivo ZIP do repositório

# Navegue até a pasta da API
cd furia-fanbot/backend/

# Instale as dependências
npm install

# Inicie o servidor de desenvolvimento
npm run dev
```

✅ A API estará disponível em: `http://localhost:3000/api/v1/furia`

## 🐳 Execução com Docker

Para maior portabilidade e facilidade de implantação, você pode utilizar Docker:

```bash
# Construa a imagem Docker
docker build -t furia-api .

# Execute o container
docker run -p 3000:3000 furia-api
```

✅ A API estará disponível em: `http://localhost:3000/api/v1/furia`

## 🛠️ Endpoints Disponíveis

### Estrutura da API

| Método | Rota            | Descrição                        |
| ------ | --------------- | -------------------------------- |
| GET    | `/`             | 📝 Documentação básica da API    |
| GET    | `/api/v1/furia` | 🚪 Endpoint principal de entrada |

### Jogadores e Time

| Método | Rota                                 | Descrição                                         |
| ------ | ------------------------------------ | ------------------------------------------------- |
| GET    | `/api/v1/furia/players/{identifier}` | 👨‍💻 Busca informações de um jogador por ID ou nome |
| GET    | `/api/v1/furia/team/roster`          | 👥 Lista atual de jogadores da FURIA              |
| GET    | `/api/v1/furia/team/coach`           | 🧠 Informações sobre o técnico da equipe          |
| GET    | `/api/v1/furia/team/info`            | ℹ️ Dados gerais do time (fundação, país, etc.)    |

### Estatísticas e Performance

| Método | Rota                                       | Descrição                             |
| ------ | ------------------------------------------ | ------------------------------------- |
| GET    | `/api/v1/furia/team/ranking`               | 🏆 Ranking atual e evolução histórica |
| GET    | `/api/v1/furia/team/stats`                 | 📊 Estatísticas completas do time     |
| GET    | `/api/v1/furia/team/stats/overview`        | 📈 Visão geral rápida de estatísticas |
| GET    | `/api/v1/furia/team/stats/maps`            | 🗺️ Estatísticas de winrate por mapa   |
| GET    | `/api/v1/furia/team/stats/matches?limit=X` | 🏹 Histórico de partidas recentes     |

### Conteúdo e Resumos

| Método | Rota                              | Descrição                                  |
| ------ | --------------------------------- | ------------------------------------------ |
| GET    | `/api/v1/furia/team/news?limit=X` | 📰 Últimas notícias da FURIA               |
| GET    | `/api/v1/furia/team/summary`      | 📋 Resumo completo de todas as informações |

## 💾 Sistema de Cache

- ⚡ Todas as rotas estão cacheadas em memória por padrão
- ⏱️ O tempo de cache padrão é de 1 hora
- 🚀 Evita sobrecarga no scraping e melhora a velocidade de resposta

## 🎯 Exemplos de Respostas

### 📋 Exemplo de `/api/v1/furia/team/coach`

```json
{
  "coach": {
    "id": 24267,
    "name": "sidde",
    "timeOnTeam": "9 months",
    "mapsPlayed": 140,
    "type": "Coach"
  }
}
```

## 🛡️ Tratamento de Erros

A API implementa um sistema robusto de tratamento de erros:

| Código  | Descrição                                                |
| ------- | -------------------------------------------------------- |
| **500** | ❌ Internal Server Error: Falha ao buscar dados          |
| **404** | 🔍 Not Found: Quando jogador ou recurso não é encontrado |

## 👨‍💻 Desenvolvedor

**Pedro Henrique Novais**  
_Projeto desenvolvido para o desafio Experiência Conversacional FURIA_

## 🏆 Status do Projeto

✅ API 100% funcional e cacheada  
✅ Pronta para produção  
✅ Testes realizados em ambientes reais  
✅ Containerização Docker completa

---

<div align="center">
  <h3>🔥 FURIA CS2 FANBOT - API 🔥</h3>
  <p><i>Este projeto foi desenvolvido para fins acadêmicos e demonstração de habilidades técnicas em APIs modernas, scraping seguro e arquitetura REST.</i></p>
</div>
