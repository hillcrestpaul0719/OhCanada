import csv

with open('data.csv', 'r') as f:
    data = list(csv.reader(f))
    f.close()

# print(data)

label = [i[0] for i in data[1:]]
population = [float(i[1]) for i in data[1:]]
area = [float(i[2]) for i in data[1:]]

csvData = [['Province/Territory','Population density', 'Percent of population']] + [[label[i], round(population[i]/area[i], 2), round(population[i]/population[-1]*100, 2)] for i in range(0, len(label))]

with open('table.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()
