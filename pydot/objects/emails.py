class Emails():
    """
    A class to query and send Pardot emails.
    Email field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#email
    """

    def __init__(self, client):
        self.client = client

    def send(self, **kwargs):
        """
        Sends a one-to-one email to the given prospect email, prospect ID, or list IDs
        Supported parameters: http://developer.pardot.com/kb/api-version-3/sending-one-to-one-emails#supported-parameters-
        """
        if 'prospect_email' in kwargs:
            path = '/do/send/prospect_email/{prospect_email}'.format(prospect_email=kwargs.get('prospect_email'))
        elif 'prospect_id' in kwargs:
            path = '/do/send/prospect_id/{prospect_id}'.format(prospect_id=kwargs.get('id'))
        else:
            path = '/do/send'
        result = self._post(path=path, params=kwargs)
        return result

    def read(self, id):
        """
        Returns the data for the email specified by id.
        id is the Pardot ID of the target email.
        """
        result = self._get(path='/do/read/id/{id}'.format(id=id))
        return result

    def _get(self, path=None, params={}):
        """GET requests for the Email object"""
        result = self.client._get(object='email', path=path, params=params)
        return result

    def _post(self, path=None, params={}):
        """POST requests for the Email object"""
        result = self.client._post(object='email', path=path, params=params)
        return result