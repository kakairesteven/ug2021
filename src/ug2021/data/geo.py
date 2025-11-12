from importlib.resources import files
import geopandas as gpd


__all__ = (
    "national",
    "regions",
    "subregions",
    "districts",
    "counties",
)


def _read(path):
    """
    Read geojson file from the resources
    """
    return  gpd.GeoDataFrame.from_file(
        files("ug2021._resources").joinpath(f"geo/{path}")
    )


national = _read("national.geojson")
regions = _read("regions.geojson")
subregions = _read("subregions.geojson")
districts = _read("districts.geojson")
counties = _read("counties.geojson")
