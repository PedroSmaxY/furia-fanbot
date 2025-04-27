import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import {
  TelegramLogo,
  XLogo,
  TiktokLogo,
  FacebookLogo,
  TwitchLogo,
  YoutubeLogo,
} from "@phosphor-icons/react/dist/ssr";
import Link from "next/link";

export function Footer() {
  return (
    <footer className="bg-gradient-to-br from-black to-gray-900 text-white py-10 px-4 border-t border-gray-800">
      <div className="container mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Logo and description */}
          <div className="space-y-4">
            <h3 className="text-xl font-bold">
              <span className="text-blue-400">FURIA</span>
              <span className="text-gray-200"> CS2 FANBOT</span>
            </h3>
            <p className="text-sm text-gray-300">
              Acompanhe as últimas notícias, estatísticas e jogos da FURIA CS2
              diretamente pelo Telegram.
            </p>
            <Button
              variant="outline"
              className="gap-2 bg-transparent border-blue-500 text-blue-400 hover:bg-blue-600 hover:text-white transition-all duration-300"
              asChild
            >
              <a
                href="https://t.me/furiabot"
                target="_blank"
                rel="noopener noreferrer"
              >
                <TelegramLogo className="h-4 w-4" />
                Acessar Bot
              </a>
            </Button>
          </div>

          {/* Social media and contact */}
          <div className="flex flex-col items-start md:items-end justify-between">
            <div>
              <h4 className="font-medium mb-4 text-gray-100">Conecte-se</h4>
              <div className="flex space-x-4 mt-2">
                <Link
                  href="https://x.com/FURIA"
                  target="_blank"
                  className="hover:text-blue-400 transition-colors p-2 bg-gray-800 rounded-full hover:bg-gray-700"
                >
                  <XLogo className="h-5 w-5" />
                </Link>
                <Link
                  href="https://www.facebook.com/furiagg"
                  target="_blank"
                  className="hover:text-blue-400 transition-colors p-2 bg-gray-800 rounded-full hover:bg-gray-700"
                >
                  <FacebookLogo className="h-5 w-5" />
                </Link>
                <Link
                  href="https://www.tiktok.com/@furiagg"
                  target="_blank"
                  className="hover:text-blue-400 transition-colors p-2 bg-gray-800 rounded-full hover:bg-gray-700"
                >
                  <TiktokLogo className="h-5 w-5" />
                </Link>
                <Link
                  href="https://www.twitch.tv/furiatv"
                  target="_blank"
                  className="hover:text-blue-400 transition-colors p-2 bg-gray-800 rounded-full hover:bg-gray-700"
                >
                  <TwitchLogo className="h-5 w-5" />
                </Link>
                <Link
                  href="https://www.youtube.com/@FURIAgg"
                  target="_blank"
                  className="hover:text-blue-400 transition-colors p-2 bg-gray-800 rounded-full hover:bg-gray-700"
                >
                  <YoutubeLogo className="h-5 w-5" />
                </Link>
              </div>
            </div>
          </div>
        </div>

        <Separator className="my-6 bg-gradient-to-r from-blue-600/20 via-gray-700/20 to-red-600/20" />

        <div className="flex flex-col md:flex-row justify-between items-center text-xs text-gray-400">
          <p>
            © {new Date().getFullYear()} FURIA CS2 FANBOT. Todos os direitos
            reservados.
          </p>
          <p className="mt-2 md:mt-0">
            Projeto acadêmico não oficial. Não afiliado à FURIA Esports.
          </p>
        </div>
      </div>
    </footer>
  );
}
