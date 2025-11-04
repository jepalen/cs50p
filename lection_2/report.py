def main():
    spaceCraft = {
        "name": "Endeavour"
    }
    spaceCraft["crew_capacity"] = 5 
    spaceCraft.update({"type": "Orbiter", "missions": 25})

    print(create_report(spaceCraft))

def create_report(spaceCraft):
    return f"""
    ============================
    Spacecraft Report
    ============================
    Name: {spaceCraft.get('name','unknown')}
    Type: {spaceCraft['type']}
    Missions Flown: {spaceCraft['missions']}
    Total Distance Covered: {spaceCraft.get('distance','unknown')} million miles
    Crew Capacity: {spaceCraft.get('crew_capacity','unknown')} astronauts
    ============================
    """
main()