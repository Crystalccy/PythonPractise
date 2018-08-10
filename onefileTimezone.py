# -*- coding: utf-8 -*-
import json
# sys.path.append ("tiny_func")
from tiny_func import get_counts2

path = "pydata-book-2nd-edition/datasets/bitly_usagov/example.txt"
records = [json.loads(line) for line in open(path,encoding = "utf-8")]
time_zones = [rec["tz"] for rec in records if "tz" in rec]

tz_counts = get_counts2.count(time_zones)

print (tz_counts['America/New_York'] )
print (len(time_zones))

