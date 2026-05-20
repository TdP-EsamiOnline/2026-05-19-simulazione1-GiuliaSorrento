from dataclasses import dataclass


@dataclass
class Arco:
    artista1_id: int
    artista2_id: int
    peso: int