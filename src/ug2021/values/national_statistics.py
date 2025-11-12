import polars as pl

from ..data.results import national_long, national_wide
from ..utils import full_name

__all__ = (
    "registered_voters",
    "valid_votes",
    "invalid_votes",
    "total_votes",
    "turnout",
    "winner",
    "winner_votes",
    "winner_pct",
    "runner_up",
    "runner_up_votes",
    "runner_up_pct",
)


registered_voters: float = national_wide["registered"][0]
valid_votes: float = national_wide["valid"][0]
invalid_votes: float = national_wide["invalid"][0]
total_votes: float = national_wide["total"][0]
turnout: float = national_wide["turnout"][0]
winner: float = full_name(national_long.filter(pl.col("rank") == 1)["candidate"][0])
winner_votes: float = national_long.filter(pl.col("rank") == 1)["votes"][0]
winner_pct = (winner_votes / total_votes) * 100

runner_up: float = full_name(national_long.filter(pl.col("rank") == 2)["candidate"][0])
runner_up_votes: float = national_long.filter(pl.col("rank") == 2)["votes"][0]
runner_up_pct = (runner_up_votes / total_votes) * 100
