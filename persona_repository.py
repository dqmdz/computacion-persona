import csv
from persona import Persona


class PersonaRepository:
    def __init__(self):
        self.personas = {}

    def save(self, persona: Persona):
        self.personas[persona.documento] = persona

    def delete(self, documento: int):
        del self.personas[documento]

    def findByDocumento(self, documento: int):
        try:
            return self.personas[documento]
        except KeyError:
            print('Documento INEXISTENTE')
            return None

    def findAll(self):
        return [persona for persona in self.personas.values()]

    def loadFile(self):
        with open('data.txt', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                self.save(Persona(int(row[0]), row[1], row[2]))

    def writeFile(self):
        with open('data.txt', 'w') as f:
            for persona in self.personas.values():
                f.write(
                    f'{persona.documento},{persona.apellido},{persona.nombre}\n')
