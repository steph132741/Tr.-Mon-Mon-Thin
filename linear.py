class LinearSearch:
    def __init__(self, data):
        """Initialize the list of elements."""
        self.data = data

    def search_element(self, target):
        """
        Perform a linear search for the target element.
        Returns the index if found, otherwise -1.
        """
        for i in range(len(self.data)): 
            if self.data[i] == target:
                return i 
        return -1 

numbers = [10, 25, 36, 47, 58, 69, 80]
search_obj = LinearSearch(numbers)

target = int(input("Enter number to search: "))
result = search_obj.search_element(target)

# Displaying the result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
