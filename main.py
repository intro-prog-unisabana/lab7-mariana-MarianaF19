from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
 filename = input("Enter the CSV file name: ")
encrypt_passwords_in_file(filename)
while True:
        # 2. Mostrar el menú de opciones
        print("Options: (1) Change Password, (2) Add Password, (3) Quit: ", end="")
        option = input()
        if option == "1":
            datos = input("Enter the website and the new password: ").split()
            
pass


if __name__ == "__main__":
    main()
