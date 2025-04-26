import { FastifyInstance } from "fastify";
import { registerPlayerRoutes } from "./player-routes.js";

export async function registerRoutes(app: FastifyInstance) {
  await registerPlayerRoutes(app);
}
