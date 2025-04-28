from dataclasses import dataclass
from typing import List, Optional, Dict, Any


@dataclass
class TeamPlayer:
    id: int
    active: bool
    name: str
    first_name: str
    last_name: str
    nationality: str
    birthday: str
    age: int
    image_url: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=int(data['id']),
            active=bool(data['active']),
            name=data['name'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            nationality=data['nationality'],
            birthday=data['birthday'],
            age=int(data['age']),
            image_url=data['image_url']
        )


@dataclass
class Team:
    @dataclass
    class CurrentVideoGame:
        id: int
        name: str
        slug: str

        @classmethod
        def from_dict(cls, data: dict):
            return cls(
                id=int(data['id']),
                name=data['name'],
                slug=data['slug']
            )

    id: int
    name: str
    location: str
    image_url: str
    players: List[TeamPlayer]
    acronym: str
    current_video_game: CurrentVideoGame

    @classmethod
    def from_dict(cls, data: dict):
        players = [TeamPlayer.from_dict(player) for player in data['players']]
        return cls(
            id=int(data['id']),
            name=data['name'],
            location=data['location'],
            image_url=data['image_url'],
            acronym=data['acronym'],
            players=players,
            current_video_game=cls.CurrentVideoGame.from_dict(data['current_videogame'])
        )


@dataclass
class PlayerDetail:
    @dataclass
    class PlayerCurrentVideoGame:
        id: int
        name: str
        slug: str

        @classmethod
        def from_dict(cls, data: dict):
            return cls(
                id=int(data['id']),
                name=data['name'],
                slug=data['slug']
            )

    @dataclass
    class PlayerCurrentTeam:
        id: int
        name: str
        location: str
        slug: str
        modified_at: str
        acronym: str
        image_url: str

        @classmethod
        def from_dict(cls, data: dict):
            return cls(
                id=int(data['id']),
                name=data['name'],
                location=data['location'],
                slug=data['slug'],
                modified_at=data['modified_at'],
                acronym=data['acronym'],
                image_url=data['image_url']
            )

    id: int
    name: str
    slug: str
    first_name: str
    last_name: str
    nationality: str
    image_url: str
    active: bool
    modified_at: str
    role: Optional[str]
    current_videogame: PlayerCurrentVideoGame
    current_team: PlayerCurrentTeam

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=int(data['id']),
            name=data['name'],
            slug=data['slug'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            nationality=data['nationality'],
            image_url=data['image_url'],
            active=data['active'],
            modified_at=data['modified_at'],
            role=data.get('role'),
            current_videogame=cls.PlayerCurrentVideoGame.from_dict(data['current_videogame']),
            current_team=cls.PlayerCurrentTeam.from_dict(data['current_team'])
        )


