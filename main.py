## Wir definieren eine Klasse, die eine Tabelle aus Tabellen darstellt, also
## einen Aktenschrank, der Aktenfächer enthält und die wiederum Akten enthalten

# Eine Akte ist ein flexibles Element, das eine Tabelle mit Columns enthält.
# Diese bekommt sie als Liste übergeben und macht daraus ein Dictionary mit
# Defaultwerten

class Akte():

    def __init__(self, *args):
        try:
            self.args = dict(*args)
            key = self.args.keys()
            items = self.args.items()
            for key,value in self.args.items():
                print(key, '--', value)
        except TypeError:
            pass
            # What to do if invalid parameters are passed

class Personenakte():
    reference_keys = ['Vorname', 'Nachname', 'Telefon']
    def __init__(self, *args):
        try:
            self.args = dict(*args)
            keys = self.args.keys()
            items = self.args.items()
        for key in keys:
            print(key)

        except TypeError:
            pass
            # What to do if invalid parameters are passed

## Aktentyp bestellen.

entry = {}
entry['Nachname'] = 'Mueller'
entry['Vorname'] = 'Mark'
entry['Telefon'] = '987656'

#print(entry)
#print(type(entry))
#exit(code=12)
Akte1 = Akte(entry)
print(Akte1.args)





