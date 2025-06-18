cpf = "xxx.xxx.xxx.xx"
peso_verify_1 = [10,9,8,7,6,5,4,3,2]
peso_verify_2 = [11,10,9,8,7,6,5,4,3,2]

cpf_use_verify_1 = cpf[:-2]
cpf_use_verify_2 = cpf[:-1]

array_in_verify_1 = [int(d) for d in str(cpf_use_verify_1)]
array_in_verify_2 = [int(d) for d in str(cpf_use_verify_2)]

multplication_array_and_peso_1 = [a * b for a, b in zip(array_in_verify_1, peso_verify_1)]
multplication_array_and_peso_2 = [a * b for a, b in zip(array_in_verify_2, peso_verify_2)]

soma_values_in_multiplication_1= 0
soma_values_in_multiplication_2 = 0


for d in multplication_array_and_peso_1:
    soma_values_in_multiplication_1+=d

for d in multplication_array_and_peso_2:
    soma_values_in_multiplication_2+=d

    
resto_1 = soma_values_in_multiplication_1 % 11
resto_2 = soma_values_in_multiplication_2 % 11


digito_verification_1 = 11 - resto_1
digito_verification_2 = 11 - resto_2


if digito_verification_1 == 11:
    verificador_1 = 0
else:
    verificador_1 = digito_verification_1

if digito_verification_2 == 11:
    verificador_2 = 0
else:
    verificador_2 = digito_verification_2


digitos_verification= str(verificador_1) + str(verificador_2)
digitos_verification_input_cpf = cpf[-2:]


if digitos_verification == digitos_verification_input_cpf:
    print("Digitos validos!! :)")
    print(f"1° Digito: {verificador_1}")
    print(f"2° Digito: {verificador_2}")
else: 
    print("Digitos invalidos!! :(")
    print(f"1° Digito (correto) : {verificador_1}")
    print(f"2° Digito (correto) : {verificador_2}")



