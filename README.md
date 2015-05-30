PyPardot
=========
PyPardot is an API wrapper for [Pardot](http://www.pardot.com/), written in Python.

Using it is simple:

```
from pypardot.client import PardotAPI


p = PardotAPI(
                email='your_pardot_email',
                password='your_pardot_password',
                user_key='your_pardot_user_key'
                )
                
p.authenticate()

# Create a new prospect
p.prospects.create_by_email(email='joe@company.com', first_name='Joe', last_name='Schmoe')

# Update a prospect field
p.prospects.update_field_by_email(email='joe@company.com', field='company', field_value='Joes Plumbing')

# Update or create a prospect
p.prospects.upsert_by_email(email='joe@company.com', first_name='Joe', last_name='Schmoe')

# Send a one-off email
p.emails.send_to_email(prospect_email='joe@company.com', email_template_id=123, campaign_id=456)
```

Features
---

+ Includes all documented Pardot API operations
+ Handles API key expiration
+ Detailed API error handling

Object Types & Operations
---

Support for the following object types:

+ Accounts
+ Emails
+ Lists
+ Opportunities
+ Prospects
+ Users
+ Visitor Activities
+ Visitors
+ Visits

Required
---

+ [requests](http://docs.python-requests.org/en/latest/)

Installation
---

Install PyPardot by running:
```
pip install pypardot
```

Usage
---

###Authentication

To connect to the Pardot API, you'll need the e-mail address, password, and user key associated with your Pardot account. Your user key is available in the Pardot application under My Settings.

The client will authenticate before performing other API calls, but you can manually authenticate as well:


```
p = PardotAPI(
                email='your_pardot_email',
                password='your_pardot_password',
                user_key='your_pardot_user_key'
                )
                
p.authenticate()
```

###Querying Objects

Supported search criteria varies for each object. Check the [official Pardot API documentation](http://developer.pardot.com/kb/api-version-3/introduction-table-of-contents) for supported parameters. Most objects support `limit`, `offset`, `sort_by`, and `sort_order` parameters. PyPardot returns JSON for all API queries.

**Note**: Pardot only returns 200 records with each request. Use `offset` to retrieve matching records beyond this limit.

```
# Query and iterate through today's prospects
prospects = p.prospects.query(created_after='yesterday')
total = prospects['total_results'] # total number of matching records
for prospect in prospects['prospect']
  print(prospect.get('first_name'))
```

### Editing/Updating/Reading Objects

Supported fields varies for each object. Check the [official Pardot API documentation](http://developer.pardot.com/kb/api-version-3/introduction-table-of-contents) to see the fields associated with each object. 

```
# Create a new prospect
p.prospects.create_by_email(email='joe@company.com', first_name='Joe', last_name='Schmoe')

# Update a prospect field (works with default or custom field)
p.prospects.update_field_by_email(email='joe@company.com', field='company', field_value='Joes Plumbing')

# Send a one-off email
p.emails.send_to_email(prospect_email='joe@company.com', email_template_id=123)
```

### Extras

PyPardot supports some un-documented API methods:

+ `prospects.add_to_list`: Adds the prospect to a Pardot list
+ `prospects.update_field_by_email`: Updates the value for a single default or custom field
+ `prospects.read_field_by_email`: Returns the value for a single default or custom field
+ More coming soon!

### Error Handling

#### Handling expired API keys

Pardot API keys expire after 60 minutes. If PyPardot detects an 'Invalid API key' error during any API call, it will automatically attempt to re-authenticate and obtain a new valid API key. If re-authentication is successful, the API call will be re-issued. If re-authentication fails, a `PardotAPIError` is thrown.

#### Invalid API parameters

If an API call is made with missing or invalid parameters, a `PardotAPIError` is thrown. Error instances contain the error code and message corresponding to error response returned by the API. See [Pardot Error Codes & Messages](http://developer.pardot.com/kb/api-version-3/error-codes-and-messages) in the official documentation.

Performing API calls is inherently unsafe, so be sure to catch exceptions:

```
try:
  p.prospects.create_by_email(email='existing.email.address@company.com')
except PardotAPIError, e:
  print(e)
```
