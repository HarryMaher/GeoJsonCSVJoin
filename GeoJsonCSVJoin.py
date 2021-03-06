#!/usr/bin/env python3

"""
A simple Python 3 tool to join csv data to geojson files
"""
import json


def join_csv_to_json(geojson_file, geojson_join_field, input_csv_dict, headers = True, pretty = False, outfile = "outfile.geojson"):
    """
    Ouput a geojson joined with csvs and print out a list of 
    errors for fields missing from CSV that didn't join.

    :geojson_file: Name of the geojson you're joining to. (String)
    :geojson_join_field: The unique id that the geojson shares with the CSVs ("join on"). (String)
    :csv_dict: A dictionary that contains key: value pairs conforming to this format:
        {"filename1.csv" : "csv_join_field1", "filename2.csv": "join_field2" ... etc}
        Note: the join_fields all have to have the same unique id as each other and as
        the geojson_join_field. (Dict of string key: value pairs)
    :headers: If the .csv files have headers. (Optional, bool, default = True)
    :pretty: pretty print the output. (Optional, bool, default = False)
    :outfile: The name of the resulting file. (String)
    """

    with open(geojson_file, "r") as geojson:
        geojson = json.load(geojson)
    
    csv_dicts = []
    
    for filename, join_value in input_csv_dict.items():
        with open(filename, "r") as csv:
            csv = csv.read().split("\n")
            
        headers = [x.strip() for x in csv[0].split(",")]
        idx = headers.index(join_value) # quotes around our join column
        if headers:
            csv = csv[1:-1] # skip the header and tail newline
        else:
            csv = csv[:-1]
        # this is the csv dictionary
        csv_dict = {}
        for line in csv:
            line_separated = line.split(",")
            # Make each of the unique id strings a key and 
            # the rest of the row a dictionary of k:v pairs.
            csv_dict[line_separated[idx].strip()] = {headers[i]:field.strip() for i, field in enumerate(line_separated) if i != idx}
        #put this dict in with the others
        csv_dicts.append(csv_dict)

    
    errors = []
    
    for i, feature in enumerate(geojson["features"]):
        this_prop_join_id = feature["properties"][geojson_join_field]
        
        properties_dict = {}
        properties_dict.update(feature["properties"])
        
        ## Maybe check to see if property already in dict
        ## if so then prepend w/ filename_?
        for csv_d in csv_dicts:
            try:
                properties_dict.update(csv_d[this_prop_join_id])
            except Exception as err:
                errors.append(err)
        geojson["features"][i]["properties"] = (properties_dict) 
    
    if pretty:
        geojson = json.dumps(geojson, separators=(', ', ': '), indent=4, sort_keys=True)
    else:
        geojson = json.dumps(geojson, separators=(',', ':')) # no space makes smaller file
        
    with open(outfile, "w+") as outfile:
        outfile.write(geojson)
    print("Join errors:")
    for error in errors:
        print(error)


#Eg:
#join_csv_to_json("KC_Precincts.geojson", "NAME", {"csv2016.csv": "Precinct"})

