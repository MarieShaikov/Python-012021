#Kniha
#Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů.
# Vytvoř tedy třídu Book, která reprezentuje knihu. Každá kniha bude mít atributy title,
# pages a price. Hodnoty nastav ve funkci __init__.
#Přidej knize funkci getInfo, která vypíše informace o knize v nějakém pěkném formátu.
#Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou.
# Přidej funkci discount, která bude mít jeden parametr - velikost slevy v procentech.
# Funkce sníží cenu knihy o dané procento.

class Book:

    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_info(self):
        return f"{self.title} has {self.pages} pages and cost {self.price}."

    def discount(self, amount):
        self.price -= self.price * (amount/100)

#funkce pouze snizuje cenu

book = Book('Harry Potter', 350, 250)
print(book.get_info())
book.discount(50)
print(book.get_info())

