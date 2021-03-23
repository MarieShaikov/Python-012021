import pandas
u202 = pandas.read_csv('u202.csv')
u203 = pandas.read_csv('u203.csv')
u302 = pandas.read_csv('u302.csv')

u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()

u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"

exam = pandas.concat([u202, u203, u302], ignore_index=True)
print(exam.head)

#exam.to_csv("Maturita.csv", index=False)