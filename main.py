#
# import pandas
# from matplotlib import pyplot as plt
# df = pandas.read_csv("charts.csv")
#
#
#
#
# titles = df.groupby('title').count()
# max_rank = titles["rank"].max()
# min_rank = titles["rank"].min()
# print(f"{max_rank}\n")
# print(min_rank.min())
#
#
#
# print(f"Most popular ->\n{titles[titles['rank'] == max_rank]}\n\n")
# print(f"Lest popular ->\n{titles[titles['rank'] == min_rank]}\n\n")
#
#
#
# print(df.groupby('artist').max('rank'))
#
#
# test = df[df['artist'] == "System Of A Down"]
# test.groupby('date').min('rank')[['rank']].plot()


import csv
with open("charts.csv", encoding="utf8") as f:
    csvreader = csv.reader(f)
    title_occurrences = dict()
    for row in csvreader:
        if (row[0] not in title_occurrences) and row[0] != "title":
            title_occurrences[row[0]] = 1
        else:
            if row[0] != "title":
                title_occurrences[row[0]] += 1
    max_value = 0
    max_key, min_key = ('','')
    for key, item in title_occurrences.items():
            if item > max_value:
                max_key = key
                max_value = title_occurrences[max_key]
    min_value = max_value
    for key, item in title_occurrences.items():
            if item < min_value:
                min_key = key
                min_value = title_occurrences[min_key]
    print(f"lowest amount if occ -> {min_key} -> {min_value}\n")
    print(f"highest amount if occ -> {max_key} -> {max_value}\n")