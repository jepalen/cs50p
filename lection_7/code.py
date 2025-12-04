import re

def main():
    code = input("Hexadecimal color code: ").strip()
    pattern =r"^#[A-Fa-f0-9]{6}$"
    match = re.search(pattern, code)

    if match:
        print(f"Valid. matched with: {match.group()}")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()