##Empresa##
salário = float(input("Digite o salário: "))
cargo = input("Digite o cargo: ")

if cargo == "Programador de sistemas":
     novo_salario = salário + (salário * 0.30)
     print("Novo salário:", novo_salario)

elif cargo == "Analista de sistemas":
     novo_salario = salário + (salário * 0.20)
     print("Novo_salario:", novo_salario ) 

elif cargo == "Analista de banco de dados":
     novo_salario = salário + (salário * 0.15)
     print("Novo_salário:", novo_salario)
else:
     print("Cargo inválido")
