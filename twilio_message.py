import time
import schedule
from twilio.rest import Client

monday_message = """ Dear Manager. Please remember to conduct a performance review of each employee in your department 
for the week and submit it by Friday. Also, please kindly deliver feedback to employees to state whether they need to 
either up their game or maintain their current level."""

friday_reminder = """Dear Manager. Please note that the performance review for your department employees is due today 
before the end of working hours."""


def send_message_monday(reminder_message=monday_message):
	"""Sends the first message on Monday"""
	account_sid = " "  #enter your account SID
	auth_token = " "   #enter your auth token here 
	client = Client(account_sid, auth_token)

	# sending the message. Format is from Twilio
	client.messages.create(to =" ", #enter your receipient cellphone number here  
							from_= " ", #enter your Twilio cellphone number that they give you
							body=reminder_message)


def send_message_friday(reminder_message=friday_reminder):
	"""Sends the final reminder on Friday"""
	account_sid = " "  #enter your account SID
	auth_token = " "   #enter your auth token here 
	client = Client(account_sid, auth_token)

	# sending the message. Format is from Twilio
	client.messages.create(to =" ", #enter your receipient cellphone number here  
							from_= " ",  #enter your Twilio cellphone number that they give you
							body=reminder_message)

# the schedule to send the message function (send_message_monday) on Monday at a specific time
schedule.every().monday.at("09:00").do(send_message_monday)

# the schedule to send the message function (send_message_friday) on Friday at a specific time
schedule.every().friday.at("14:00").do(send_message_friday)


# A test to see if it works (It does)
schedule.every().saturday.at("14:33").do(send_message_monday)


# checks whether a scheduled task is pending to run or not
# straight from the Schedule documentation
while True:
	schedule.run_pending()
	time.sleep(2)






