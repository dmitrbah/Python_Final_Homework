# Напишите функцию, которая принимает количество дней от текущей даты и возвращает дату, которая
# наступит через указанное количество дней. Дополнительно, выведите эту дату в формате YYYY - MM - DD.

from datetime import datetime, timedelta


def get_future_date(days_number):
    now = datetime.now()
    future_date = now + timedelta(days_number)
    return future_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    days = 10
    print(f'Через {days} дней наступит {get_future_date(days)}')