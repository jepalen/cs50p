import re

locations= {"+1": "United States", "+44": "United Kingdom", "+34": "Spain"}

def main():
    phone = input("Phone number: ").strip()
    pattern =r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    match = re.search(pattern, phone)

    if match:
        print(f"Valid. matched with: {match.group('country_code')}")
        country_code = match.group('country_code')
        print(f"Location: {locations.get(country_code, 'Unknown')}")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()