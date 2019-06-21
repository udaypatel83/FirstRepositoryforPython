import pandas
#import xlrd

#df = pandas.read_csv("C:\\Users\\uday.patel\\Downloads\\supermarkets.csv")
#print (df)

#dfj = pandas.read_json("C:\\Users\\uday.patel\\Downloads\\supermarkets.json")

#print (dfj)

#dfe = pandas.read_excel("C:\\Users\\uday.patel\\Downloads\\supermarkets.xlsx")

#print(dfe)


dfcsv = pandas.read_csv("C:\\Users\\uday.patel\\Downloads\\supermarkets-semi-colons.txt", sep= ";" )

#print (dfcsv)

#dfsc = pandas.read_csv("C:\\Users\\uday.patel\\Downloads\\supermarkets-commas.txt")

#print (dfsc)

print (dfcsv)
dfcsv= dfcsv.set_index("ID")

print (dfcsv.shape)

print(dfcsv.loc[:,])

print (dfcsv.T )

print (dfcsv.shape)