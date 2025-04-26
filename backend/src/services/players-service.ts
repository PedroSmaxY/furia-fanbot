import { FullPlayer, HLTV } from "hltv";
import { cache } from "../utils/cache.js";

const PLAYER_CACHE_TTL = 43200; /* 12 hours */

export async function getPlayerInfo(identifier: string) {
  const cacheKey = `player_${identifier}`;

  const cachedPlayer = cache.get(cacheKey);
  if (cachedPlayer) {
    return cachedPlayer;
  }

  let player: FullPlayer | null = null;

  if (/^\d+$/.test(identifier)) {
    const playerId = parseInt(identifier);
    player = await HLTV.getPlayer({ id: playerId });
  } else {
    player = await HLTV.getPlayerByName({ name: identifier });

    if (!player) {
      throw new Error("Jogador não encontrado");
    }
  }

  const response = formatPlayerData(player);

  cache.set(cacheKey, response, PLAYER_CACHE_TTL);

  return response;
}

function formatPlayerData(player: FullPlayer) {
  return {
    player: {
      playerId: player.id,
      name: player.name,
      image: player.image,
      age: player.age,
      rating: player.statistics?.rating,
      team: player.team,
      country: player.country,
    },
    socials: {
      instagram: player.instagram,
      twitter: player.twitter,
      twitch: player.twitch,
    },
    news: player.news.slice(0, 5).map((news) => {
      return {
        title: news.name,
        link: `https://www.hltv.org${news.link}`,
      };
    }),
  };
}
