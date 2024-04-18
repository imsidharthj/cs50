def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")

def main():
    name = input("whats your name ")
    name =  convert(name)
    print(name)

main()