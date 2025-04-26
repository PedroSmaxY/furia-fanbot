import { FastifyInstance, FastifyReply, FastifyRequest } from "fastify";
import { HLTV } from "hltv";
import { FullTeamStats } from "hltv/lib/endpoints/getTeamStats.js";

const TEAM_ID = 8297;

export default async function registerStatsRoutes(app: FastifyInstance) {
  app.get("/", async (_, reply: FastifyReply) => {
    try {
      const teamStats: FullTeamStats = await HLTV.getTeamStats({
        id: TEAM_ID,
      });

      return reply.send({ stats: teamStats });
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/overview", async (_, reply: FastifyReply) => {
    try {
      const teamStats: FullTeamStats = await HLTV.getTeamStats({
        id: TEAM_ID,
      });

      return reply.send({ overview: teamStats.overview });
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/maps", async (_, reply: FastifyReply) => {
    try {
      const teamStats: FullTeamStats = await HLTV.getTeamStats({
        id: TEAM_ID,
      });

      return reply.send({ stats: teamStats.mapStats });
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/matches", async (request: FastifyRequest, reply: FastifyReply) => {
    const limit = Number((request.query as any).limit) || 5;

    try {
      const teamStats: FullTeamStats = await HLTV.getTeamStats({
        id: TEAM_ID,
      });
      const recent = teamStats.matches.slice(0, limit);

      const formattedMatches = recent.map((match) => ({
        date: new Date(match.date).toLocaleDateString("pt-BR"),
        opponent: match.team2.name,
        map: match.map.replace("de_", " ").trim(),
        score: `${match.result.team1}-${match.result.team2}`,
        eventName: match.event.name,
      }));

      return reply.send({
        total: formattedMatches.length,
        matches: formattedMatches,
      });
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });
}
