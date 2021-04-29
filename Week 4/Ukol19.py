# Instalace modulu
# Zopakuj si postup při instalaci modulu. Pojďme si vytvořit směnárnu, která nemá kurzy zadané pevně,
# ale umí si kurz měny stáhnout z internetu.
#
# V PyCharmu klikni na File -> Settings -> Project -> Python Interpreter.
# Následně klikni na tlačítko + (Install) a vyhledej modul forex-python.
# Dále klini na Install Package a potvrď instalaci.
#
# Dále se podívej na následující příklad, jak s modulem pracovat.
# Na prvním řádku je import, aby Python věděl, že s modulem chceme pracovat.
# Na druhém řádku vytvoříme objekt prevodnik (je to objekt třídy CurrencyRates), který se stará o převod měn.
#
# Uvažujme třeba, že chceme spočítat, kolik by nás stálo, pokud bychom chtěli 10 dolarů.
# Použijeme funkci convert(), která má jako první parametr zkraktu cílové měny,
# jako druhé parametr zkratku zdrojové měny a jako třetí parametr množství požadovaných dolarů.
# Funkce vypočte, kolik jednotek zdrojové měny je potřeba zaplatit, aby to odpovídalo požadovanému množství cílové měny.
#

from forex_python.converter import CurrencyRates
initial_currency = input("What is your initial currency?")
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("How much money you need in the desired currency?"))

final_currency = prevodnik.convert('USD', initial_currency, pozadovano_v_cilove_mene)
print(int(final_currency))


# Zkus program upravit tak, aby zjistil požadovanou měnu od uživatele (pomocí funkce input()).
# Uvažuj, zkus např. pracovat s měnami EUR, GBP nebo DKK. Následně od uživatele získej i
# požadované množství cílové měny. Nezapomeň toho množství převést na typ int.
#
from forex_python.bitcoin import BtcConverter
b = BtcConverter()
initial_currency = input("What is your initial currency?")
pozadovano_v_cilove_mene = int(input("How many Bitcoin do you want?"))

final_currency = b.convert_to_btc(pozadovano_v_cilove_mene, initial_currency)
print(final_currency)

# Pokročilejší varianta
# Podívej se do dokumentace k modulu forex-python. Zjistíš, že umí pár dalších zajímavých věcí,
# například převod měny do Bitcoinu. Zkus pomocí modulu vytvořit program,
# který se zeptá uživatele na měnu a požadovaný počet Bitcoinů a vrátí mu množství měny,
# které by potřeboval, aby požadované množství Bitcoinů mohl koupit.