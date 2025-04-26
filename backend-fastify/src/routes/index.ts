import { FastifyInstance } from "fastify";
import { registerPlayerRoutes } from "./players-routes.js";
import { registerStatsRoutes } from "./stats-routes.js";
import { registerTeamRoutes } from "./team-routes.js";

export async function registerRoutes(app: FastifyInstance) {
  await app.register(registerPlayerRoutes, { prefix: "/players" });
  await app.register(registerStatsRoutes, { prefix: "/stats" });
  await app.register(registerTeamRoutes, { prefix: "/team" });

  app.get("/", async (request, reply) => {
    return reply.send({ message: "Welcome to the HLTV API" });
  });
}
