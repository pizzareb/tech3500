from app.addition import add
from app.subraction import subtract
from app.multiplication import multiply
from app.division import division



class Calculator:

    def addition(val1, val2):

        return add(val1, val2)

    def subtraction(val1, val2):
        return subtract(val1, val2)

    def multiplication(val1, val2):

        return multiply(val1, val2)

    def division(val1, val2):

        return divide(val1, val2)

