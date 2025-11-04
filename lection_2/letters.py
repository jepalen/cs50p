SENDER= "Princess Peach"
RECEIVERS = ["Mario", "Luigi", "Toad", "Yoshi"]
def main():
    for receiver in RECEIVERS:
        print (write_letter(receiver,SENDER))
 

def write_letter(to,from_):
    return f"""
    ----------------
    Dear {to},
    You are cordially invited to my castle for tea and cake 
    this evening at 7 PM.
    Sincerely,
    {from_}
    ----------------
    """
          
 
main()