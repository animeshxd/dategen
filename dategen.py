from datetime import datetime, timedelta 
import asyncio
from pandas import date_range


class DateGen:
    def __init__(self):
        pass
    @staticmethod
    def today() -> str:
        return datetime.now().strftime("%Y-%m-%d")
    @staticmethod
    async def days(Range: int):
        return [(datetime.now() -  timedelta(days=i)).strftime("%Y-%m-%d")  for i in range(Range)]
    @staticmethod
    def last_week(last: int):
        last_week = datetime.now() - timedelta(weeks=last)
        return date_range(start=last_week.strftime('%Y/%m/%d'), end=datetime.now().strftime('%Y/%m/%d'))

if __name__ == '__main__':
    date = DateGen()
    print(date.today())
    print(asyncio.run(date.days(30)))    
    print(date.today() in date.last_week(5))

