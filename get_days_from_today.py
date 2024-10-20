from datetime import datetime

def get_days_from_today(date):
    
    try:
    
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        
        today = datetime.today().date()
        
        
        delta = today - input_date
        
        
        return delta.days
    except ValueError:
        # Якщо формат дати неправильний, повідомляємо користувача
        raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")


print(get_days_from_today("2021-10-09"))  
print(get_days_from_today("2025-01-01"))