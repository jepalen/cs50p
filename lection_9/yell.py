def yell(*words):
    uppercase= map(str.upper,words)
    print(*uppercase)

def yell_comprehension(*words):
    uppercase= [word.upper() for word in words]
    print(*uppercase)

def main():
    yell("hello","world","python")
    yell_comprehension("hella","worlda","pythona")

if __name__ == "__main__":
    main()