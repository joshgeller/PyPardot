class Opportunities():
    """
    A class to query and use Pardot opportunities.
    Opportunity field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#opportunity
    """

    def query(self, **kwargs):
        """
        Returns the opportunities matching the specified criteria parameters.
        Supported search criteria: http://developer.pardot.com/kb/api-version-3/querying-opportunities
        """
        result = self._get(path='/do/query', params=kwargs)
        return result

    def create_by_email(self, prospect_email=None, name=None, value=None, probability=None, **kwargs):
        """
        Creates a new opportunity using the specified data. <prospect_email> must correspond to an existing prospect.
        <name>, <value>, and <probability> correspond to the opportunity being created.
        """
        kwargs.update({'prospect_email': prospect_email, 'name': name, 'value': value, 'probability': probability})
        result = self._post(
            path='/do/create/prospect_email/{prospect_email}'.format(prospect_email=kwargs.get('prospect_email')),
            params=kwargs)
        return result

    def create_by_id(self, prospect_id=None, name=None, value=None, probability=None, **kwargs):
        """
        Creates a new opportunity using the specified data. <prospect_id> must correspond to an existing prospect.
        <name>, <value>, and <probability> correspond to the opportunity being created.
        """
        kwargs.update({'prospect_id': prospect_id, 'name': name, 'value': value, 'probability': probability})
        result = self._post(
            path='/do/create/prospect_id/{prospect_id}'.format(prospect_id=kwargs.get('prospect_id')),
            params=kwargs)
        return result

    def read(self, id=None):
        """
        Returns the data for the opportunity specified by <id>, including campaign assignment and associated visitor
        activities. <id> is the Pardot ID for the target opportunity.
        """
        result = self._get(path='/do/read/id/{id}'.format(id=id))
        return result

    def update(self, id=None):
        """
        Updates the provided data for the opportunity specified by <id>. <id> is the Pardot ID for the target
        opportunity. Fields that are not updated by the request remain unchanged. Returns an updated version of the
        opportunity.
        """
        result = self._get(path='/do/update/id/{id}'.format(id=id))
        return result

    def delete(self, id=None):
        """
        Deletes the opportunity specified by <id>. <id> is the Pardot ID for the target opportunity. Returns no response
        on success.
        """
        # TODO audit HTTP response
        result = self._get(path='/do/delete/id/{id}'.format(id=id))
        return result

    def undelete(self, id=None):
        """
        Un-deletes the opportunity specified by <id>. <id> is the Pardot ID for the target opportunity. Returns no
        response on success.
        """
        # TODO audit HTTP response
        result = self._get(path='/do/undelete/id/{id}'.format(id=id))
        return result

    def _get(self, path=None, params={}):
        """GET requests for the Opportunity object"""
        result = self.client._get(object='opportunity', path=path, params=params)
        return result

    def _post(self, path=None, params={}):
        """POST requests for the Opportunity object"""
        result = self.client._post(object='opportunity', path=path, params=params)
        return result