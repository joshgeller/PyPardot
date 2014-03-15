class VisitorActivities():
    """
    A class to query and use Pardot visitor activities.
    Visitor Activity field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#visitor-activity
    """

    def __init__(self, client):
        self.client = client

    def query(self, **kwargs):
        """
        Returns the visitor activities matching the specified criteria parameters.
        Supported search criteria: http://developer.pardot.com/kb/api-version-3/querying-visitor-activities#supported-search-criteria-
        """
        result = self._get(path='/do/query', params=kwargs)
        return result.get('result')

    def read(self, id=None, **kwargs):
        """
        Returns the data for the visitor activity specified by <id>. <id> is the Pardot ID for the target visitor activity.
        """
        kwargs['id'] = id
        result = self._post(path='/do/read/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def _get(self, object='visitorActivity', path=None, params=None):
        """GET requests for the Visitor Activity object."""
        if params is None:
            params = {}
        result = self.client.get(object=object, path=path, params=params)
        return result

    def _post(self, object='visitorActivity', path=None, params=None):
        """POST requests for the Visitor Activity object."""
        if params is None:
            params = {}
        result = self.client.post(object=object, path=path, params=params)
        return result

