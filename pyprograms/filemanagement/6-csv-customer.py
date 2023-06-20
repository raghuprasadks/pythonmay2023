class Customer():
    def __init__(self, name, mobile, email, address, city, zipcode):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.address = address
        self.city = city
        self.zipcode = zipcode

    def info(self):
        return "Customer: name ", self.name, "Address:  ", self.address


customerList = []
c1 = Customer('raghu', 9845547471, 'prasadraghuks@gmail.com', '1094,MCECHS Layout', 'Bengaluru', 560077)
customerList.append(c1)

c2 = Customer('rudresh', 9845547472, 'prasadrudreshks@gmail.com', '1095,MCECHS Layout', 'Bengaluru', 560077)
customerList.append(c2)

c3 = Customer('girish', 9845547473, 'girish@gmail.com', '1096,MCECHS Layout', 'Bengaluru', 560077)
customerList.append(c3)

'''
create csv
'''
import csv

with open('customerData1.csv', mode='w',newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    headerdata = ["name", "mobile", "email", "address", "city", "zipcode"]

    writer.writerow(headerdata)
    for c in customerList:
        data = []
        data.append(c.name)
        data.append(c.mobile)
        data.append(c.email)
        data.append(c.address)
        data.append(c.city)
        data.append(c.zipcode)
        writer.writerow(data)

import csv

with open('customerData1.csv', 'rt') as f:
    data = csv.reader(f)
    for row in data:
        print(row)
