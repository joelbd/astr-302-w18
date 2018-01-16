#!/anaconda2/bin/python
# calc.py

# Define a caluclator class that has methods: add, subtract, multiply, divide, clear
class Calculator:
  # Take some numbers and do math upon them

  def __init__(self, value = 0.0):
    self.value = self._is_number(value)

  # Add input number to the current self.value
  def add(self, userInput):
    inputVal = self._is_number(userInput)
    self.value += inputVal
    return self.value

  # Subtract input number from the current self.value
  def sub(self, userInput):
    inputVal = self._is_number(userInput)
    self.value -= inputVal
    return self.value

  # Multiply current self.value by the input number
  def mul(self, userInput):
    inputVal = self._is_number(userInput)
    self.value *= inputVal
    return self.value

  # Divide current self.value by the input number
  def div(self, userInput):
    inputVal = self._is_number(userInput)
    self.value /= inputVal
    return self.value

  # Reset self.value to default number 0.0
  def clr(self):
    self.value = 0.0
    return self.value

  # Verify if argument is a valid number
  def _is_number(self, userInput):
    try:
      inputNumber = float(userInput)
    except ValueError:
      print("Error: the input must be a number")
    return inputNumber

  # Output current self.value
  def result(self):
    return self.value
