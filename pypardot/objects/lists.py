class Lists():
    """
    A class to query and use Pardot lists.
    List field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#list
    """

    def __init__(self, client):
        self.client = client

    def query(self, **kwargs):
        """
        Returns the lists matching the specified criteria parameters.
        Supported search parameters: http://developer.pardot.com/kb/api-version-3/querying-lists
        """
        result = self._get(path='/do/query', params=kwargs)
        return result.get('result')

    def read(self, id=None):
        """
        Returns the data for the list specified by <id>.<id> is the Pardot ID of the target list.
        """
        result = self._post(path='/do/read/id/{id}'.format(id=id))
        return result

    def _get(self, object='list', path=None, params=None):
        """GET requests for the List object."""
        if params is None:
            params = {}
        result = self.client.get(object=object, path=path, params=params)
        return result

    def _post(self, object='list', path=None, params=None):
        """POST requests for the List object."""
        if params is None:
            params = {}
        result = self.client.post(object=object, path=path, params=params)
        return result

