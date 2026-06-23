from datetime import datetime

def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    return f"The time is {current_time}"


def tell_date():
    current_date = datetime.now().strftime("%d %B %Y")
    return f"Today's date is {current_date}"