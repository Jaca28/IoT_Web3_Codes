from app import transaction

nit= input("Ingrese el NIT del proveedor: ")
calf=input("Ingrese una calificación para el proveedor de 1 a 5: ")
comen=input("Ingrese un comentario para el proveedor: ")

transaction(nit, calf, comen)