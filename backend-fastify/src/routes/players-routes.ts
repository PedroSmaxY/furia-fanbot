import { FastifyInstance, FastifyReply, FastifyRequest } from "fastify";
import { HLTV } from "hltv";

export async function registerPlayerRoutes(app: FastifyInstance) {
  app.get("/", async (request: FastifyRequest, reply: FastifyReply) => {
    try {
      const players = await HLTV.getPlayerRanking();
      return reply.send(players);
    } catch (error) {
      app.log.error(error);
      return reply
        .status(500)
        .send({ error: "Falha ao buscar ranking de jogadores" });
    }
  });

  app.get(
    "/:id",
    async (
      request: FastifyRequest<{
        Params: { id: string };
      }>,
      reply: FastifyReply
    ) => {
      try {
        const playerId = parseInt(request.params.id);
        const player = await HLTV.getPlayer({ id: playerId });
        return reply.send(player);
      } catch (error) {
        app.log.error(error);
        return reply
          .status(500)
          .send({ error: "Falha ao buscar informações do jogador" });
      }
    }
  );
}
