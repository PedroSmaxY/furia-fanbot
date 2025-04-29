/** @type {import('next').NextConfig} */
const nextConfig = {
  ...(process.env.DEPLOYMENT_ENV === "docker" ? { output: "standalone" } : {}),
};

export default nextConfig;
