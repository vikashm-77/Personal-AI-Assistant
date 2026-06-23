from commands.datetime_cmd import tell_time, tell_date

def handle_time_date(user_text):

    if any(x in user_text for x in [
        "what time is it",
        "current time",
        "time now",
        "time"
    ]):
        return tell_time()

    if any(x in user_text for x in [
        "today date",
        "current date",
        "what is today's date",
        "date"
    ]):
        return tell_date()

    return None