class Prospects():
    """
    A class to query and use Pardot prospects.
    Prospect field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#prospect
    """

    def __init__(self, client):
        self.client = client

    def query(self, **kwargs):
        """
        Returns the prospects matching the specified criteria parameters.
        Supported search parameters: http://developer.pardot.com/kb/api-version-3/querying-prospects#supported-search-criteria
        ex: client.Prospects.query(created_after='yesterday', assigned='false', limit=100)
        """
        result = self._get(path='/do/query', params=kwargs)
        return result

    def assign(self, **kwargs):
        """
        Assigns or reassigns the prospect specified by <email> or <id> to a specified Pardot user or
        group. One (and only one) of the following parameters must be provided to identify the target user or
        group: <user_email>, <user_id>, or <group_id>. Returns an updated version of the prospect.
        """
        if 'email' in kwargs:
            path = '/do/assign/email/{email}'.format(email=kwargs.get('email'))
        elif 'id' in kwargs:
            path = '/do/assign/id/{id}'.format(id=kwargs['id'])
        else:
            path = '/do/assign/'
        result = self._post(path=path, params=kwargs)
        return result

    def unassign(self, **kwargs):
        """
        Unassigns the prospect specified by <email> or <id>. Returns an updated version of the prospect.
        """
        if 'email' in kwargs:
            path = '/do/unassign/email/{email}'.format(email=kwargs.get('email'))
        elif 'id' in kwargs:
            path = '/do/unassign/id/{id}'.format(id=kwargs.get('id'))
        else:
            path = '/do/unassign/'
        result = self._post(path=path, params=kwargs)
        return result

    def create(self, **kwargs):
        """
        Creates a new prospect using the specified data. <email> must be a unique email address. Returns the new prospect.
        """
        result = self._post(path='/do/create/email/{email}'.format(email=kwargs.get('email')), params=kwargs)
        return result

    def read(self, **kwargs):
        """
        Returns data for the prospect specified by <email> or <id>, including campaign assignment, profile criteria
        matching statuses, associated visitor activities, email list subscriptions, and custom field data.
        <email> is the email address of the target prospect. <id> is the Pardot ID of the target prospect.
        """
        if 'email' in kwargs:
            path = '/do/read/email/{email}'.format(email=kwargs.get('email'))
        elif 'id' in kwargs:
            path = '/do/read/id/{id}'.format(id=kwargs.get('id'))
        else:
            path = '/do/read/'
        result = self._post(path=path, params=kwargs)
        return result

    def update(self, **kwargs):
        """
        Updates the provided data for a prospect specified by <email> or <id>. <email> is the email address of the
        prospect. <id> is the Pardot ID of the prospect. Fields that are not updated by the request remain unchanged.
        Email list subscriptions and custom field data may also be updated with this request.
        """
        if 'email' in kwargs:
            path = '/do/update/email/{email}'.format(email=kwargs.get('email'))
        elif 'id' in kwargs:
            path = '/do/update/id/{id}'.format(id=kwargs.get('id'))
        else:
            path = '/do/update/'
        result = self._post(path=path, params=kwargs)
        return result

    def upsert(self, **kwargs):
        """
        Updates the provided data for a prospect specified by <email> or <id>. If a prospect with the provided email
        address does not yet exist, a new prospect is created using the <email> value. <email> is the email address of
        the prospect. <id> is the Pardot ID of the prospect. Fields that are not updated by the request remain
        unchanged. Email list subscriptions and custom field data may also be updated with this request.
        """
        if 'email' in kwargs:
            path = '/do/upsert/email/{email}'.format(email=kwargs.get('email'))
        elif 'id' in kwargs:
            path = '/do/upsert/id/{id}'.format(id=kwargs.get('id'))
        else:
            path = '/do/upsert/'
        result = self._post(path=path, params=kwargs)
        return result

    def delete(self, **kwargs):
        """
        Deletes the prospect specified by <email>.
        """
        if 'email' in kwargs:
            path = '/do/delete/email/{email}'.format(email=kwargs.get('email'))
        elif 'id' in kwargs:
            path = '/do/delete/id/{id}'.format(id=kwargs.get('id'))
        else:
            path = '/do/delete/'
        try:
            self._post(path=path, params=kwargs)
        # API doesn't return JSON, so we'll get a ValueError on success.
        # TODO Find a way to clean this up.
        except ValueError:
            pass


    def _get(self, path=None, params={}):
        """GET requests for the Prospect object"""
        result = self.client._get(object='prospect', path=path, params=params)
        return result

    def _post(self, path=None, params={}):
        """POST requests for the Prospect object"""
        result = self.client._post(object='prospect', path=path, params=params)
        return result

