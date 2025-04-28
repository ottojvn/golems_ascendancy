from game.constants import GAME_START_DAY, GAME_START_YEAR, GAME_DAYS_IN_YEAR

def init_date():
    # Initialize total based on start year and day
    total_initial_days = (GAME_START_YEAR - 1) * GAME_DAYS_IN_YEAR + (GAME_START_DAY - 1)
    return {'day': GAME_START_DAY, 'year': GAME_START_YEAR, 'days_in_year': GAME_DAYS_IN_YEAR, 'total': total_initial_days}

def advance_date(date, num_days=1):
    total = date['total'] + num_days
    days_in_year = date['days_in_year']
    # Calculate year based on total days, adding the base start year
    current_year = GAME_START_YEAR + (total // days_in_year)
    # Calculate day within the current year (1-based index)
    current_day = (total % days_in_year) + 1
    return {
        **date,
        'total': total,
        'year':  current_year,
        'day':   current_day,
    }