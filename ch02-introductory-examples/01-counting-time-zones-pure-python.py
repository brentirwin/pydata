# Chapter 2 examples

# Read Data and convert JSON to dictionary
import json
path = 'usagov_bitly.json'
records = [json.loads(line) for line in open(path)]
print(records)

# Counting Time Zones in Pure Python
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10])

# Create new dictionary with counts for each time zone
from collections import defaultdict
def get_counts(sequence):
  counts = defaultdict(int) # values will initalize to 0
  for x in sequence:
    counts[x] += 1
  return counts

# Get number of results in Eastern Time
counts = get_counts(time_zones)
print(counts['America/New_York'])
print(len(time_zones))

#Find the top 10 time zones and their counts
from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(10))