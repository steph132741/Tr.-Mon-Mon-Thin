# #Without Command Pattern
# class Light:
#     def on(self):
#         print("Light ON")

#     def off(self):
#         print("Light OFF")

# class RemoteControl:
#     def press_button(self, action, light):
#         if action == "on":
#             light.on()
#         elif action == "off":
#             light.off()

# # Usage
# light = Light()
# remote = RemoteControl()
# remote.press_button("on", light)
# remote.press_button("off", light)

#With Command Pattern
# Receiver
class Light:
    def on(self):
        print("Light ON")

    def off(self):
        print("Light OFF")

# Command Interface
class Command:
    def execute(self):
        pass

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()
        
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

# Invoker
class RemoteControl:
    def submit(self, command: Command):
        command.execute()

# Client
light = Light()
on_command = LightOnCommand(light)
off_command = LightOffCommand(light)

remote = RemoteControl()
remote.submit(on_command)
remote.submit(off_command)
