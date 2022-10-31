def unique_letters(str):
    try:
        for letter in str:
            # verificar se aquela letra se repete na palavra
            if str.count(letter) > 1:
                return False
        return True
    except TypeError:
        return False


print(unique("palavra"))
