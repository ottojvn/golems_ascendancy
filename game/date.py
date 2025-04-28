from game.constants import GAME_START_DAY, GAME_START_YEAR, GAME_DAYS_IN_YEAR

def init_date():
    return {'day': GAME_START_DAY, 'year': GAME_START_YEAR, 'days_in_year': GAME_DAYS_IN_YEAR, 'total': 0}

def advance_date(date, num_days=1):
    total = date['total'] + num_days
    days_in_year = date['days_in_year']
    return {
        **date,
        'total': total,
        'year':  total // days_in_year,
        'day':   (total % days_in_year) + 1,
    }