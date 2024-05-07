from dataclasses import dataclass
@dataclass
class Flight:
    id: int
    original_airport: int
    destination_airport: int
    distance: int