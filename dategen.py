from datetime import datetime, timedelta 
import asyncio
from pandas import date_range
from calendar import Calendar

class DateGen:
    def __init__(self):
        pass
    @staticmethod
    async def today() -> str:
        return datetime.now().strftime("%Y-%m-%d")
    @staticmethod
    async def days(Range: int):
        return [(datetime.now() -  timedelta(days=i)).strftime("%Y-%m-%d")  for i in range(Range)]
    @staticmethod
    async def last_week(last: int):
        last_week = datetime.now() - timedelta(weeks=last)
        return date_range(start=last_week.strftime('%Y/%m/%d'), end=datetime.now().strftime('%Y/%m/%d'))
    @staticmethod
    async def this_month():
        year = datetime.today().year
        month = datetime.today().month
        iter_ = Calendar().itermonthdates(year,month)
        return [ i.strftime('%Y-%m-%d') for i in iter_ if i.month == month]

if __name__ == '__main__':
    date = DateGen()
    print(asyncio.run(date.today()))
    print(asyncio.run(date.days(30)))   
    print(asyncio.run(date.last_week(5)))
    # print(date.today() in date.last_week(5))
    print(asyncio.run(date.this_month()))
    

