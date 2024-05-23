def main():
    correct_password = "Professer123"
    weapon_choice = None  

    while True:
        password = input("Enter password: ")
        if password != correct_password:
            continue
        print("BOOM, We Are In!")

        turtles = input("Do you like turtles? (yes/no): ").strip().lower()
        if turtles == "no":
            continue
        elif turtles == "yes":
            print("TURTLE GANG")

        ninja = input("Are you a ninja? (yes/no): ").strip().lower()
        if ninja == "no":
            continue
        elif ninja == "yes":
            print("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlByb2Zlc3NvcihQeXRoME5fQ2gwSzNfSDBMRH0iLCJpYXQiOjE1MTYyMzkwMjJ9.S2nn5l2YNytegukLdnodmHQM2PCYQOY6GjtnFWfvOpk")
            break

        token_like = input("Did you like the token we provided? (yes/no): ").strip().lower()
        if token_like == "no":
            continue
        elif token_like == "yes":
            print("Then maybe you should use it!")
            break

    weapon = input("Of the 3 weapons when fighting a monster, which would you choose?\nA. Fish\nB. Gummybear\nC. Water\n").strip().upper()
    if weapon == "A":
        pass
    elif weapon == "C":
        pass
    elif weapon == "B":
        weapon_choice = "Gummybear" 

    if weapon_choice:
        print(f"See ya later {weapon_choice}")

if __name__ == "__main__":
    main()
