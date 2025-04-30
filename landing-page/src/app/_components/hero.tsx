import { Button } from "@/components/ui/button";
import { HandWaving, TelegramLogo } from "@phosphor-icons/react/dist/ssr";
import { BotIcon, CalendarSync, ChartArea } from "lucide-react";
import FuriaLogo from "../../../public/furia-logo.png";
import Image from "next/image";
import Link from "next/link";

export function Hero() {
  return (
    <section className="bg-gradient-to-br from-black to-gray-900 text-white relative overflow-hidden">
      {/* Background decoration */}
      <div className="absolute inset-0 opacity-10">
        <div className="absolute top-20 left-10 w-72 h-72 rounded-full bg-blue-500 blur-3xl"></div>
        <div className="absolute bottom-20 right-10 w-72 h-72 rounded-full bg-red-500 blur-3xl"></div>
      </div>

      <div className="container mx-auto px-4 py-20 lg:py-32 flex flex-col gap-12 lg:flex-row items-center justify-between relative z-10">
        <article className="lg:w-1/2">
          <div className="flex flex-col items-center lg:items-start gap-8">
            <div>
              <span className="text-blue-400 font-semibold text-sm uppercase tracking-wider">
                FuriaGG Fan Community
              </span>
              <header className="text-3xl md:text-4xl lg:text-5xl font-bold mt-2 leading-tight">
                <h1>
                  Conheça o novo Bot de Telegram para os
                  <span className="text-blue-400">
                    {" "}
                    fans do time de CS da FuriaGG!
                  </span>
                </h1>
              </header>
            </div>

            <Image
              src={FuriaLogo}
              alt="Logo do time"
              className="opacity-80 w-52 h-52 lg:w-96 lg:h-96 lg:absolute lg:-z-10 lg:top-40 lg:left-20 lg:opacity-5"
              priority={true}
            />

            <p className="text-gray-300 lg:text-lg leading-relaxed">
              O bot é uma ferramenta que permite aos usuários interagir com o
              time de CS da FuriaGG de forma rápida e fácil. Com ele, você pode
              receber atualizações sobre jogos, resultados, estatísticas e muito
              mais, tudo diretamente no seu Telegram.
            </p>

            <Button
              asChild
              className="bg-blue-500 hover:bg-blue-600 w-fit transition-all duration-300 hover:scale-105 hover:shadow-lg hover:shadow-blue-500/30 text-lg py-6"
            >
              <Link
                href="https://t.me/furiacs2_pedrosmaxy_bot"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-center gap-3"
              >
                <BotIcon className="h-5 w-5" />
                <span>Iniciar Conversa</span>
                <TelegramLogo className="h-5 w-5" />
              </Link>
            </Button>
          </div>
        </article>

        <article className="lg:w-5/12 hidden lg:block">
          <div className="relative">
            <div className="absolute -inset-1 bg-gradient-to-r from-blue-600 to-red-600 rounded-2xl blur-md opacity-75"></div>
            <div className="relative bg-gray-900 p-6 rounded-xl shadow-2xl border border-gray-800">
              <div className="flex items-center justify-between mb-4 lg:h-14">
                <div className="flex items-center gap-2">
                  <BotIcon className="text-blue-400" />
                  <span className="font-medium">FuriaGG Bot</span>
                </div>
                <TelegramLogo className="text-blue-400" />
              </div>
              <div className="space-y-3">
                <div className="bg-gray-800 p-3 rounded-lg flex justify-between">
                  <p className="text-sm">
                    👋 Olá! Sou o Bot oficial da FuriaGG.
                  </p>
                  <HandWaving className=" text-gray-500 w-4 h-4" />
                </div>
                <div className="bg-gray-800 p-3 rounded-lg flex justify-between">
                  <p className="text-sm">
                    📊 Digite /resumo para ver estatísticas
                  </p>
                  <ChartArea className=" text-gray-500 w-4 h-4" />
                </div>
                <div className="bg-gray-800 p-3 rounded-lg flex justify-between">
                  <p className="text-sm">
                    🗓️ Digite /proximaspartidas para próximos jogos
                  </p>
                  <CalendarSync className=" text-gray-500 w-4 h-4" />
                </div>
              </div>
            </div>
          </div>
        </article>
      </div>
    </section>
  );
}
