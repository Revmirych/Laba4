import csv
import json
 
File_Import = "import.csv"
File_Export = "export.json"
 
with open(File_Import, "r", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  for row in reader:
    rows = list(reader)

json_data = json.dumps(rows, ensure_ascii=False, indent=4)

with open(File_Export, 'w', encoding="utf-8") as f:
    f.write(json_data)