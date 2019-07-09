import csv
csvData = [['Person'], ['Peter'], ['Jasmine'], ['Sam']]
with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writecolumn(csvData)
csvFile.close()