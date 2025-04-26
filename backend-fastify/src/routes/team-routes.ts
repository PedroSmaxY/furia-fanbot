import { FastifyInstance, FastifyReply, FastifyRequest } from "fastify";
import { FullTeam, FullTeamPlayer, HLTV } from "hltv";

const TEAM_ID = 8297;

export default async function registerTeamRoutes(app: FastifyInstance) {
  app.get("/roster", async (request, reply) => {
    try {
      const team: FullTeam = await HLTV.getTeam({ id: TEAM_ID });
      return reply.send({ players: team.players });
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team roster" });
    }
  });

  app.get("/coach", async (request, reply) => {
    try {
      const team: FullTeam = await HLTV.getTeam({ id: TEAM_ID });
      const coach = team.players.find(
        (player: FullTeamPlayer) => player.type === "Coach"
      );

      return reply.send({ coach: coach });
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/ranking", async (request, reply) => {
    try {
      const team: FullTeam = await HLTV.getTeam({ id: TEAM_ID });
      const rankingStats = {
        actualRanking: team.rank,
        historyRanking: team.rankingDevelopment.slice(0, 5),
      };

      return reply.send({ ranking: rankingStats });
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/info", async (request, reply) => {
    try {
      const team: FullTeam = await HLTV.getTeam({ id: TEAM_ID });
      const info = {
        id: team.id,
        name: team.name,
        logo: team.logo,
        country: team.country,
        instagram: team.instagram,
      };

      return reply.send({ info: info });
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/news", async (request: FastifyRequest, reply: FastifyReply) => {
    const { limit = 5 } = request.query as { limit: number };

    try {
      const team: FullTeam = await HLTV.getTeam({ id: TEAM_ID });
      const news = team.news.slice(0, limit);

      return reply.send({ news: news });
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });
}
