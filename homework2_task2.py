from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        delta: timedelta = timedelta(days=1)

        for dates in self.dates:
            start_date: datetime = dates[0]
            end_date: datetime = dates[1]

            while end_date >= start_date:
                yield start_date
                start_date += delta


if __name__ == "__main__":
    m = Movie('sw', [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)
