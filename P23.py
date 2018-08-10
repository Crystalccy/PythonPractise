# -*- coding: utf-8 -*-

import json

from pandas import DataFrame, Series
import pandas as pd; import numpy as np

path = "pydata-book-2nd-edition/datasets/bitly_usagov/example.txt"
records = [json.loads(line) for line in open(path,encoding = "utf-8")]
time_zones = [rec["tz"] for rec in records if "tz" in rec]

frame= DataFrame(records)
tz_counts = frame['tz'].value_counts()


clean_tz = frame['tz'].fillna("missing")
clean_tz[clean_tz == ''] = 'unknown'
tz_counts = clean_tz.value_counts()

results = Series([x.split()[0] for x in frame.a.dropna()])
print (results[:5])