@dataclass
class Match:
    @dataclass
    class Stream:
        main: bool
        language: str
        embed_url: str
        official: bool
        raw_url: str

        @classmethod
        def from_dict(cls, data: dict):
            return cls(
                main=data.get('main', False),
                language=data.get('language', ''),
                embed_url=data.get('embed_url', ''),
                official=data.get('official', False),
                raw_url=data.get('raw_url', '')
            )

    @dataclass
    class Videogame:
        id: Optional[int] = None
        name: Optional[str] = None
        slug: Optional[str] = None

        @classmethod
        def from_dict(cls, data: dict):
            if not data:
                return cls()
            return cls(
                id=data.get('id'),
                name=data.get('name'),
                slug=data.get('slug')
            )

    @dataclass
    class TeamInfo:
        id: int
        name: str
        location: str
        slug: str
        modified_at: str
        acronym: str
        image_url: str

        @classmethod
        def from_dict(cls, data: dict):
            return cls(
                id=data.get('id'),
                name=data.get('name'),
                location=data.get('location'),
                slug=data.get('slug'),
                modified_at=data.get('modified_at'),
                acronym=data.get('acronym'),
                image_url=data.get('image_url')
            )

    @dataclass
    class Opponent:
        type: str
        opponent: Optional['Match.TeamInfo'] = None

        @classmethod
        def from_dict(cls, data: dict):
            opponent_data = data.get('opponent', {})
            return cls(
                type=data.get('type', ''),
                opponent=Match.TeamInfo.from_dict(opponent_data) if opponent_data else None
            )

    @dataclass
    class Game:
        id: int
        position: int
        status: str
        finished: bool
        match_id: int
        detailed_stats: bool
        forfeit: bool
        complete: bool
        length: Optional[int] = None
        begin_at: Optional[str] = None
        end_at: Optional[str] = None
        winner_type: Optional[str] = None
        winner: Optional[Dict[str, Any]] = None

        @classmethod
        def from_dict(cls, data: dict):
            if not data:
                return None
            return cls(
                id=data.get('id', 0),
                position=data.get('position', 0),
                status=data.get('status', ''),
                finished=data.get('finished', False),
                match_id=data.get('match_id', 0),
                detailed_stats=data.get('detailed_stats', False),
                forfeit=data.get('forfeit', False),
                complete=data.get('complete', False),
                length=data.get('length'),
                begin_at=data.get('begin_at'),
                end_at=data.get('end_at'),
                winner_type=data.get('winner_type'),
                winner=data.get('winner')
            )

    @dataclass
    class Tournament:
        id: int
        name: str
        slug: str
        begin_at: str
        end_at: str
        tier: str
        region: str
        type: str

        @classmethod
        def from_dict(cls, data: dict):
            return cls(
                id=data.get('id', 0),
                name=data.get('name', ''),
                slug=data.get('slug', ''),
                begin_at=data.get('begin_at', ''),
                end_at=data.get('end_at', ''),
                tier=data.get('tier', ''),
                region=data.get('region', ''),
                type=data.get('type', '')
            )

    @dataclass
    class League:
        id: int
        name: str
        slug: str
        image_url: str
        modified_at: str
        url: Optional[str] = None

        @classmethod
        def from_dict(cls, data: dict):
            return cls(
                id=data.get('id', 0),
                name=data.get('name', ''),
                slug=data.get('slug', ''),
                image_url=data.get('image_url', ''),
                modified_at=data.get('modified_at', ''),
                url=data.get('url')
            )

    @dataclass
    class Serie:
        id: int
        name: str
        slug: str
        year: int
        season: str
        begin_at: str
        end_at: str
        full_name: str

        @classmethod
        def from_dict(cls, data: dict):
            if not data:
                return None
            return cls(
                id=data.get('id', 0),
                name=data.get('name', ''),
                slug=data.get('slug', ''),
                year=data.get('year', 0),
                season=data.get('season', ''),
                begin_at=data.get('begin_at', ''),
                end_at=data.get('end_at', ''),
                full_name=data.get('full_name', '')
            )

    @dataclass
    class MatchResult:
        team_id: int
        score: int

        @classmethod
        def from_dict(cls, data: dict):
            return cls(
                team_id=data.get('team_id', 0),
                score=data.get('score', 0)
            )

    id: int
    name: str
    slug: str
    status: str
    begin_at: str
    scheduled_at: str
    modified_at: str
    match_type: str
    number_of_games: int
    forfeit: bool
    draw: bool
    streams_list: List[Stream]
    opponents: List[Opponent]
    results: List[MatchResult]
    games: List[Game]
    videogame: Videogame
    league: League
    tournament: Tournament
    serie: Optional[Serie] = None

    @classmethod
    def from_dict(cls, data: dict):
        opponents = [cls.Opponent.from_dict(o) for o in data.get('opponents', [])]
        results = [cls.MatchResult.from_dict(r) for r in data.get('results', [])]
        games = [cls.Game.from_dict(g) if g else None for g in data.get('games', [])]
        streams = [cls.Stream.from_dict(s) for s in data.get('streams_list', [])]

        videogame_data = data.get('videogame', {})
        league_data = data.get('league', {})
        tournament_data = data.get('tournament', {})
        serie_data = data.get('serie', {})

        videogame = cls.Videogame.from_dict(videogame_data)
        league = cls.League.from_dict(league_data)
        tournament = cls.Tournament.from_dict(tournament_data)
        serie = cls.Serie.from_dict(serie_data) if serie_data else None

        return cls(
            id=data.get('id', 0),
            name=data.get('name', ''),
            slug=data.get('slug', ''),
            status=data.get('status', ''),
            begin_at=data.get('begin_at', ''),
            scheduled_at=data.get('scheduled_at', ''),
            modified_at=data.get('modified_at', ''),
            match_type=data.get('match_type', ''),
            number_of_games=data.get('number_of_games', 0),
            forfeit=data.get('forfeit', False),
            draw=data.get('draw', False),
            videogame=videogame,
            league=league,
            tournament=tournament,
            serie=serie,
            opponents=opponents,
            results=results,
            games=games,
            streams_list=streams
        )


@dataclass
class MatchList:
    matches: List[Match]

    @classmethod
    def from_dict(cls, data: list):
        matches = [Match.from_dict(match_data) for match_data in data]
        return cls(matches=matches)
