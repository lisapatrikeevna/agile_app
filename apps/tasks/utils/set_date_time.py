from datetime import datetime
import calendar
from django.utils import timezone


def last_day_of_month():
    today = timezone.now()
    amount_of_days = calendar.monthrange(today.year, today.month)[1]
    date = datetime(today.year, today.month, amount_of_days)
    # return date.astimezone(timezone.get_current_timezone())  #menyaem na tip jango
    return date.astimezone()  #menyaem na tip jango


































