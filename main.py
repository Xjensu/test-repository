file = open("config.txt","r",encoding="UTF-8")

def summ():
    text = file.read().split()
    a:int = int(text[0])
    b:int = int(text[1])
    print(a + b)


summ()