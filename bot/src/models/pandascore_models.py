from dataclasses import dataclass
from typing import List


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
