from datetime import datetime, timedelta
datetime.now()

apolo_start = datetime(1969, 7,16,14,32)
print(apolo_start)
1969-07-16 14:32:00

apolo_start.isoformat()
'1969-07-16T14:32:00'

apolo_start.strftime("%d. %m. %Y, %H:%M")
'16. 07. 1969, 14:32'

#Cvičení

#1. Převod času
#V proměnné apolloStart máme uložený datum a čas startu Apolla 11. Vypiš datum na obrazovku ve formátu,
# na který jsou zvyklí Američané, tj. na první místo napiš měsíc, dále den a nakonec rok,
# jako oddělovače použij lomítka. Čas vypisovat nemusíš.

#2. Čas od startu
#Satelit Solar Orbiter, který má za cíl pozorování Slunce, odstartoval 10. února 2020 v 5:03.
# Ulož si hodnotu startu do proměnné.
#Který den v týdnu Solar Orbiter odstartoval?
#Spočítej, kolik času od jeho startu uplynulo.

#3. Doprava večeře
#Zákazník si objednal večeři na webu dovážkové služby 13. listopadu 2020 v 19:47.
# Víme, že převzetí objednávky restaurací v průměru trvá 8 minut a 35 sekund,
# příprava jídla trvá 30 minut a doprava jídla k zákazníkovi 25 minut a 30 sekund.
# Kdy očekáváme, že jídlo dorazí zákazníkovi?

#%d day
#%m month
#%Y year
#%H hour
#%M minute
#%S second

#1.

from datetime import datetime, timedelta
apolo_start = datetime(1969, 7, 16, 14, 32)
print(apolo_start.strftime('%m/%d/%y'))

#print(apolo_start.strftime('%m/%d/%y'))
#07/16/69

#2.

orbiter_start = datetime(2020, 2, 10, 5, 3)
print(orbiter_start.isoweekday())
cas_od_startu = datetime.now() - orbiter_start
print(type(cas_od_startu))
print(cas_od_startu)

#class 'datetime.timedelta'>
#386 days, 14:33:30.047789

#3.

cas_objednavky = datetime(2020, 11, 13, 19, 47)
prevzeti = timedelta(minutes=8, seconds=35)
priprava = timedelta(minutes=30)
doprava = timedelta(minutes=25, seconds=30)

print(cas_objednavky + prevzeti + priprava + doprava)

#print(cas_objednavky + prevzeti + priprava + doprava)
#2020-11-13 20:51:05