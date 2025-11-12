from importlib.resources import files

import polars as pl
from mizani.palettes import gradient_n_pal

# red_green_pal = gradient_n_pal(["#FF0100", "#29850E"])
red_green_pal = gradient_n_pal(["#999999", "#29850E"])


def red_green_pal_pct(value: float) -> list[str]:
    return red_green_pal(value / 100)


_lookup = {
    "Amuriat": "Patrick Oboi Amuriat",
    "Kabuleta": "Joseph Kiza Kabuleta",
    "Kalembe": "Nancy Linda Kalembe",
    "Katumba": "John Katumba",
    "Kyagulanyi": "Robert Ssentamu Kyagulanyi",
    "Mao": "Norbert Mao",
    "Mayambala": "Willy Mayambala",
    "Muntu": "Gregg Mugisha Muntu",
    "Mwesigye": "Fred Mwesigye",
    "Tumukunde": "Henry Kakurugu Tumukunde",
    "Museveni": "Yoweri Museveni Tibuhaburwa Kuguta",
}


def full_name(name: str) -> str:
    """
    Return the full name of the candidate
    """
    return _lookup[name]


def read_parquet(filename: str) -> pl.DataFrame:
    """
    Read parquet file from the package resources
    """
    return pl.read_parquet(files("ug2021._resources").joinpath(filename))



