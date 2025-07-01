def calculate(num1: float, num2: float, operation: str):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre 0.")
        return num1 / num2
    else:
        raise ValueError("Operador no válido. Use solo +, -, * o /.")

if __name__ == "__main__":
    try:
        x = float(input("Ingrese el primer número: "))
        y = float(input("Ingrese el segundo número: "))
        z = input("Ingrese la operación que desea realizar (+, -, *, /): ")
        result = calculate(x, y, z)
        print("Resultado:", result)
    except ValueError as error:
        print(f"Error: {error}")
    except ZeroDivisionError as error:
        print(f"Error: {error}")

    
    
    
    