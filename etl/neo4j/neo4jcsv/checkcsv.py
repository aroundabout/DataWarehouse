import csv


def create_csv(filename):
    path = filename
    with open(path, 'w') as f:
        csv_write = csv.writer(f)


def write_csv(c, filename):
    path = filename
    with open(path, 'a+', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        data_row = c
        csv_write.writerow(data_row)


if __name__ == "__main__":
    csvFile = open("../../../data/neo4j/actor.csv", "r", encoding="utf-8")
    reader = csv.reader(csvFile)
    filename = "actor.csv"
    create_csv(filename)
    oenset=set()
    for item in reader:
        if "\n" in item[0]:
            newActor = item[0].split("\n")
            for i in newActor:
                oenset.add(i)
        else:
            oenset.add(item[0])

    for item in oenset:
        content = item, "Actor"
        write_csv(content, filename)
    print(oenset.__len__())
