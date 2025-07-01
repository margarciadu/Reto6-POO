class NoAnagramsFoundError(Exception):
    def __init__(self, message="No se encontraron anagramas en la lista."):
        self.message = message
        super().__init__(self.message)

def same_characters(words: list[str]) -> list[str]:
    groups = {}

    for word in words:
        key = ''.join(sorted(word.lower()))  # Ignorar mayúsculas
        groups.setdefault(key, []).append(word)

    result = []
    for group in groups.values():
        if len(group) > 1:
            result.extend(group)

    if not result:
        raise NoAnagramsFoundError()

    return list(set(result))  # Evitar duplicados

if __name__ == "__main__":
    try:
        x = input("Ingrese una lista de palabras separadas por espacios: ").strip()
        if not x:
            raise ValueError("Debe ingresar al menos dos palabras.")
        
        y = x.split()
        if len(y) < 2:
            raise ValueError("Debe ingresar al menos dos palabras.")
        
        result = same_characters(y)
        print("Palabras con los mismos caracteres (anagramas):")
        print(result)

    except NoAnagramsFoundError as nae:
        print("Error:", nae)
    except ValueError as error:
        print(f"Error: {error}")

