import configparser
import requests



class FablabClient():
	"""Module Python pour interagir avec l'API du site de gestion du Fablab UTC en tant que Fablab_Client"""



	def __init__(self):
		config = configparser.ConfigParser()
		config.read('config/env.ini')
		self.key = config['FABLAB']['FABLAB_APP_KEY']
		self.url = config['FABLAB']['FABLAB_API_URL']


   
	def postLogin(self, data):
		"""Fonction pour envoyer à l'API du FablabUTC le badgeage d'un permanencier"""

		return self._apiCall(method='post', path='/studentbadge/badgeuse', data=data);



	def _apiCall(self, method, path, data=None, parameters = None):
		"""Fonction effecutant les appels API sur l'API du site de gestion du Fablab"""

		uri = self.url + path
		key = self.key

		response = requests.request(method=method, url=uri + '?key=' + key, data = data, params = parameters)

		return self._buildResponse(response)

	

	def _buildResponse(self, api_response):
		"""Fonction pour construire une réponse à une requête API"""

		response = {
			'data' : api_response.json(),
			'status' : api_response.status_code
		}

		return response
