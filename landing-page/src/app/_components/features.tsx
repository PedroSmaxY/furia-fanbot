import { Card } from "@/components/ui/card";
import {
  ChartBar,
  CalendarCheck,
  Bell,
  Trophy,
  Newspaper,
  Robot,
} from "@phosphor-icons/react/dist/ssr";

export function Features() {
  const features = [
    {
      icon: <ChartBar className="h-10 w-10 text-blue-400" />,
      title: "Estatísticas Detalhadas",
      description:
        "Acesse estatísticas dos jogadores e da equipe FURIA CS2 com um simples comando.",
      command: "/resumo",
    },
    {
      icon: <Trophy className="h-10 w-10 text-blue-400" />,
      title: "Últimos Resultados",
      description:
        "Veja os resultados mais recentes das partidas da FURIA CS2.",
      command: "/partidas",
    },
    {
      icon: <CalendarCheck className="h-10 w-10 text-blue-400" />,
      title: "Calendário de Partidas",
      description:
        "Fique por dentro de todas as próximas partidas e torneios da FURIA CS2.",
      command: "/proximaspartidas",
    },
    {
      icon: <Bell className="h-10 w-10 text-blue-400" />,
      title: "Notificações em Tempo Real",
      description:
        "Receba alertas sobre início de partidas, resultados e momentos importantes.",
      command: "/notificacoes",
    },
    {
      icon: <Newspaper className="h-10 w-10 text-blue-400" />,
      title: "Notícias Exclusivas",
      description:
        "Fique por dentro das últimas notícias sobre a equipe da FURIA CS2.",
      command: "/news",
    },
    {
      icon: <Robot className="h-10 w-10 text-blue-400" />,
      title: "Interação Direta",
      description:
        "Converse com o bot e obtenha informações customizadas sobre a FURIA.",
      command: "/start",
    },
  ];

  return (
    <section id="recursos" className="py-20 bg-black text-white">
      <div className="container mx-auto px-4">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            Recursos do <span className="text-blue-400">FURIA CS2 FANBOT</span>
          </h2>
          <p className="text-gray-300">
            Nosso bot oferece diversas funcionalidades para você acompanhar o
            desempenho da FURIA de perto. Confira o que você pode fazer com
            apenas alguns comandos:
          </p>
        </div>

        {/* Background decoration */}
        <div className="absolute inset-0 pointer-events-none opacity-10">
          <div className="absolute top-1/4 left-1/4 w-72 h-72 rounded-full bg-blue-500 blur-3xl"></div>
          <div className="absolute bottom-1/4 right-1/4 w-72 h-72 rounded-full bg-red-500 blur-3xl"></div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <Card
              key={index}
              className="bg-gradient-to-br from-gray-900 to-gray-800 border-gray-700 p-6 rounded-xl hover:shadow-lg hover:shadow-blue-500/10 transition-all duration-300"
            >
              <div className="flex flex-col gap-4">
                <div className="bg-gray-800 p-3 rounded-lg w-fit">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold text-white">
                  {feature.title}
                </h3>
                <p className="text-gray-300">{feature.description}</p>
                <div className="mt-2 bg-gray-800/50 px-3 py-1.5 rounded-lg w-fit text-sm font-mono text-blue-400">
                  {feature.command}
                </div>
              </div>
            </Card>
          ))}
        </div>

        <div className="mt-16 text-center">
          <div className="inline-block relative">
            <div className="absolute -inset-1 bg-gradient-to-r from-blue-600 to-red-600 rounded-xl blur-md opacity-75"></div>
            <div className="relative bg-gray-900 px-6 py-4 rounded-lg border border-gray-700">
              <p className="text-lg">
                <span className="text-gray-300">Digite </span>
                <span className="font-mono text-blue-400 font-semibold">
                  /start
                </span>
                <span className="text-gray-300">
                  {" "}
                  a qualquer momento para ver todos os comandos disponíveis!
                </span>
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
