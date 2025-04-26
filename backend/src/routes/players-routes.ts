import { FastifyInstance, FastifyReply, FastifyRequest } from "fastify";
import { FullPlayer, HLTV } from "hltv";

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

        const isNumeric = /^\d+$/.test(identifier);

        let player: FullPlayer | null = null;
        if (isNumeric) {
          const playerId = parseInt(identifier);
          player = await HLTV.getPlayer({ id: playerId });
        } else {
          player = await HLTV.getPlayerByName({ name: identifier });

          if (!player) {
            return reply.status(404).send({ error: "Jogador não encontrado" });
          }
        }

        return reply.send({
          player: {
            playerId: player.id,
            name: player.name,
            image: player.image,
            age: player.age,
            rating: player.statistics?.rating,
            team: player.team,
            country: player.country,
          },
          socials: {
            instagram: player.instagram,
            twitter: player.twitter,
            twitch: player.twitch,
          },
          news: player.news.slice(0, 5).map((news) => {
            return {
              title: news.name,
              link: `https://www.hltv.org${news.link}`,
            };
          }),
        });
      } catch (error) {
        app.log.error(error);
        return reply
          .status(500)
          .send({ error: "Falha ao buscar informações do jogador" });
      }
    }
  );
}
