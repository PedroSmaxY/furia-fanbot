import { FastifyInstance } from "fastify";
import { registerPlayerRoutes } from "./players-routes.js";
import { registerTeamStatsRoutes } from "./team-stats-routes.js";
import { registerTeamRoutes } from "./team-routes.js";
import { apiDocumentation } from "../docs/api-documentation.js";

export async function registerRoutes(app: FastifyInstance) {
  await app.register(registerPlayerRoutes, { prefix: "/players" });
  await app.register(registerTeamRoutes, { prefix: "/team" });
  await app.register(registerTeamStatsRoutes, { prefix: "/team/stats" });

  app.get("/", async (request, reply) => {
    const baseUrl = `${request.protocol}://${request.hostname}`;
    return reply.send({
      ...apiDocumentation,
      baseUrl: baseUrl,
    });
  });
}
