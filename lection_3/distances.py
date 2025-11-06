distances = {
    "Endeavour": "250",
    "Discovery": "300",
    "Challenger": "200 AU",
    "Columbia": "400 AU",
}

def convert_to_km(au):
    return au * 149597870.7

def main():
    spacecraft = input('Select the spacecraft: ')
    try:
        au= float(distances[spacecraft])
    except KeyError:
        print(f'the spacecraft "{spacecraft}" is not in the dictionary')
        return
    except ValueError:  
        print(f'the value: "{distances[spacecraft]}" cant be converted to float') 
        return 

    km = convert_to_km(au)
    print(f'the distance in km for {spacecraft} is {km}')
main()