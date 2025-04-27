import { Button } from "@/components/ui/button";
import { Hero } from "./_components/hero";
import { WhatsappLogo } from "@phosphor-icons/react/dist/ssr";

export default function Home() {
  return (
    <>
      <main>
        <Hero />
        <Button variant="default" className="">
          Botão <WhatsappLogo />
        </Button>
      </main>
    </>
  );
}
