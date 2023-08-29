import sys

class Estoque:
    def __init__(self):
        self.rolhas = 0
        self.garrafas = 0
        self.rotulos = 0
        self.caixa = 0
        self.total_frete = 0 

    def adicionar_rolha(self, quantidade):
        self.rolhas += quantidade
        if quantidade <= 1:
            print(f"{quantidade} rolha adicionada ao estoque.")
        else:
            print(f"{quantidade} rolhas adicionados ao estoque.")

    def adicionar_garrafa(self, quantidade):
        self.garrafas += quantidade
        if quantidade <= 1:
            print(f"{quantidade} garrafa adicionada ao estoque.")
        else:
            print(f"{quantidade} garrafas adicionados ao estoque.")

    def adicionar_rotulo(self, quantidade):
        self.rotulos += quantidade
        if quantidade <= 1:
            print(f"{quantidade} rotulo adicionada ao estoque.")
        else:
            print(f"{quantidade} rotulos adicionados ao estoque.")
        
    def adicionar_caixas(self, quantidade):
        self.caixa += quantidade
        if quantidade <= 1:
            print(f"{quantidade} caixa adicionada ao estoque.")
        else:
            print(f"{quantidade} caixas adicionados ao estoque.")

    def calcular_caixas(self,quantidade):
        caixas_de_12 = quantidade // 12
        sobras_de_12 = quantidade % 12
        caixas_de_6 = sobras_de_12 // 6
        sobras_finais = sobras_de_12 % 6

        return caixas_de_12, caixas_de_6, sobras_finais
        print(f"{caixas_de_12} caixas de 12; {caixas_de_6} caixas de 6; {sobras_finais} sobras.")


    def sair_garrafa(self, quantidade):
        if self.garrafas >= quantidade:
            if self.rolhas >= quantidade:
                if self.rotulos >= quantidade:
                    caixas_de_12, caixas_de_6, sobras_finais = estoque.calcular_caixas(quantidade)
                    print(f"Separadas em {caixas_de_12} caixas de 12; {caixas_de_6} caixas de 6; e {sobras_finais} sozinhas.")
                    frete = 10+(10*quantidade)*1.10
                    if quantidade <= 1:
                        print(f"{quantidade} garrafa foi retiradas do estoque. Com frete de R${frete}")
                    else:
                        print(f"{quantidade} garrafas foram retiradas do estoque. Com frete de R${frete}")
                    self.garrafas -= quantidade
                    self.rolhas -= quantidade
                    self.rotulos -= quantidade
        else:
            if quantidade <= 1:
                print(f'Não há quantidades suficientes no estoque para formar {quantidade} garrafa.')
                estoque.mostrar_estoque()
            else:
                print(f'Não há quantidades suficientes no estoque para formar {quantidade} garrafas.')
                estoque.mostrar_estoque()


    def mostrar_estoque(self):
        print("Estoque:")
        print(f"Rolhas: {self.rolhas}")
        print(f"Garrafas: {self.garrafas}")
        print(f"Rótulos: {self.rotulos}")
        print(f"Caixas: {self.caixa}")
        

estoque = Estoque()

while True:
    print("\nOpções:")
    print("1 - Adicionar Rolhas")
    print("2 - Adicionar Garrafas")
    print("3 - Adicionar Rótulos")
    print("4 - Adicionar Caixas")
    print("5 - Retirar Garrafas")
    print("6 - Mostrar Estoque")
    print("7 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        quantidade = int(input("Digite a quantidade de rolhas a ser adicionada: "))
        estoque.adicionar_rolha(quantidade)
    elif opcao == 2:
        quantidade = int(input("Digite a quantidade de garrafas a ser adicionada: "))
        estoque.adicionar_garrafa(quantidade)
    elif opcao == 3:
        quantidade = int(input("Digite a quantidade de rótulos a ser adicionada: "))
        estoque.adicionar_rotulo(quantidade)
    elif opcao == 4:
        quantidade = int(input("Digite a quantidade de caixas ser adicionada: "))
        estoque.adicionar_caixas(quantidade)
    elif opcao == 5:
        quantidade = int(input("Digite a quantidade de garrafas a serem retiradas: "))
        estoque.sair_garrafa(quantidade)
    elif opcao == 6:
        estoque.mostrar_estoque()
    elif opcao == 7:
        print("Saindo do programa.")
        sys.exit()
    else:
        print("Opção inválida. Escolha novamente.")
        
    