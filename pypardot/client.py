import requests
from objects.lists import Lists
from objects.emails import Emails
from objects.prospects import Prospects
from objects.opportunities import Opportunities
from objects.accounts import Accounts
from objects.users import Users
from objects.visits import Visits
from objects.visitors import Visitors
from objects.visitoractivities import VisitorActivities

from errors import PardotAPIError

# Issue #1 (http://code.google.com/p/pybing/issues/detail?id=1)
# Python 2.6 has json built in, 2.5 needs simplejson
try:
    import json
except ImportError:
    import simplejson as json

BASE_URI = 'https://pi.pardot.com'


class PardotAPI():
    def __init__(self, email, password, user_key):
        self.email = email
        self.password = password
        self.user_key = user_key
        self.api_key = None
        self.lists = Lists(self)
        self.emails = Emails(self)
        self.prospects = Prospects(self)
        self.opportunities = Opportunities(self)
        self.accounts = Accounts(self)
        self.users = Users(self)
        self.visits = Visits(self)
        self.visitors = Visitors(self)
        self.visitorActivities = VisitorActivities(self)

    def post(self, object, path=None, params=None, retries=0):
        """
        Makes a POST request to the API. Checks for invalid requests that raise PardotAPIErrors. If the API key is
        invalid, one re-authentication request is made, in case the key has simply expired. If no errors are raised,
        returns either the JSON response, or if no JSON was returned, returns the HTTP response status code.
        """
        if params is None:
            params = {}
        params.update({'user_key': self.user_key, 'api_key': self.api_key, 'format': 'json'})
        try:
            self._check_auth(object=object)
            request = requests.post(self._full_path(object, path), params=params)
            response = self._check_response(request)
            return response
        except PardotAPIError, err:
            if err.message == 'Invalid API key or user key':
                response = self._handle_expired_api_key(err, retries, 'post', object, path, params)
                return response
            else:
                raise err

    def get(self, object, path=None, params=None, retries=0):
        """
        Makes a GET request to the API. Checks for invalid requests that raise PardotAPIErrors. If the API key is
        invalid, one re-authentication request is made, in case the key has simply expired. If no errors are raised,
        returns either the JSON response, or if no JSON was returned, returns the HTTP response status code.
        """
        if params is None:
            params = {}
        params.update({'user_key': self.user_key, 'api_key': self.api_key, 'format': 'json'})
        try:
            self._check_auth(object=object)
            request = requests.get(self._full_path(object, path), params=params)
            response = self._check_response(request)
            return response
        except PardotAPIError, err:
            if err.message == 'Invalid API key or user key':
                response = self._handle_expired_api_key(err, retries, 'get', object, path, params)
                return response
            else:
                raise err

    def _handle_expired_api_key(self, err, retries, method, object, path, params):
        """
        Tries to refresh an expired API key and re-issue the HTTP request. If the refresh has already been attempted,
        an error is raised.
        """
        if retries != 0:
            raise err
        self.api_key = None
        if self.authenticate():
            response = getattr(self, method)(object=object, path=path, params=params, retries=1)
            return response
        else:
            raise err

    @staticmethod
    def _full_path(object, path=None, version=3):
        """Builds the full path for the API request"""
        full = '{0}/api/{1}/version/{2}'.format(BASE_URI, object, version)
        if path:
            return full + '/{0}'.format(path)
        return full

    @staticmethod
    def _check_response(response):
        """
        Checks the HTTP response to see if it contains JSON. If it does, checks the JSON for error codes and messages.
        Raises PardotAPIError if an error was found. If no error was found, returns the JSON. If JSON was not found,
        returns the response status code.
        """
        if response.headers.get('content-type') == 'application/json':
            json = response.json()
            error = json.get('err')
            if error:
                raise PardotAPIError(json_response=json)
            return json
        else:
            return response.status_code

    def _check_auth(self, object):
        if object == 'login':
            return
        if self.api_key is None:
            self.authenticate()

    def authenticate(self):
        """
         Authenticates the user and sets the API key if successful. Returns True if authentication is successful,
         False if authentication fails.
        """
        try:
            auth = self.post('login', params={'email': self.email, 'password': self.password})
            self.api_key = auth.get('api_key')
            if self.api_key is not None:
                return True
            return False
        except PardotAPIError:
            return False





