
def main():
    names, ranks, divisions, IDs = init_database()
    choice = display_menu()
    if choice == 1:
        add_member(names, ranks, divisions, IDs)
    elif choice == 2:
        remove_member(names, ranks, divisions, IDs)
    elif choice == 3:
        update_rank(names, ranks, IDs)
        

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

def add_member(names, ranks, divisions, IDs):
    valid_ranks = ["Captain", "Lieutenant", "Ensign", "Commander"]
    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_divison = input("Division: ")
    new_ID = input("ID: ")
    while True:
        if new_ID in IDs:
            print("ID already exists")
            new_ID = input("enter another ID: ")
        elif new_rank not in ranks:
            print("invalid rank")
            new_rank = input("enter rank: ")
        else:
            names.append(new_name)
            ranks.append(new_rank)
            divisions.append(new_divison)
            IDs.append(new_ID)
            return names, ranks, divisions, IDs
            break

def remove_member(names, ranks, divisions, IDs):
    index = int(input("select the ID of the person to remove: "))
    names.pop(index)
    ranks.pop(index)
    divisions.pop(index)
    IDs.pop(index)
    print(names, ranks, divisions, IDs)

def update_rank(names, ranks, IDs):
    n = int(input("whats the members ID?: "))
    ranks[n - 1] = input("whats their rank?: ")
    print(names, ranks, IDs)



main()


