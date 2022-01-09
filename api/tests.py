from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from api.models import *
import json

# Create your tests here.


# función para iniciar sesion y crear token
def test_login_user(self):
    response = self.client.post('/api/login/client/', {
        'email': 'chikara@test.com',
        'password': 'rc{4@qHjR>!b`yAV'
    },
        format='json'
    )
    result = json.loads(response.content)
    self.assertIn('token', result)
    self.access_token = result['token']
    return result['token']


# función encargada de verificar el uso de token
def test_token_incorrect(self, url):
    response = self.client.post(url)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserTestCase(TestCase):
    def setUp(self):
        user = User(
            email='chikara@test.com',
            first_name='Testing',
            last_name='Testing',
        )
        user.set_password('rc{4@qHjR>!b`yAV')
        user.save()
        self.client = APIClient()

    # test de registro de usuario
    def test_register_user(self):
        response = self.client.post(
            '/api/register/client/', {
                'email': 'testing@chikara.com',
                'password': 'rc{4@qHjR>!b`yAV',
                'password_confirmation': 'rc{4@qHjR>!b`yAV',
            },
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {'success': True})

    # test logout
    def test_logout_user(self):
        test_token_incorrect(self, '/api/logout/client/')
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + test_login_user(self))
        response = self.client.post('/api/logout/client/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestPokemon(TestCase):
    def setUp(self):
        # creacion de usuario
        user = User(
            email='chikara@test.com',
            first_name='Testing',
            last_name='Testing',
        )
        user.set_password('rc{4@qHjR>!b`yAV')
        user.save()
        self.client = APIClient()
        self.user = user
        # creacion de elemento
        element = Element(
            english='fire',
        )
        element.save()
        self.element = element
        # creacion de pokemon
        pokemon = Pokemon(
            name='Pikachu',
            id_element=element,
            image='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png',
            id_pokedex=25,
            description='Pikachu es un Pokémon de la segunda generación. Es un Pokémon de tipo eléctrico, y se caracteriza por ser rápido y agresivo.',
        )
        pokemon.save()
        self.pokemon = pokemon

    # test crear pokemon
    def test_create_pokemon(self):
        url = '/api/pokemon/create/'
        test_token_incorrect(self, url)
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + test_login_user(self))
        response = self.client.post(
            url, {
                'name': 'squirtle',
                'id_element': self.element.id,
                'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png',
                'id_pokedex': 7,
                'description': 'Squirtle es un Pokémon de la segunda generación. Es un Pokémon de tipo agua, y se caracteriza por ser rápido y agresivo.',
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # test lista de pokemon
    def test_get_pokemon(self):
        response = self.client.get('/api/pokemon/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test de pokemon por id
        response = self.client.get(
            '/api/pokemon/list/?id_element=' + str(self.element.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test de actualizacion  de pokemons
    def test_update_pokemon(self):
        url = '/api/pokemon/update/' + str(self.pokemon.id) + '/'
        test_token_incorrect(self, url)
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + test_login_user(self))
        response = self.client.put(
            url, {
                'name': 'raichu',
                'id_element': self.element.id,
                'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png',
                'id_pokedex': 26,
                'description': 'Raichu es un Pokémon de la segunda generación. Es un Pokémon de tipo eléctrico, y se caracteriza por ser rápido y agresivo.',
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test de elminacion de pokemon
    def test_delete_pokemon(self):
        url = '/api/pokemon/delete/' + str(self.pokemon.id) + '/'
        test_token_incorrect(self, url)
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + test_login_user(self))
        response = self.client.delete(
            url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
