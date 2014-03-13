class Visits():
    """
    A class to query and use Pardot visits.
    Prospect field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#visit
    """

    def __init__(self, client):
        self.client = client

    def query_by_ids(self, ids=None, **kwargs):
        """Returns the visits matching the given <ids>. The <ids> should be comma separated integers (no spaces)."""
        kwargs['ids'] = ids.replace(' ', '')
        result = self._post(path='/do/query', params=kwargs)
        return result

    def query_by_visitor_ids(self, visitor_ids=None, **kwargs):
        """
        Returns the visits matching the given <visitor ids>. The <visitor ids> should be comma separated integers (no spaces)."""
        kwargs['visitor_ids'] = visitor_ids.replace(' ', '')
        result = self._post(path='/do/query', params=kwargs)
        return result

    def query_by_prospect_ids(self, prospect_ids=None, **kwargs):
        """
        Returns the visits matching the given <prospect ids>. The <prospect ids> should be comma separated integers (no spaces)."""
        kwargs['prospect_ids'] = prospect_ids.replace(' ', '')
        result = self._post(path='/do/query', params=kwargs)
        return result

    def read(self, id=None, **kwargs):
        """
        Returns the data for the visit specified by <id>. <id> is the Pardot ID of the target visit."""
        kwargs['id'] = id
        result = self._post(path='/do/read/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def _get(self, path=None, params=None):
        """GET requests for the Visit object"""
        if params is None:
            params = {}
        result = self.client._get(object='visit', path=path, params=params)
        return result

    def _post(self, path=None, params=None):
        """POST requests for the Visit object"""
        if params is None:
            params = {}
        result = self.client._post(object='visit', path=path, params=params)
        return result

