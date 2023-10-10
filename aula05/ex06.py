def shorten(string):
    short_string = ""
    for char in string:
        if char.isupper():
            short_string += char
    return short_string

print(shorten("Universidade de Aveiro"))
print(shorten("United Nations Organization"))