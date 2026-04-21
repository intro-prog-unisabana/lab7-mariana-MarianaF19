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
            if len(datos) < 2:
                print("Input is in the wrong format!")
            elif len(datos[1]) < 12:
                print("Password is too short!")
            else:
                website = datos[0] 
                nueva_pass = datos[1]
                if change_password(filename, website, nueva_pass):
                    print("Password changed.")

pass


if __name__ == "__main__":
    main()
