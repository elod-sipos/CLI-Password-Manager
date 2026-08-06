import getpass
from cli import home_menu, prompt_add, prompt_get
from crypto import derive_key, generate_salt
from vault import add_entry, get_entry, get_or_create_salt


def main():
    try: 
        master_password = getpass.getpass("Enter master password: ")
        salt = get_or_create_salt()
        key = derive_key(master_password, salt)

        while True:
            choice = home_menu()

            if choice.lower() == "g":
                service = prompt_get()
                entry = get_entry(service, key)
                if entry:
                    print(f"Service: {service}\n Password: {entry}")
                else:
                    print(f"No entry found for {service}")
            
            elif choice.lower() == "c":
                service, password = prompt_add()
                add_entry(service, password, key)
                print(f"Saved password for {service}")

            elif choice.lower() == "q":
                break
            
            else:
                print("Invalid option")
        
    except (KeyboardInterrupt, EOFError):
        print("Exiting..")

if __name__ == "__main__":
    main()
