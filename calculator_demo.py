class Calculator:
    def __init__(self):
        self.x = 0
        self.y = 0

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        while True:
            if self.y != 0:
                return self.x / self.y
            else:
                print("Cannot divide by zero. Please enter a non-zero value.")
                return self.inputs()

    def inputs(self):
        self.x = float(input("Enter the first value (non-zero): "))
        self.y = float(input("Enter the second value: "))

    def calculate(self):
        print("--" * 20)
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("--" * 20)
        choice = input("Enter your choice of operation: ")

        if choice == '1' or choice.lower() == 'addition':
            print("Result:", self.add())
        elif choice == '2' or choice.lower() == 'subtraction':
            print("Result:", self.subtract())
        elif choice == '3' or choice.lower() == 'multiplication':
            print("Result:", self.multiply())
        elif choice == '4' or choice.lower() == 'division':
            print("Result:", self.divide())
        else:
            print("Invalid input. Please enter a valid choice.")


def main():
    calculated = Calculator()
    print("This is a calculator demo.")
    calculated.inputs()
    calculated.calculate()

if __name__ == "__main__":
    main()