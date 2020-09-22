number_of_people = 10
genders=[]
ages=[]
for x in range(number_of_people):
while True:
typed_age = input("\nQual sua idade: ")
try:
ages.append(int(typed_age))
break
except:
print("Digite a idade válida")
            
while True:
typed_gender = input("Qual o seu sexo: F/M ").upper()
if typed_gender == "F" or typed_gender == "M":
genders.append(typed_gender)
break
else:
print("Digite o sexo válido")

male_index=[]
female_index=[]
counter = 0
for x in genders:
if x == "M":
male_index.append(counter)
else:
female_index.append(counter)
counter+=1

average_male_age = 0 
for x in male_index:
average_male_age += ages[x]
average_male_age = average_male_age/len(male_index)

average_female_age = 0
for x in female_index:
average_female_age += ages[x]
average_female_age = average_female_age/len(female_index)

general_average = sum(ages)/number_of_people

print("\nMédia de idade dos homens:",average_male_age)
print("Média de idade das mulheres:",average_female_age)
print("Média de idade geral:",general_average)
