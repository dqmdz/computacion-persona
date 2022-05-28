from persona import Persona
from persona_repository import PersonaRepository


class PersonaService:

    def __init__(self):
        self.repository = PersonaRepository()

    def input(self, persona: Persona, full=True):
        print('Ingresando PERSONA')
        if full:
            persona.documento = int(input('Ingrese Documento: '))
        persona.apellido = input('Ingrese Apellido: ')
        persona.nombre = input('Ingrese Nombre: ')

    def add(self, persona: Persona):
        self.repository.save(persona)

    def delete(self, documento: int):
        self.repository.delete(documento)

    def update(self, persona: Persona):
        self.repository.save(persona)

    def findByDocumento(self, documento: int):
        return self.repository.findByDocumento(documento)

    def findAll(self):
        return self.repository.findAll()

    def load(self):
        self.repository.loadFile()

    def flush(self):
        self.repository.writeFile()
