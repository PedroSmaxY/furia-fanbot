from dataclasses import dataclass
from typing import List


@dataclass
class Country:
    name: str
    code: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data['name'],
            code=data['code']
        )


@dataclass
class TeamInfo:
    id: int
    name: str
    logo: str
    instagram: str
    country: Country

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            name=data['name'],
            logo=data['logo'],
            instagram=data['instagram'],
            country=Country.from_dict(data['country'])
        )


@dataclass
class Ranking:
    current: int
    history: List[int]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            current=data['current'],
            history=data['history']
        )


@dataclass
class SummaryRosterMember:
    name: str
    type: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data['name'],
            type=data['type'],
        )


@dataclass
class RosterMember:
    id: int
    name: str
    type: str
    maps_played: int
    time_on_team: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data['name'],
            type=data['type'],
            maps_played=data['mapsPlayed'],
            time_on_team=data['timeOnTeam'],
            id=data['id']
        )


@dataclass
class Roster:
    players: List[RosterMember]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            players=[RosterMember.from_dict(m) for m in data['players']]
        )


@dataclass
class Coach:
    name: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data['name']
        )


@dataclass
class Stats:
    mapsPlayed: int
    totalKills: int
    totalDeaths: int
    roundsPlayed: int
    kdRatio: float
    wins: int
    draws: int
    losses: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            mapsPlayed=data['mapsPlayed'],
            totalKills=data['totalKills'],
            totalDeaths=data['totalDeaths'],
            roundsPlayed=data['roundsPlayed'],
            kdRatio=data['kdRatio'],
            wins=data['wins'],
            draws=data['draws'],
            losses=data['losses']
        )


@dataclass
class MapStats:
    name: str
    played: int
    winRate: float

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data['name'],
            played=data['played'],
            winRate=data['winRate']
        )


@dataclass
class Event:
    id: int
    name: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            name=data['name']
        )


@dataclass
class Achievement:
    place: str
    event: Event

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            place=data['place'],
            event=Event.from_dict(data['event'])
        )


@dataclass
class Summary:
    info: TeamInfo
    ranking: Ranking
    roster: List[SummaryRosterMember]
    coach: Coach
    stats: Stats
    maps: List[MapStats]
    achievements: List[Achievement]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            info=TeamInfo.from_dict(data['summary']['info']),
            ranking=Ranking.from_dict(data['summary']['ranking']),
            roster=[SummaryRosterMember.from_dict(m) for m in data['summary']['roster']],
            coach=Coach.from_dict(data['summary']['coach']),
            stats=Stats.from_dict(data['summary']['stats']),
            maps=[MapStats.from_dict(m) for m in data['summary']['maps']],
            achievements=[Achievement.from_dict(a) for a in data['summary']['achievements']]
        )


@dataclass
class Match:
    date: str
    opponent: str
    map: str
    score: str
    eventName: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            date=data['date'],
            opponent=data['opponent'],
            map=data['map'],
            score=data['score'],
            eventName=data['eventName']
        )


@dataclass
class MatchesResponse:
    total: int
    matches: List[Match]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            total=data['total'],
            matches=data['matches']
        )
