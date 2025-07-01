class NotWordError(Exception):
    def __init__(self, message="Debe ingresar una palabra o frase válida (con letras)."):
        self.message = message
        super().__init__(self.message)

def palindrome(word):
    inverted_word = ""
    for i in range(len(word)-1,-1,-1):
        inverted_word += word[i]
    
    if word == inverted_word:
        return "Es palindromo"
    else:
        return "No es palindromo"
    
    
if __name__ == "__main__":
    try:
        x = input("Ingrese una palabra o frase: ").strip()
        if not x:
            raise NotWordError("No ingresó ningún texto.")
        print(palindrome(x))
    except NotWordError as error:
        print(f"Error: {error.message}")
    