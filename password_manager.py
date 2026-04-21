import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    with open(filename, "r") as H: password = H.read().strip()
    encr_pass = caesar_encrypt(password)
    with open(filename, "w") as H:
        H.write(encr_pass)
    pass


def encrypt_passwords_in_file(filename: str) -> None:
    filas_actualizadas = []
    
    with open(filename, "r", encoding="utf-8") as f:
        lector = csv.reader(f)
        encabezado = next(lector, None)
        if encabezado:
            filas_actualizadas.append(encabezado)
        for fila in lector:
            if len(fila) >= 3:
                fila[2] = caesar_encrypt(fila[2])
                filas_actualizadas.append(fila)
                
    with open(filename, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerows(filas_actualizadas)
    pass


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
