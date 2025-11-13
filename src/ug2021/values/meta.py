from ..data.results import stations_wide, polling_station_results
from datetime import date, datetime

__all__ = (
    "election_date",
    "last_updated",
    "data_source",
    "number_of_polling_stations",
    "number_of_polling_stations_received",
)


election_date: date = date(2021, 1, 14)
last_updated: datetime = date(2021, 1, 28)
data_source: str = "https://ec.or.ug/2021-general-elections"
number_of_polling_stations = len(polling_station_results)
number_of_polling_stations_received = len(stations_wide)
