class hr_to_sec:
    
    def hour_to_sec(self, hour):
        hour = int(input("Enter Hours: "))
        sec = hour * 3600
        print(f"the second for {hour} hour is {sec} second.")
        

obj = hr_to_sec()
obj.hour_to_sec(obj)