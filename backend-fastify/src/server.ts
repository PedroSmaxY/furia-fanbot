import Fastify, { FastifyInstance } from "fastify";
import { registerRoutes } from "./routes/index.js";

const app: FastifyInstance = Fastify({
  logger: true,
});

await registerRoutes(app);

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
