from dataclasses import dataclass


@dataclass
class Artist:
    ArtistId:int
    Name:str

    def __post_init__(self):
        self.popolarita = None

    def __hash__(self):
        return hash(self.ArtistId)
    def __eq__(self, other):
        return self.ArtistId == other.ArtistId

    def __str__(self):
        return self.Name

    def __lt__(self,other):
        return self.popolarita<other.popolarita