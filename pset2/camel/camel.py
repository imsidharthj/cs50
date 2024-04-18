camelString = input("camelCase: ")

def camel_to_sanke(camelString):
 snake = ""
 for i in camelString:
    if i.isupper():
         snake = snake + "_" + i.lower()
    else:
         snake = snake + i
 return snake

snake_case = camel_to_sanke(camelString)

print("snake_case: ", snake_case)