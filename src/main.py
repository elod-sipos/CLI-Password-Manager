from cli import home_menu, prompt_add, prompt_get
from vault import add_entry, get_entry

def main():
    while True:
        choice = home_menu()

        if choice.lower() == "g":
            service = prompt_get()
            entry = get_entry(service)
            if entry:
                print(f"Service: {service}\n Password: {entry['password']}")
            else:
                print(f"No entry found for {service}")
        
        elif choice.lower() == "c":
            service, password = prompt_add()
            add_entry(service, password)
            print(f"Saved password for {service}")

        elif choice.lower() == "q":
            break
        
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
