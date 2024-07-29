class Calculator:


    def add(self, num_1: float, num_2: float) -> float:
        return num_1 + num_2

    def subtrac(self, num_1: float, num_2: float) -> float:
        return num_1 - num_2

    def multiply(self, num_1: float, num_2: float) -> float:
        return num_1 * num_2

    def divide(self, num_1: float, num_2: float) -> float | str:
        if num_2 ==0:
            return "cannot divide by zero (0)"
        return num_1 / num_2