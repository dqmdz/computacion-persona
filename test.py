import unittest
from unittest.mock import patch

from persona import Persona


class TestPersona(unittest.TestCase):

    def test_default(self):
        persona = Persona()
        self.assertEqual(persona.__dict__, {
                         'documento': 1, 'apellido': 'Torvalds', 'nombre': 'Linus'})

    # @patch('builtins.input', side_effect=[3, 'Bezos', 'Jeff'])
    # def test_input(self, mock_inputs):
    #     persona = Persona()
    #     persona.input()
    #     self.assertEqual(persona.__dict__, {
    #                      'documento': 3, 'apellido': 'Bezos', 'nombre': 'Jeff'})


if __name__ == '__main__':
    unittest.main()
