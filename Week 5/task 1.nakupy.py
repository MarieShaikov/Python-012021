import pandas
nakupy = pandas.read_csv('nakupy.csv')
#print(nakupy.iloc[8:])
greeting = " Hi  George "
#print(greeting.strip().replace("  "," "))

#print(nakupy.head(3))
#print(nakupy.tail(n=2))

print(nakupy.iloc[:5, 0]) #calling first 5 rows for 0 columns which is the first variable!!! 0 column == 1.variable
print(nakupy.head(n=3)) #calling the first three rows for all variables
print(nakupy.iloc[:5, [0,3]]) #calling first 5 rows for vriables in columns between 0-3 position (number ID, name, money)

