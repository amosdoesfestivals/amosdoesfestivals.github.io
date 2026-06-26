import csv
import requests
import yaml

# URL of the published Google Sheet in CSV format
CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTocOAy6u-NbEM0Dv6KqtBV57AcHD8O6pISeVq8I-dYXldsyUcDPVGYkYtPgtRoNYxnKv_XOctINZph/pub?gid=0&single=true&output=csv'

# Fetch the CSV data
response = requests.get(CSV_URL)
response.raise_for_status()  # Ensure we got a successful response

response.encoding = 'utf-8'

# Define headers according to the order
headers = ['Rank', 'Name', 'Star', 'Rating', 'Producer', 'Location', 'Review', 'Start', 'End', 'URL']

# Convert CSV to a list of dictionaries
csv_data = response.text.splitlines()
reader = csv.DictReader(csv_data, fieldnames=headers)

yaml_data = []
for row in reader:
    yaml_data.append({
        'rank': int(row['Rank']),
        'name': row['Name'],
        'star': row['Star'],
        'rating': row['Rating'],
        'producer': row['Producer'],
        'location': row['Location'],
        'review': row['Review'],
        'start': row['Start'],
        'end': row['End'],
        'url': row['URL']
    })

# Write to a YAML file
with open('./_data/reviews2026.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml.dump(yaml_data, yaml_file, sort_keys=False, default_flow_style=False)

print("Data has been successfully converted to YAML and saved to reviews2026.yaml.")




