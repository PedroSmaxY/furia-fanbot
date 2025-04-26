import { FastifyInstance, FastifyReply, FastifyRequest } from "fastify";
import { FullTeamStats } from "hltv/lib/endpoints/getTeamStats.js";
import {
  getTeamMaps,
  getTeamMatches,
  getTeamOverview,
  getTeamStats,
} from "../services/team-service.js";

export async function registerStatsRoutes(app: FastifyInstance) {
  app.get("/", async (_, reply: FastifyReply) => {
    try {
      const teamStats: FullTeamStats = await getTeamStats();

      const response = { stats: teamStats };

      return reply.send(response);
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/overview", async (_, reply: FastifyReply) => {
    try {
      const teamOverview = await getTeamOverview();

      const response = { overview: teamOverview };

      return reply.send(response);
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/maps", async (_, reply: FastifyReply) => {
    try {
      const teamMapStats = await getTeamMaps();

      const response = { maps: teamMapStats };

      return reply.send(response);
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/matches", async (request: FastifyRequest, reply: FastifyReply) => {
    const { limit = 5 } = request.query as { limit: number };

    try {
      const teamMatches = await getTeamMatches(limit);

      const response = { total: teamMatches.length, matches: teamMatches };

      return reply.send(response);
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });
}
