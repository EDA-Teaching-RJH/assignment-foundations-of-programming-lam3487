def init_database():
    names = ["Jonathan Archer", "Julian Bashir", "B'Etor", "Brunt", "Boothby"]
    ranks = ["Captain", "Lieutenant", "Commander","Ensign", "Ensign"]
    divisions = ["Command", "Science", "Operations", "Operations", "Operations"]
    IDs = ["1", "2", "3", "4", "5"]
    return names, ranks, divisions, IDs

def display_menu():
    user = input("what is your full name?")
    print("\n MENU")
    print("1. add member")
    print("2. remove member")
    print("3. update rank")
    print("4. diplay roster")
    print("5. search crew")
    print("6. filter by division")
    print("7. calculate payroll")
    print("8. count officers")
    print("current user: ", user)
    while True:
        choice = int(input("select option: "))
        if choice >= 1 and choice <= 8:
            return choice
            break
        else:
            print("invalid")



display_menu()