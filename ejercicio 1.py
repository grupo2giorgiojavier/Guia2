vara=input("Escriba la primera variable")
varb=input("Escriba la segunda variable")

if vara.isdigit():
    if varb.isdigit():
        if vara>varb:
            print("La primera variable es mayor que la segunda ")
        elif vara<varb:
            print("La segunda variable es mayor que la primera ") 
        elif vara==varb:
            print("Las 2 variables son iguales")
    else:
         print("La primera variable es un digito")
         print("La segunda variable es una string")

else:
    print("La primera variable es una string")
    if varb.isdigit():
        print("La segunda variable es un digito")
    else:
        print("La segunda variable es una string")