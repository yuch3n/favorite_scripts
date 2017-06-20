__author__ = 'john.houg____'

from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "AC3d81515c________c5828e1f3258f4"
AUTH_TOKEN = "0f66659b________4c29cc815bc0a3c"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
	to="619581xxxx",
	from_="+176061xxxx",
	body="""Use the crosstab function to compute a cross-tabulation of two (or more) factors. By default crosstab computes a frequency table of the factors unless an array of values and an aggregation function are passed.
It takes a number of arguments

index: array-like, values to group by in the rows
columns: array-like, values to group by in the columns
values: array-like, optional, array of values to aggregate according to the factors
aggfunc: function, optional, If no values array is passed, computes a frequency table
rownames: sequence, default None, must match number of row arrays passed
colnames: sequence, default None, if passed, must match number of column arrays passed
margins: boolean, default False, Add row/column margins (subtotals)""",
	# media_url="http://www.economicfreedom.org/wp-content/uploads/2014/03/Cell-phone-3.14.14_single-use-only.jpg",
)