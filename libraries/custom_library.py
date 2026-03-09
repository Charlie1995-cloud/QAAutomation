class CustomLibrary:

    def say_hello(self, name):
        print(f"Hello {name}")

    def add_numbers(self, a, b):
        return int(a) + int(b)

    def check_number(self, number):
        if int(number) > 10:
            return "Number is greater than 10"
        return "Number is 10 or less"