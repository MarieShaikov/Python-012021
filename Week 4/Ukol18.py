# Inverview
# Uvažuj následující třídu Kontakt, která slouží k evidenci všech kontaktů
# (např. zákazníků, zaměstnanců, uchazečů o práci atd.).

from datetime import date

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Applicant(Kontakt):
    def __init__(self, interview_date, jmeno, email):
        self.interview_date = interview_date
        self.interview_notes = ""
        super().__init__(jmeno, email)


    def save_notes(self, text, date):
        if date < self.interview_date:
            return "This is error"
        else:
            self.interview_notes += text
            return "The text has been saved"

x = Applicant(date(2021, 3, 21), "Marie", "m.@gmail.com")
y = x.save_notes("Ahoj, dej mi praci", date.today())
print(y)
print(x.interview_notes)

# Vytvoř třídu Uchazec, která bude dědit od třídy Kontakt a která reprezentuje uchazeče o
# práci. Uchazeč o práci bude mít navíc atribut datum_pohovoru a zapis_z_pohovoru.
# Datum pohovoru objekt získá z parametru a zápis z pohovoru je na začátku prázdný řetězec "".
#
# Dále přidej funkci uloz_zapis(), která bude mít jako parametr textový zápis pohovoru.
# Tato funkce ohlídá, zda uživatel omylem nezadává zápis k pohovoru, který ještě neproběhl.
# Na začátku funkce porovnej aktuální datum a datum pohovoru. Pokud podle data pohovor ještě neproběhl,
# vrať chybový text, který informuje uživatele o chybě. Pokud již podle data pohovor proběhl,
# ulož zápis a vrať text s informací, že zápis byl uložen.

