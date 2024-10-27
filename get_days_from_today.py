from datetime import datetime

def get_days_from_today(date):
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - target_date
        
        
        return delta.days
    except Exception:
        
        return "Error: Please check the date format (should be 'YYYY-MM-DD') and ensure the input is valid."

print(get_days_from_today("2021-10-09"))   
print(get_days_from_today("2021-15-09"))   
print(get_days_from_today("invalid text"))
