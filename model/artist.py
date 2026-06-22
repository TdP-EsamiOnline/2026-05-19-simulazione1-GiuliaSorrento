from dataclasses import dataclass


@dataclass
class Artist:
    ArtistId:int
    Name:str

    def __post_init__(self):
        self.popolarita = 0

    def __hash__(self):
        return hash(self.ArtistId)
    def __eq__(self, other):
        return self.ArtistId == other.ArtistId

    def __str__(self):
        return self.Name

    def __lt__(self,other):  #ordinamento lt funziona solo se popolarita è un numero, quindi inizializza nel post_init la popolarità a 0
        return self.popolarita<other.popolarita