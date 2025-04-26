import { FastifyInstance, FastifyReply, FastifyRequest } from "fastify";
import {
  getTeamCoach,
  getTeamData,
  getTeamInfo,
  getTeamNews,
  getTeamRanking,
  getTeamSummary,
} from "../services/team-service.js";

export async function registerTeamRoutes(app: FastifyInstance) {
  app.get("/roster", async (_, reply: FastifyReply) => {
    try {
      const team = await getTeamData();
      const response = { players: team.players };

      return reply.send(response);
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team roster" });
    }
  });

  app.get("/coach", async (_, reply: FastifyReply) => {
    try {
      const teamCoach = await getTeamCoach();
      const response = { coach: teamCoach };

      return reply.send(response);
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team roster" });
    }
  });

  app.get("/ranking", async (_, reply: FastifyReply) => {
    try {
      const teamRanking = await getTeamRanking();

      const response = { ranking: teamRanking };

      return reply.send(response);
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/info", async (_, reply: FastifyReply) => {
    try {
      const teamInfo = await getTeamInfo();
      const response = { info: teamInfo };

      return reply.send(response);
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/news", async (request: FastifyRequest, reply: FastifyReply) => {
    const { limit = 5 } = request.query as { limit: number };

    try {
      const teamNews = await getTeamNews(limit);

      const response = { total: teamNews.length, news: teamNews };

      return reply.send(response);
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });

  app.get("/summary", async (_, reply: FastifyReply) => {
    try {
      const teamSummary = await getTeamSummary();

      const response = { summary: teamSummary };

      return reply.send(response);
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });
}
