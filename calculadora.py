#Joao Pedro L. Affonso
#####    

def main():
    import math;

    opcao = input("O que você quer? \n -> Digite 1 para cos^(-1) \n -> Digite 2 para sen^(-1) \nDigite aqui:");

    if opcao == "1":
        x = float(input("Digite o angulo: "));
        y = 180*(math.acos(x)/math.pi);
        print("O cos^(-1) de " + str(x) + " é: " + str(y));

    elif opcao == "2":
        x = float(input("Digite o angulo: "));
        y = 180*(math.asin(x)/math.pi);
        print("O sen^(-1) de " + str(x) + " é: " + str(y));

if __name__ == '__main__':
    main()
