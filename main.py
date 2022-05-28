from persona import Persona
from persona_service import PersonaService


if __name__ == '__main__':
    personaService = PersonaService()
    personaService.load()
    print('Lista PERSONAS')
    print(personaService.findAll())
    persona = Persona()
    personaService.input(persona)
    personaService.add(persona)
    print('Persona INGRESADA')
    print(persona)
    print('Lista PERSONAS')
    print(personaService.findAll())
    persona = None
    while persona is None:
        documento = int(input('Documento a MODIFICAR: '))
        persona = personaService.findByDocumento(documento)
    print('Persona ENCONTRADA')
    print(persona)
    nueva_persona = Persona()
    personaService.input(nueva_persona, False)
    nueva_persona.documento = documento
    personaService.update(nueva_persona)
    persona = personaService.findByDocumento(documento)
    print('Persona MODIFICADA')
    print(persona)
    persona = Persona()
    print('Persona NUEVA')
    personaService.input(persona)
    personaService.add(persona)
    print('Lista PERSONAS')
    print(personaService.findAll())
    persona = None
    while persona is None:
        documento = int(input('Documento a ELIMINAR: '))
        persona = personaService.findByDocumento(documento)
    print('Persona ENCONTRADA')
    print(persona)
    personaService.delete(documento)
    print('Lista PERSONAS')
    print(personaService.findAll())
    personaService.flush()
