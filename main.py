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

    reference_dict = {'Vorname':'', 'Nachname':'', 'Telefon':'', 'E-Mail':'', 'Straße':'', 'Hausnummer':'', 'PLZ':'', 'Ort':''}

    def __init__(self, *args):
        try:
            self.args = dict(*args)
            in_keys = self.args.keys()
            in_items = self.args.items()
            for key,value in self.reference_dict.items():
                if key in in_keys:
                    self.reference_dict[key] = self.args[key]
                else:
                    print("Hae?")

        except TypeError:
            pass
            # What to do if invalid parameters are passed

    def print(self):

        for key, value in self.reference_dict.items():
            print(key, ' : ', value)

    def midiprint(self):
        for key, value in self.reference_dict.items():
            if not value:
                pass
            else:
                print(key, ' - ', value)

class Visitenkarte(Personenakte):

    print(Personenakte.reference_dict['Vorname'])
    exit(code=9)
    vk_dict = {'fullName': '', 'Postal' : '', 'Kontakt' : ''}
    vk_dict['fullName'] = Personenakte.reference_dict['Vorname'] + ' ' + Personenakte.reference_dict['Nachname']
    vk_dict['Postal'] = Personenakte.reference_dict['Straße'] + ' ' + Personenakte.reference_dict['Hausnummer'] + ' ' + \
                        Personenakte.reference_dict['PLZ'] + Personenakte.reference_dict['Ort']
    vk_dict['Kontakt'] = Personenakte.reference_dict['Telefon'] + ' ' + Personenakte.reference_dict['E-Mail']

    print(vk_dict)

    def midiprint(self):
        for key, value in self.vk_dict.items():
            print(key, ' : ', value)
## Aktentyp bestellen.

entry = {}
entry['Nachname'] = 'Mueller'
entry['Vorname'] = 'Mark'
entry['Telefon'] = '987656'

#print(entry)
#print(type(entry))
#exit(code=12)
Akte1 = Personenakte(entry)
#print(Akte1.reference_dict)
#Akte1.print()
#print("================")
#Akte1.midiprint()

vk = Visitenkarte(Akte1)

vk.midiprint()


