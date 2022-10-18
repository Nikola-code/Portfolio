def main():
    sentence = input()
    sentence = convert(sentence)
    print(sentence)

def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

main()