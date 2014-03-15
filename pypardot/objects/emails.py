class Emails():
    """
    A class to query and send Pardot emails.
    Email field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#email
    """

    def __init__(self, client):
        self.client = client

    def send_to_email(self, prospect_email=None, **kwargs):
        """
        Sends an email to the prospect identified by <prospect_email>.
        Required parameters: (email_template_id OR (text_content, name, subject, & ((from_email & from_name) OR from_user_id)))
        """
        kwargs['prospect_email'] = prospect_email
        result = self._post(
            path='/do/send/prospect_email/{prospect_email}'.format(prospect_email=kwargs.get('prospect_email')),
            params=kwargs)
        return result

    def send_to_id(self, prospect_id=None, **kwargs):
        """
        Sends an email to the prospect identified by <prospect_id>.
        Required parameters: (email_template_id OR (text_content, name, subject, & ((from_email & from_name) OR from_user_id)))
        """
        kwargs['prospect_id'] = prospect_id
        result = self._post(
            path='/do/send/prospect_id/{prospect_id}'.format(prospect_id=kwargs.get('prospect_id')), params=kwargs)
        return result

    def send_to_lists(self, list_ids=None, **kwargs):
        """
        Sends an email to the lists identified by <list_ids>.
        Required parameters: (email_template_id OR (text_content, name, subject, & ((from_email & from_name) OR from_user_id)))
        """
        kwargs['list_ids'] = list_ids
        result = self._post(
            path='/do/send/', params=kwargs)
        return result

    def read(self, id=None):
        """Returns the data for the email specified by <id>. <id> is the Pardot ID of the target email."""
        result = self._post(path='/do/read/id/{id}'.format(id=id))
        return result

    def _get(self, object='email', path=None, params=None):
        """GET requests for the Email object."""
        if params is None:
            params = {}
        result = self.client.get(object=object, path=path, params=params)
        return result

    def _post(self, object='email', path=None, params=None):
        """POST requests for the Email object."""
        if params is None:
            params = {}
        result = self.client.post(object=object, path=path, params=params)
        return result