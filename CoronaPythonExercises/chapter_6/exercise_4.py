glossary = {
    'tuple': 'a values that cannot change.',
    'list': 'a collection of items in a particular order.',
    'variable': ' a boxes you can store values in.',
    'string': 'a series of characters.',
    'boolean': 'a subset of algebra used for creating true/false statements.',
    'dictionary': 'an associative array that holds key-value pairs.',
    'argument': 'a value we pass to a function or a method when calling it.',
    'attribute': 'a value an object holds.',
    'f-string': 'a formatted string literal, that lets us put in values into a string.',
    'conditional statement': 'a statement that contains an “if” or “if/else”.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")
