from ..data.results import national_wide

__all__ = (
    "registered_voters",
    "valid_votes",
    "total_votes",
    "turnout",
)


registered_voters: float = national_wide["registered"][0]
valid_votes: float = national_wide["valid"][0]
total_votes: float = national_wide["total"][0]
turnout: float = national_wide["turnout"][0]
