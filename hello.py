from flask import Flask
# Create the logging_decorator() function 👇
def logging_decorator(*args):
    print(f"You called {args[0].__name__}({args[0]})")
    def call_inside(function):
        function()
    return call_inside()


# Use the decorator 👇
@logging_decorator
def a_function(numero1,numero2,numero3):
    resultado = numero1 * numero2* numero3
    return resultado

a_function(1,2,3)

