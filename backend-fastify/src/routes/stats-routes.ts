import { FastifyInstance, FastifyReply, FastifyRequest } from "fastify";
import { FullTeam, HLTV } from "hltv";
import { FullTeamStats } from "hltv/lib/endpoints/getTeamStats.js";

const TEAM_ID = 8297;

export async function registerStatsRoutes(app: FastifyInstance) {
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
    const { limit = 5 } = request.query as { limit: number };

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

  app.get("/summary", async (_, reply: FastifyReply) => {
    try {
      const teamStats: FullTeamStats = await HLTV.getTeamStats({
        id: TEAM_ID,
      });
      const teamInfos: FullTeam = await HLTV.getTeam({ id: TEAM_ID });

      const summary = {
        info: {
          id: teamInfos.id,
          name: teamInfos.name,
          logo: teamInfos.logo,
          instagram: teamInfos.instagram,
          country: teamInfos.country,
        },
        ranking: {
          current: teamInfos.rank,
          history: teamInfos.rankingDevelopment.slice(0, 5),
        },
        roster: [
          ...teamInfos.players
            .filter((player) => player.type !== "Coach")
            .map((player) => ({
              name: player.name,
              type: player.type,
            })),
        ],
        coach: {
          name: teamInfos.players.find((player) => player.type === "Coach")
            ?.name,
        },
        stats: teamStats.overview,
        maps: Object.entries(teamStats.mapStats).map(([mapName, stats]) => ({
          name: mapName.replace("de_", " ").trim(),
          played: stats.wins + stats.draws + stats.losses,
          winRate: stats.winRate,
        })),
        achievements: teamStats.events.filter((event) => event.place == "1st"),
      };

      return reply.send({ summary: summary });
    } catch (error) {
      app.log.error(error);
      return reply.status(500).send({ error: "Failed to fetch team matches" });
    }
  });
}
