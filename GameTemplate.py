from dataclasses import dataclass

@dataclass
class Game:
    name: str
    ageRating: int
    genre: str
    price: int
    stock: int
