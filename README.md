# GeoJsonCSVJoin
Takes a geojson, csv(s), and joins csv(s) to geojson based off a common unique id (eg: zip code, GISJOIN, election precinct number, census block number, etc. etc.) Prints missed joins.


How to use:

Download or clone this repo and copy GeoJsonCSVJoin.py into your project directory.
Use it like this:

```
from GeoJsonCSVJoin import join_csv_to_json


geo_file_1 = "geojsonfile.geojson"
geo_join_field = "Election_precinct_number"
csv_file_1 = "my_csv1.csv"
csv_join_field1 = "Precinct"


"""
*Input:*
geojson_file: Name of the geojson you're joining to. (String)
geojson_join_field: The unique id that the geojson shares with the CSVs ("join on"). (String)
csv_dict: A dictionary that contains key: value pairs conforming to this format:
    {"filename1.csv" : "csv_join_field1", "filename2.csv": "join_field2" ... etc}
    Note: the join_fields all have to have the same unique id as each other and as
    the geojson_join_field. (Dict of string key: value pairs)
headers: If the .csv files have headers. (Optional, bool, default = True)
pretty: pretty print the output. (Optional, bool, default = False)
outfile: The name of the resulting file. (String)
"""


join_csv_to_json(geojson_file = geo_file_1, geojson_join_field = geo_join_field, input_csv_dict = {csv_file_1: csv_join_field1}, headers = True, pretty = False, outfile = "outfile.geojson")


# Alternatively, you can join with mutiple csvs at once, like so:

join_csv_to_json(geojson_file = geo_file_1, geojson_join_field = geo_join_field, input_csv_dict = {csv_file_1: csv_file_1, "another_csv_file.csv": "join_field"}, pretty = False, outfile = "outfile.geojson")

```