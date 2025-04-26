import { FastifyInstance } from "fastify";
import { registerPlayerRoutes } from "./player-routes.js";
import registerTeamRoutes from "./team-routes.js";

export async function registerRoutes(app: FastifyInstance) {
  await app.register(registerPlayerRoutes, { prefix: "/players" });
  await app.register(registerTeamRoutes, { prefix: "/furia" });

  app.get("/", async (request, reply) => {
    return reply.send({ message: "Welcome to the HLTV API" });
  });
}
