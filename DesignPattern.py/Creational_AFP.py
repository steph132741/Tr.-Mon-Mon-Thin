# #Without Abstract Factory
# class WindowsButton:
#     def paint(self):
#         print("Windows Button rendered")

# class MacButton:
#     def paint(self):
#         print("Mac Button rendered")

# # Client Code (without factory)
# def create_ui(os_type):
#     if os_type == "Windows":
#         button = WindowsButton()
#     elif os_type == "Mac":
#         button = MacButton()
#     else:
#         raise ValueError("Unknown OS type")

#     button.paint()

# # Example use
# create_ui("Windows")


#With Abstract Factory
# Step 1: Abstract Product
class Button:
    def paint(self):
        pass

# Step 2: Concrete Products
class WindowsButton(Button):
    def paint(self):
        print("Windows Button rendered")

class MacButton(Button):
    def paint(self):
        print("Mac Button rendered")

# Step 3: Abstract Factory
class GUIFactory:
    def create_button(self):
        pass

# Step 4: Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

# Step 5: Client Code
def create_ui(factory: GUIFactory):
    button = factory.create_button()
    button.paint()

# Example use
factory = MacFactory()
create_ui(factory)

