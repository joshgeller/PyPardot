class Visitors():
    """
    A class to query and use Pardot visitors.
    Visitor field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#visitor
    """

    def __init__(self, client):
        self.client = client

    def query(self, **kwargs):
        """
        Returns the visitors matching the specified criteria parameters.
        Supported search criteria: http://developer.pardot.com/kb/api-version-3/querying-visitors#supported-search-criteria-
        """
        result = self._get(path='/do/query', params=kwargs)
        return result.get('result')

    def assign(self, id=None, **kwargs):
        """
        Assigns or reassigns the visitor specified by <id> to a specified prospect. One (and only one) of the following
        parameters must be provided to identify the target prospect: <prospect_email> or <prospect_id>. Returns an
        updated version of the visitor.
        """
        kwargs['id'] = id
        result = self._post(path='/do/assign/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def read(self, id=None, **kwargs):
        """
        Returns the data for the visitor specified by <id>, including associated visitor activities, identified
        company data, and visitor referrers. <id> is the Pardot ID for the target visitor.
        """
        kwargs['id'] = id
        result = self._post(path='/do/read/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def _get(self, object='visitor', path=None, params=None):
        """GET requests for the Visitor object."""
        if params is None:
            params = {}
        result = self.client.get(object=object, path=path, params=params)
        return result

    def _post(self, object='visitor', path=None, params=None):
        """POST requests for the Visitor object."""
        if params is None:
            params = {}
        result = self.client.post(object=object, path=path, params=params)
        return result

