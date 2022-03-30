from convert_hours_to_second import hr_to_sec


class conversion:
    def __init__(self) :
        self.hrs = int(input("Enter A number for hours: "))
        self.minutes = int(input("Enter A number for minutes: "))


    def hr_min_to_sec(self):
        hr_to_sec = self.hrs * 3600
        mins_to_sec = self.minutes * 60
        return hr_to_sec,mins_to_sec


obj = conversion()
new = obj.hr_min_to_sec()
print(new)