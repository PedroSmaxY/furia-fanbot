import type { Metadata } from "next";
import localFont from "next/font/local";
import FuriaLogo from "../../public/furia-logo.png";
import "./globals.css";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "FURIA CS2 FANBOT | Acompanhe o Time da FURIA pelo Telegram",
  description:
    "Bot de Telegram não oficial para fãs do time FURIA CS2. Receba notificações de jogos, estatísticas de jogadores, resultados e notícias em tempo real.",
  keywords: [
    "FURIA",
    "CS2",
    "bot",
    "telegram",
    "esports",
    "counter-strike",
    "estatísticas",
    "notificações",
    "FURIA Esports",
  ],
  authors: [{ name: "FURIA CS2 FANBOT Team" }],
  creator: "github.com/PedroSmaxY",
  publisher: "FURIA CS2 FANBOT",
  formatDetection: {
    telephone: false,
  },
  openGraph: {
    title: "FURIA CS2 FANBOT | Bot de Telegram para Fãs",
    description:
      "Acompanhe jogos, estatísticas e notícias da FURIA CS2 diretamente pelo Telegram com o FURIA CS2 FANBOT.",
    url: "https://furiabot.com.br",
    siteName: "FURIA CS2 FANBOT",
    locale: "pt_BR",
    type: "website",
    images: [
      {
        url: FuriaLogo.src,
        width: FuriaLogo.width,
        height: FuriaLogo.height,
        alt: "Logo da FURIA Esports",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "FURIA CS2 FANBOT | Atualizações em tempo real",
    description:
      "Bot de Telegram para acompanhar jogos, estatísticas e notícias do time FURIA CS2.",
    images: [FuriaLogo.src],
  },
  robots: {
    index: true,
    follow: true,
  },
  viewport: {
    width: "device-width",
    initialScale: 1,
  },
  icons: {
    icon: [{ url: FuriaLogo.src }],
    apple: [{ url: FuriaLogo.src }],
  },
  manifest: "/site.webmanifest",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
