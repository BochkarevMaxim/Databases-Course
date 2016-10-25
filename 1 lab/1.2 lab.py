import csv

searchingName = raw_input('What is records name you are looking for? ')
findId = []
try:
    with open('db.csv', 'rt') as inputFile:
         reader = csv.reader(inputFile, delimiter=',')
         for row in reader:
             if searchingName == row[4]: 
                 findId.append(row[0])
                 
except IOError:
    print 'Cannot open db.csv. Programm terminated.'

else:
    if len(findId) <> 0:
        print ('Record id: '+ ", ".join(findId))
    else:
        print 'There is no record that matches inputed name'  

