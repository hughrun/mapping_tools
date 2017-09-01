import csv
import json

# files to merge
geojson_file = 'example.geojson'
csv_file = 'example.csv'
# fields to match on
geojson_match = 'SA1_7DIG16'
csv_match = 'sa1'

# fields to add
# ------------
# new property names
key1 = 'COFFEE'
# key2 = ''
# key3 = ''
# name of each row in csv where corresponding value is stored
value1 = 'coffee'
# value2 = ''
# value3 = ''

# open the geojson file
file = open(geojson_file, 'r')
# read the file and then load the json so it's a dict
json_data = json.loads(file.read())

# for each geojson feature, if a field in the json matches a field in the csv, add new properties to the json
for feature in json_data['features']:
  with open(csv_file, newline='') as f:
    # use DictReader so we can use the header names
    reader = csv.DictReader(f)
    for row in reader:
      # look for match
      if row[csv_match] == feature['properties'][geojson_match]:
        # create new property in geojson
        feature['properties'][key1] = row[value1]
        # feature['properties'][key2] = row[value2]
        # feature['properties'][key3] = row[value3]

# write out new geojson file with the updates
with open('new_file.geojson', 'w') as newfile:
  json.dump(json_data, newfile, indent=2)

        