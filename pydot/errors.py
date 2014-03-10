class PardotAPIError(Exception):
    """
    Basic exception class for errors encountered in API post and get requests.
    Takes the json response and parses out the error code and message.
    """

    def __init__(self, response):
        self.response = response
        try:
            self.err_code = response['@attributes']['err_code']
            self.message = str(response['err'])
        except KeyError:
            self.err_code = 0
            self.message = 'Unknown error occurred'

    def __str__(self):
        #print('Raw JSON error response: {}'.format(self.response))
        return 'Error {err_code}: {message}'.format(err_code=self.err_code, message=self.message)