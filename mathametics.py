class employee:
   "this class is for employees of MB"
   name = "affan"
   age = 10

   def emp_func(self):
       print(f"{self.name} is an employee of MB and his age is {self.age}")

obj = employee()

print(obj.name)

obj.emp_func()