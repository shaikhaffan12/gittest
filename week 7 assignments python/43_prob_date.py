import datetime
import calendar
class mycls:
    def find_day(self,str1):
        born = datetime.datetime.strptime(txt, '%d %m %Y').weekday()
        print(calendar.day_name[born])

obj = mycls()
txt = input("Enter Date: ")
obj.find_day(txt)