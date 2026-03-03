import datetime

# ----- PSEUDOCODE -----
# timestamp(): Get the current date and time, format it as YYYY-MM-DD HH:MM:SS, return it

# ----- CODE & PSEUDOCODE -----

# Pseudocode for timestamp():
# - Get current datetime
# - Format as "YYYY-MM-DD HH:MM:SS"
# - Return the formatted string
def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")