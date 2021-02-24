import csv

if __name__ == "__main__":
    filename="yearseason"
    csvFile = open("../../../data/neo4j/"+filename+".csv", "r", encoding="utf-8")
    reader = csv.reader(csvFile)
    i = 0
    oneset = set()
    for item in reader:
        i = i + 1
        oneset.add(item[0])
    print(i)
    print(oneset.__len__())
