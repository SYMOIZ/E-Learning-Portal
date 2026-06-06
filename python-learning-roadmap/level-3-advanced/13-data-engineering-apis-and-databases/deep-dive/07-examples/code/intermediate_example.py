import csv
from io import StringIO

data = "name,score\nAda,95\nGrace,98\n"
reader = csv.DictReader(StringIO(data))
scores = {row["name"]: int(row["score"]) for row in reader}
print(scores)
