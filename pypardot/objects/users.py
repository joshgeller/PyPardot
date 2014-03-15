class Users():
    """
    A class to query and use Pardot users.
    User field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#user
    """

    def __init__(self, client):
        self.client = client

    def query(self, **kwargs):
        """
        Returns the users matching the specified criteria parameters.
        Supported search parameters: http://http://developer.pardot.com/kb/api-version-3/querying-users#supported-search-criteria
        """
        result = self._get(path='/do/query', params=kwargs)
        return result.get('result')

    def read_by_id(self, id=None, **kwargs):
        """
        Returns the data for the user specified by <id>. <id> is the Pardot ID of the target user."""
        kwargs['id'] = id
        result = self._post(path='/do/read/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def read_by_email(self, email=None, **kwargs):
        """
        Returns the data for the user specified by <email>. <email> is the email address of the target user."""
        kwargs['email'] = email
        result = self._post(path='/do/read/email/{email}'.format(email=kwargs.get('email')), params=kwargs)
        return result

    def _get(self, object='user', path=None, params=None):
        """GET requests for the User object."""
        if params is None:
            params = {}
        result = self.client.get(object=object, path=path, params=params)
        return result

    def _post(self, object='user', path=None, params=None):
        """POST requests for the User object."""
        if params is None:
            params = {}
        result = self.client.post(object=object, path=path, params=params)
        return result

