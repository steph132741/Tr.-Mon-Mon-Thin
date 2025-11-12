# #Wothout Flyweight
# class Character:
#     def __init__(self, symbol, font):
#         self.symbol = symbol
#         self.font = font

#     def display(self, position):
#         print(f"{self.symbol} in {self.font} at {position}")

# # Create characters
# chars = []
# for i in range(1_000_000):
#     chars.append(Character('A', 'Arial'))

# print(f"Created {len(chars)} characters")

#With Flyweight
# Flyweight class
class Character:
    def __init__(self, symbol, font):
        self.symbol = symbol  # intrinsic (shared)
        self.font = font      # intrinsic (shared)

    def display(self, position):
        print(f"{self.symbol} in {self.font} at {position}")

# Flyweight Factory
class CharacterFactory:
    _characters = {}

    def get_character(self, symbol, font):
        key = (symbol, font)
        if key not in self._characters:
            self._characters[key] = Character(symbol, font)
        return self._characters[key]

# Client code
factory = CharacterFactory()
chars = []

for i in range(10):
    char = factory.get_character('A', 'Arial')
    chars.append(char)

print(f"Unique objects created: {len(factory._characters)}")
chars[0].display(1)
chars[1].display(2)
