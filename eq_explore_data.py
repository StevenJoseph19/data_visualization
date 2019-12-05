import json

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    all_eq_dicts = all_eq_data['features']
    # readable_file = 'data/readable_eq_data.json'
    print(len(all_eq_dicts))

# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)