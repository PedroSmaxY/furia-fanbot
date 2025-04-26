import { FastifyInstance, FastifyReply, FastifyRequest } from "fastify";
import { getPlayerInfo } from "../services/players-service.js";

type PlayerParams = {
  identifier: string;
};

export async function registerPlayerRoutes(app: FastifyInstance) {
  app.get(
    "/:identifier",
    async (
      request: FastifyRequest<{ Params: PlayerParams }>,
      reply: FastifyReply
    ) => {
      try {
        const identifier = request.params.identifier;
        const playerData = await getPlayerInfo(identifier);

        return reply.send(playerData);
      } catch (error) {
        app.log.error(error);
        if (error instanceof Error) {
          if (error.message === "Jogador não encontrado") {
            return reply.status(404).send({ error: "Jogador não encontrado" });
          }
        }

        return reply
          .status(500)
          .send({ error: "Falha ao buscar informações do jogador" });
      }
    }
  );
}
