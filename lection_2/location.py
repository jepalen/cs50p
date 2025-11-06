import sys

def main():

    coordinates=(42.3601, -71.0589, 100)
    coordinatesInList= [42.3601, -71.0589, 100]
    latitude, longitude,another = coordinates
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Another:", another)

    print(f"the size of coordinates is {sys.getsizeof(coordinates)} bytes")
    print(f"the size of coordinatesInList is {sys.getsizeof(coordinatesInList)} bytes")

main()    