months = {
    1:"janeiro",
    2:"fevereiro",
    3:"março",
    4:"abril",
    5:"maio",
    6:"junho",
    7:"julho",
    8:"agosto",
    9:"setembro",
    10:"outubro",
    11:"novembro",
    12:"dezembro",
}
while True:
    typed_number = input("\nDigite um número de um a doze, será demonstrado o mês correspondente ao numero escrito: ")
    try:
        number = int(typed_number)
        if number in months:
            access = months.get(number)
            print("O mês é", access)
            break
        else: 
            print("não foi digitado um numero entre um e doze")
            continue
    except:
        print("não foi digitado um numero entre um e doze"")
