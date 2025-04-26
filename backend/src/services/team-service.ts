import { FullTeam, FullTeamPlayer, HLTV } from "hltv";
import { FullTeamStats } from "hltv/lib/endpoints/getTeamStats.js";
import { cache } from "../utils/cache.js";

const TEAM_ID = 8297;
const TEAM_CACHE_KEY = "full_team_data";
const TEAM_STATS_CACHE_KEY = "team_stats_data";

export async function getTeamData(): Promise<FullTeam> {
  const cached = cache.get(TEAM_CACHE_KEY);
  if (cached) {
    return cached as FullTeam;
  }

  const team = await HLTV.getTeam({ id: TEAM_ID });
  cache.set(TEAM_CACHE_KEY, team);
  return team;
}

export async function getTeamStats(): Promise<FullTeamStats> {
  const cached = cache.get(TEAM_STATS_CACHE_KEY);
  if (cached) {
    return cached as FullTeamStats;
  }

  const stats = await HLTV.getTeamStats({ id: TEAM_ID });
  cache.set(TEAM_STATS_CACHE_KEY, stats);
  return stats;
}

export async function getTeamCoach(): Promise<FullTeamPlayer | undefined> {
  const team = await getTeamData();
  return team.players.find((player) => player.type === "Coach");
}

export async function getTeamRanking() {
  const team = await getTeamData();
  return {
    actualRanking: team.rank,
    historyRanking: team.rankingDevelopment.slice(0, 5),
  };
}

export async function getTeamInfo() {
  const team = await getTeamData();
  return {
    id: team.id,
    name: team.name,
    logo: team.logo,
    country: team.country,
    instagram: team.instagram,
  };
}

export async function getTeamNews(limit: number = 5) {
  const team = await getTeamData();
  const news = team.news.slice(0, limit);

  return news.map((item) => ({
    ...item,
    link: "https://www.hltv.org" + item.link,
  }));
}

export async function getTeamMatches(limit: number = 5) {
  const teamStats = await getTeamStats();

  const recentMatches = teamStats.matches.slice(0, limit);

  return recentMatches.map((match) => ({
    date: new Date(match.date).toLocaleDateString("pt-BR"),
    opponent: match.team2.name,
    map: match.map.replace("de_", " ").trim(),
    score: `${match.result.team1}-${match.result.team2}`,
    eventName: match.event.name,
  }));
}

export async function getTeamSummary() {
  const team = await getTeamData();
  const teamStats = await getTeamStats();

  return {
    info: {
      id: team.id,
      name: team.name,
      logo: team.logo,
      instagram: team.instagram,
      country: team.country,
    },
    ranking: {
      current: team.rank,
      history: team.rankingDevelopment.slice(0, 5),
    },
    roster: [
      ...team.players
        .filter((player) => player.type !== "Coach")
        .map((player) => ({
          name: player.name,
          type: player.type,
        })),
    ],
    coach: {
      name: team.players.find((player) => player.type === "Coach")?.name,
    },
    stats: teamStats.overview,
    maps: Object.entries(teamStats.mapStats).map(([mapName, stats]) => ({
      name: mapName.replace("de_", " ").trim(),
      played: stats.wins + stats.draws + stats.losses,
      winRate: stats.winRate,
    })),
    achievements: teamStats.events.filter((event) => event.place == "1st"),
  };
}

export async function getTeamOverview() {
  const teamStats = await getTeamStats();
  return teamStats.overview;
}

export async function getTeamMaps() {
  const teamStats = await getTeamStats();
  return teamStats.mapStats;
}
