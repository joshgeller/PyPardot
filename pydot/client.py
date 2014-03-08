import requests
from objects.lists import Lists
from objects.emails import Emails
from objects.prospects import Prospects

from errors import PardotAPIError

# Issue #1 (http://code.google.com/p/pybing/issues/detail?id=1)
# Python 2.6 has json built in, 2.5 needs simplejson
try:
    import json
except ImportError:
    import simplejson as json

BASE_URI = 'https://pi.pardot.com'


class Client():
    def __init__(self, email, password, user_key):
        self.email = email
        self.password = password
        self.user_key = user_key
        self.api_key = None

        self.Lists = Lists(self)
        self.Emails = Emails(self)
        self.Prospects = Prospects(self)

    def _full_path(self, object, path=None, version='3'):
        """Builds the full path for the API request"""
        full = '{0}/api/{1}/version/{2}'.format(BASE_URI, object, version)
        if path:
            return full + '/{0}'.format(path)
        return full

    def _post(self, object, path=None, params={}):
        """
        Makes a POST request to the API. Checks for errors and returns the JSON response, if any.
        """
        params.update({'user_key': self.user_key, 'api_key': self.api_key, 'format': 'json'})
        try:
            #print('\n\nPOST parameters:\n\n{}'.format(params))
            request = requests.post(self._full_path(object, path), params=params)
            response = self._check_response(request.json())
            return response
        except PardotAPIError, err:
            print(err)


    def _get(self, object, path=None, params={}):
        """
        Makes a GET request to the API. Checks for errors and returns the JSON response, if any.
        """
        params.update({'user_key': self.user_key, 'api_key': self.api_key, 'format': 'json'})
        try:
            request = requests.get(self._full_path(object, path), params=params)
            response = self._check_response(request.json())
            return response
        except PardotAPIError, err:
            print(err)


    def _check_response(self, json_response):
        """
        Checks JSON response to see if there was an error. Raises PardotAPIError if an error was found.
        Returns the full JSON response.
        """
        for keys in json_response:
            error = json_response.get('err')
            if error:
                raise PardotAPIError(json_response)
        return json_response

    def authenticate(self):
        """
         Authenticates the user and sets the API key if successful.
         Returns True if authentication is successful, False if it isn't.
        """
        try:
            auth = self._post('login', params={'email': self.email, 'password': self.password})
            self.api_key = auth['api_key']
            return True
        except PardotAPIError, err:
            print(err)
            return False





