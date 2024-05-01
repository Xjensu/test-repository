file = open("config.txt","r",encoding="UTF-8")

def print_hello():
    print(file.readline())


print_hello()