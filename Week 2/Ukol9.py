#Maturita

#Uvažuj program, který bude pracovat s výsledky z maturitní zkoušky.
# každý student může mít jeden z následujících výsledků:

#"Prospěl s vyznamenáním", pokud je průměr jeho známek maximálně 1.5 a nemá žádnou trojku.
#"Neprospěl", pokud má alespoň jednu pětku.
#"Prospěl", pokud nemá vyznamenání a současně nedostal žádnou pětku.
#Přidej funkci ohodnot_studenta(), která bude mít jeden parametr, kterým je slovník se známkami studenta.
# Funkce rozhodne, zda student prospěl, prospěl s vyznamenáním nebo neprospěl podle výše
# popsaných kritérií.

def student_assessment(student):
  total = 0
  length = 0
  value = []
  for subject in student:
    if subject == "Jméno":
      continue
    total += student[subject]
    length += 1
    value.append(student[subject])

  average = total/length
  if (average <= 1.5) and (3 not in value):
    return "Passed with distinction"
  elif 5 in value:
    return "Not passed"
  elif (average > 1.5) and (5 not in value):
    return "Passed"



marks = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]

for student in marks:
  print(student["Jméno"], student_assessment(student))


# test:
#
# passed_with_distinction = {"Český jazyk": 1, "Anglický jazyk": 2, "Jméno": "Mirek Dušín", "Matematika": 1, "Biologie": 1, "Zeměpis": 1}
# not_passed = {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5}
# passed = {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3}
#
# print(student_assessment(passed_with_distinction), "passed with distinction")
# print(student_assessment(not_passed), "not passed")
# print(student_assessment(passed), "passed")



#Dále napiš cyklus, který projde seznam vysledky a pomocí funkce
# ohodnot_studenta() zjistí prospěch studenta. Následně pro
# každého studenta vypíše jeho jméno a informaci o tom, zda prospěl,
# neprospěl či prospěl s vyznamenáním.

#Výstup tvého programu by mohl vypadat např. takto:

#Mirek Dušín: Prospěl s vyznamenáním
#Jarka Metelka: Neprospěl
#Jindra Hojer: Prospěl
#Červenáček: Prospěl s vyznamenáním
#Rychlonožka: Prospěl