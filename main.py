import pandas
from matplotlib import pyplot as plt
if __name__ == '__main__':
    csv = pandas.read_csv("charts.csv")
    print(csv)