
def main():
    names, ranks, divisions, IDs = init_database()
    choice = display_menu()
    if choice == 1:
        add_member(names, ranks, divisions, IDs)
    elif choice == 2:
        remove_member(names, ranks, divisions, IDs)
    elif choice == 3:
        update_rank(names, ranks, IDs)
    elif choice == 4:
        display_roster(names, ranks, divisions, IDs)
    elif choice == 5:
        search_crew(names, ranks, divisions, IDs)
    elif choice == 6:
        filter_by_division(names, divisions)
    elif choice == 7:
        calculate_payroll(ranks)
    elif choice == 8:
        count_officers(ranks)
        

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

def display_roster(names, ranks, divisions, IDs):
    for i in range(len(names)):
        print(names[i], ranks[i], divisions[i], IDs[i])

def search_crew(names, ranks, divisions, IDs):
    term = input("enter search term ")
    res = zip(names, ranks, divisions, IDs)
    res = list(res)
    for i in range(0, 4):
        filter = [item for item in res if item[i] == term]
        print(filter)

    
def filter_by_division(names, divisions):
    term = input("filter by Command, Oprations, Sciences ")
    res = zip(names, ranks, divisions, IDs)
    for i in range(0, 4):
        filter = [item for item in res if item[2] == term]
        print(filter)

def calculate_payroll(ranks):
    total = 0
    for rank in ranks:
        if rank == "Captain":
            total = total + 1000
        elif rank == "Commander":
            total = total + 800
        elif rank == "Lieutenant":
            total = total + 600
        elif rank == "ensign":
            total = total + 200
    print(total)

def count_officers(ranks):
    total = 0
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            total = total + 1
    print(total)

        

main()


