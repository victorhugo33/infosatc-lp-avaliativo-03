print("\n")
print("      @                           @@@")
print("     @ @          Centro          @@@")
print("    @   @                     @@@@@@@@@@@")
print("   @  @@@@          de        @@@@@@@@@@@")
print("   @@@@@@@                        @@@")
print("    @@@@@       Hematologia       @@@")

counter=0
while counter<5:
while True:
typed_age = input("\nQual sua idade: ")
typed_weight = input("Qual seu peso: ").replace(",",".")
sleep_time = input("Você dormiu pelo menos 6 horas nas últimas 24 horas: s/n ")
try:
age = int(typed_age)
weight = float(typed_weight)
if sleep_time == "s" or sleep_time == "n":
break
else:
print("Digite valores válidos")
except:
print("Digite valores válidos")

unmet_requirements = []

if age>69 or age<16:
unmet_requirements.append("Idade")    

if weight<50:
unmet_requirements.append("Peso")    

if sleep_time=="n":
unmet_requirements.append("Não dormiu ao menos de 6 horas nas últimas 24 horas") 
can_be_donor = "Não"
else:
can_be_donor = "Sim"

if len(unmet_requirements)>0:
print("\nOs requisitos que não foram atendidos são:")
for i in unmet_requirements:
print(i)
else:
print("Você pode ser um doador")


while True:
want_to_register = input("\nVocê gostaria de se cadastrar no laboratório: s/n ")
if want_to_register == "s" or want_to_register == "n":
break
else:
print("Digite valores válidos")

if want_to_register=="s":
full_name = input("Qual seu nome completo: ")
cpf = input("Qual seu CPF: ")
password = input("Qual será sua senha: ")

if counter==0:
 person_1={
"Nome Completo":full_name,
"CPF":cpf,
"Senha":password,
"Está apto para ser doador":can_be_donor,
}
elif counter==1:
person_2={
"Nome Completo":full_name,
"CPF":cpf,
"Senha":password,
"Está apto para ser doador":can_be_donor,
}
elif counter==2:
person_3={
"Nome Completo":full_name,
"CPF":cpf,
"Senha":password,
"Está apto para ser doador"
:can_be_donor,
}
elif counter==3:
person_4={
"Nome Completo":full_name,
"CPF":cpf,
"Senha":password,
"Está apto para ser doador":can_be_donor,
}
else:
person_5={
"Nome Completo":full_name,
"CPF":cpf,
"Senha":password,
"Está apto para ser doador":can_be_donor,
}

counter+=1

print("\nPessoa 1: ")
for x in person_1:
print(f"{x}: {person_1[x]}")

print("\nPessoa 2: ")
for x in person_2:
print(f"{x}: {person_2[x]}")

print("\nPessoa 3: ")
for x in person_3:
print(f"{x}: {person_3[x]}")

print("\nPessoa 4: ")
for x in person_4:
print(f"{x}: {person_4[x]}")

print("\nPessoa 5: ")
for x in person_5:
print(f"{x}: {person_5[x]}")
