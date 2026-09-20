from abc import abstractmethod, ABC

#Abstract products
class Checkbox(ABC):
    @abstractmethod
    def view_checkbox(self):
        pass

class Button(ABC):
    @abstractmethod
    def view_button(self):
        pass

#Concrete Products
class WindowsButton(Button):
    def view_button(self):
        print("Windows Button is pressed ...")

class MacButton(Button):
    def view_button(self):
        print("Mac Button is pressed ...")

class WindowsCheckbox(Checkbox):
    def view_checkbox(self):
        print("Windows Checkbox is pressed ...")

class MacCheckbox(Checkbox):
    def view_checkbox(self):
        print("Mac Checkbox is pressed ...")

#Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

#Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()
    def create_checkbox(self):
        return MacCheckbox()

#User
factory = MacFactory()
button = factory.create_button()
checkbox = factory.create_checkbox()

button.view_button()
checkbox.view_checkbox()