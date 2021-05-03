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

exam = pandas.concat([u202], ignore_index=True)
print(exam.head)

exam.to_csv("Maturita.csv", index=False)

#join the above tables with new table studenti,
# default merge of table in pandas is "inner join", other types are: outer join, left join, right join

students = pandas.read_csv('studenti.csv')

merged_tables = pandas.merge(exam, students, how="left")

#print(u202.shape)

teachers = pandas.read_csv('predsedajici.csv')
merged_tables_teachers = pandas.merge(merged_tables, teachers, on=["den"])
print(merged_tables_teachers.head)

print(exam.groupby('predmet')['znamka'].mean())

print(exam.groupby('predmet')['znamka'].max())


nakupy = pandas.read_csv('../Week 5/nakupy.csv')
print(nakupy.groupby('Jméno').sum())