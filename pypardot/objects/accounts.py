class Accounts():
    """
    A class to query and use Pardot accounts.
    Account field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#prospectAccount
    """

    def __init__(self, client):
        self.client = client

    def query(self, **kwargs):
        """
        Returns the prospect accounts matching the specified criteria parameters.
        Supported search parameters: http://developer.pardot.com/kb/api-version-3/querying-prospect-accounts#supported-search-criteria
        """
        result = self._get(path='/do/query', params=kwargs)
        return result.get('result')

    def create(self, **kwargs):
        """Creates a new prospect account."""
        result = self._post(path='/do/create', params=kwargs)
        return result

    def describe(self, **kwargs):
        """
        Returns the field metadata for prospect accounts, explaining what fields are available, their types, whether
        they are required, and their options (for dropdowns, radio buttons, etc).
        """
        result = self._get(path='/do/describe', params=kwargs)
        return result

    def read(self, id=None, **kwargs):
        """
        Returns the data for the prospect account specified by <id>. <id> is the Pardot ID of the target prospect
        account.
        """
        kwargs['id'] = id
        result = self._post(path='/do/read/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def update(self, id=None, **kwargs):
        """
        Updates the data for the prospect account specified by <id>. <id> is the Pardot ID of the target prospect
        account.
        """
        kwargs['id'] = id
        result = self._post(path='/do/update/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def _get(self, object='prospectAccount', path=None, params=None):
        """GET requests for the Account object."""
        if params is None:
            params = {}
        result = self.client.get(object=object, path=path, params=params)
        return result

    def _post(self, object='prospectAccount', path=None, params=None):
        """POST requests for the Account object."""
        if params is None:
            params = {}
        result = self.client.post(object=object, path=path, params=params)
        return result


