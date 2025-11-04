distances = {
    "Endeavour": 250,
    "Discovery": 300,
    "Challenger": 200,
    "Columbia": 400,
}

def convert_to_km(au):
    return au * 149597870.7

def main():
    for name in distances.keys() :
        print(f"{name} : {distances[name]} in au")

    for distance in distances.values() :
        print(f"{distance} au is : {convert_to_km(distance)} m")    
main()