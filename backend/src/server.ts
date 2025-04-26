import Fastify, { FastifyInstance } from "fastify";
import { registerRoutes } from "./routes/index.js";
import { apiDocumentation } from "./docs/api-documentation.js";

const app: FastifyInstance = Fastify({
  logger: true,
});

app.get("/", async (request, reply) => {
  const baseUrl = `${request.protocol}://${request.hostname}:3000`;
  return reply.send({
    ...apiDocumentation,
    baseUrl: baseUrl,
  });
});

await app.register(registerRoutes, { prefix: "/api/v1/furia" });

const start = async () => {
  try {
    await app.listen({ port: 3000, host: "0.0.0.0" });
    console.log("Servidor rodando em http://localhost:3000");
  } catch (err) {
    app.log.error(err);
    process.exit(1);
  }
};

start();
