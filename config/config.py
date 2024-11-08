import json

import constants

geojson_data = {
    "type": "FeatureCollection",
    "features": [
        constants.start_point,
        constants.end_point,
        constants.restricted_zone_1,
        constants.restricted_zone_2,
        constants.restricted_zone_3,
    ],
}

with open("data/route_data.geojson", "w") as f:
    json.dump(geojson_data, f, indent=4)
