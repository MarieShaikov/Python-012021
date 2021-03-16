import pandas
nakupy = pandas.read_csv('../nakupy.csv')
print(nakupy.iloc[8:])
greeting = " Hi  George "
print(greeting.strip().replace("  "," "))

print(nakupy.head(3))
print(nakupy.tail(2))