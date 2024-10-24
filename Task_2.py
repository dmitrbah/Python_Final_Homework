# Напишите скрипт, который получает текущее время и дату, а затем выводит их в формате YYYY-MM-DD HH:MM:SS.
# Дополнительно, выведите день недели и номер недели в году.

from datetime import datetime

def get_current_date():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = now.isoweekday()
    week_number = now.isocalendar().week

    print(f'Текущая дата и время - {formatted_date}')
    print(f'День недели - {day_of_week}')
    print(f'Номер недели в году - {week_number}')

if __name__ == '__main__':
    get_current_date()