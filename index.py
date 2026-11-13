# 1. Payment System
class CreditCard:
    def pay(self, a): print("Credit Card:", a)

class UPI:
    def pay(self, a): print("UPI:", a)

class Cash:
    def pay(self, a): print("Cash:", a)

CreditCard().pay(1000)
UPI().pay(500)
Cash().pay(200)


# 2. Animal Sounds
class Dog:
    def sound(self): print("Barks")
class Cat:
    def sound(self): print("Meows")
class Cow:
    def sound(self): print("Moos")
class Lion:
    def sound(self): print("Roars")

def make_sound(animal):
    animal.sound()

for a in [Dog(), Cat(), Cow(), Lion()]:
    make_sound(a)


# 3. Notification – Duck Typing
class Email:
    def send(self, m): print("Email:", m)
class SMS:
    def send(self, m): print("SMS:", m)
class WhatsApp:
    def send(self, m): print("WhatsApp:", m)

def notify(obj):
    obj.send("Hello")

for n in [Email(), SMS(), WhatsApp()]:
    notify(n)


# 4. Vehicle System
class Car:
    def start(self): print("Car Started")
class Bike:
    def start(self): print("Bike Started")
class Bus:
    def start(self): print("Bus Started")

def start_vehicle(v):
    v.start()

for v in [Car(), Bike(), Bus()]:
    start_vehicle(v)


# 5. Employee Salary – Overriding
class Employee:
    def calculate_salary(self): print("Salary")
class Developer(Employee):
    def calculate_salary(self): print("50000")
class Manager(Employee):
    def calculate_salary(self): print("80000")
class Tester(Employee):
    def calculate_salary(self): print("40000")

for e in [Developer(), Manager(), Tester()]:
    e.calculate_salary()


# 6. Bank Account – Overriding
class BankAccount:
    def interest(self): print("Bank Interest")
class SavingsAccount(BankAccount):
    def interest(self): print("6% Interest")
class CurrentAccount(BankAccount):
    def interest(self): print("0% Interest")

SavingsAccount().interest()
CurrentAccount().interest()


# 7. Food Ordering System
class Food:
    def prepare(self): print("Preparing Food")
class Pizza(Food):
    def prepare(self): print("Preparing Pizza")
class Burger(Food):
    def prepare(self): print("Preparing Burger")
class Biryani(Food):
    def prepare(self): print("Preparing Biryani")

def order(food):
    food.prepare()

for f in [Pizza(), Burger(), Biryani()]:
    order(f)


# 8. Notification System
class Notification:
    def send(self): print("Notification")
class EmailNotification(Notification):
    def send(self): print("Email Sent")
class SMSNotification(Notification):
    def send(self): print("SMS Sent")
class PushNotification(Notification):
    def send(self): print("Push Notification Sent")

def send_notification(n):
    n.send()

for n in [EmailNotification(), SMSNotification(),
          PushNotification()]:
    send_notification(n)