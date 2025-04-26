export const apiDocumentation = {
  title: "FURIA FanBot API",
  description: "API para consulta de informações do time FURIA Esports de CS2",
  version: "1.0.0",
  routes: {
    "/": "Documentação da API",
    "/api/v1/furia": "Endpoint principal da API FURIA",
    "/api/v1/furia/players/{identifier}":
      "Detalhes de um jogador específico por ID ou nome",
    "/api/v1/furia/team/roster": "Lista atual de jogadores da FURIA",
    "/api/v1/furia/team/coach": "Informações sobre o técnico da FURIA",
    "/api/v1/furia/team/ranking": "Ranking atual e histórico da FURIA",
    "/api/v1/furia/team/info": "Informações gerais sobre a equipe FURIA",
    "/api/v1/furia/team/news":
      "Notícias recentes sobre a FURIA (use /news?limit=X para especificar quantidade)",
    "/api/v1/furia/team/summary":
      "Resumo completo com informações da equipe FURIA",
    "/api/v1/furia/team/stats": "Estatísticas completas da FURIA",
    "/api/v1/furia/team/stats/overview":
      "Visão geral das estatísticas da FURIA",
    "/api/v1/furia/team/stats/maps": "Estatísticas da FURIA por mapas",
    "/api/v1/furia/team/stats/matches":
      "Histórico de partidas recentes da FURIA (use /matches?limit=X para especificar quantidade)",
  },
  endpoints: [
    {
      path: "/api/v1/furia/players/{identifier}",
      method: "GET",
      description: "Retorna informações detalhadas sobre um jogador específico",
      params: "identifier - ID numérico ou nome do jogador",
      response: "Dados do jogador, redes sociais e notícias recentes",
    },
    {
      path: "/api/v1/furia/team/roster",
      method: "GET",
      description: "Retorna a lista atual de jogadores da FURIA",
    },
    {
      path: "/api/v1/furia/team/coach",
      method: "GET",
      description: "Retorna informações sobre o técnico atual da FURIA",
    },
    {
      path: "/api/v1/furia/team/ranking",
      method: "GET",
      description: "Retorna o ranking atual e histórico recente da FURIA",
    },
    {
      path: "/api/v1/furia/team/info",
      method: "GET",
      description: "Retorna informações básicas sobre a equipe FURIA",
    },
    {
      path: "/api/v1/furia/team/news",
      method: "GET",
      description: "Retorna notícias recentes relacionadas à FURIA",
      query:
        "limit - Número máximo de notícias (padrão: 5, personalizável via ?limit=X)",
      example: "/api/v1/furia/team/news?limit=10",
    },
    {
      path: "/api/v1/furia/team/summary",
      method: "GET",
      description:
        "Retorna um resumo completo com todas as informações da equipe FURIA",
    },
    {
      path: "/api/v1/furia/stats",
      method: "GET",
      description: "Retorna todas as estatísticas completas da equipe FURIA",
    },
    {
      path: "/api/v1/furia/stats/overview",
      method: "GET",
      description: "Retorna uma visão geral das estatísticas da FURIA",
    },
    {
      path: "/api/v1/furia/stats/maps",
      method: "GET",
      description: "Retorna estatísticas da FURIA em cada mapa",
    },
    {
      path: "/api/v1/furia/stats/matches",
      method: "GET",
      description: "Retorna o histórico de partidas recentes da FURIA",
      query:
        "limit - Número máximo de partidas (padrão: 5, personalizável via ?limit=X)",
      example: "/api/v1/furia/stats/matches?limit=10",
    },
  ],
  author: "FURIA FanBot Team",
};
