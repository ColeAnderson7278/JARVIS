import json
import datetime


def check_dates(reminder_list):
    today = datetime.date.today()
    messages = []
    for reminder in reminder_list:
        if reminder['date'] == str(today):
            messages.append(reminder['message'])
    if messages == []:
        return ["Nothing on your to-do list"]
    else:
        return messages
