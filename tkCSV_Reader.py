import csv

csvFile = './28daysoftypeCooker.csv'

def csv_to_dict(filename, start_row=4,encoding='utf-8'):
    data_dict = {}
    with open(filename, 'r', encoding=encoding) as file:
        csv_reader = csv.reader(file)
        for _ in range(start_row - 1):  # Skip rows before start_row
            next(csv_reader)
        headers = next(csv_reader)  # Get headers from start_row
        for row in csv_reader:
            key = row[0]  # Assuming the first column is the key
            data_dict[key] = {headers[i]: row[i] for i in range(0, len(row))}
    return data_dict


csvDict = csv_to_dict(csvFile)
#print(csvDict["A"].keys())