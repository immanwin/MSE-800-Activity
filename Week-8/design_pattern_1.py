from abc import ABC, abstractmethod

# Abstract Method
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

# Concrete Products
class Email:
    def send(self):
        print("You have an Email notification...")
class SMS:
    def send(self):
        print("You have an SMS notification...")
class Push:
    def send(self):
        print("You have an Push notification...")

# Factory Creator
class NotificationFactory:
    @abstractmethod
    def send_notification(self):
        pass

#Concrete Factories
class EmailFactory(NotificationFactory):
    def send_notification(self):
        return Email()
class SMSFactory(NotificationFactory):
    def send_notification(self):
        return SMS()
class PushFactory(NotificationFactory):
    def send_notification(self):
        return Push()

#Main (apart from Class)

factory_1 = SMSFactory()
notify = factory_1.send_notification()
notify.send()

factory_2 = EmailFactory()
notify = factory_2.send_notification()
notify.send()