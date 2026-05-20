from dataclasses import dataclass

from model.artist import Artist


@dataclass
class Arco:
    artista1_id: Artist
    artista2_id: Artist


    def __post_init__(self):
        self.peso=None