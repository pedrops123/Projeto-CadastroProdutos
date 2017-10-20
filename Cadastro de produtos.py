

def CadastroProdutos(armazem):
    
    print(" -- Cadastrar produtos -- \n ")
    
    per = 1
    
    
    while(per == 1):
        
        
        prod = str(input("Digite o nome do produto: \n "))
    
        prec = str(input("Digite o preço do produto: \n "))

        armazem.update({prod:prec})

        print("Parabéns! Produto cadastrado com suceso! \n ")

        per = int(input("Deseja continuar cadastrando ? 1 -  Sim 2 - Nao \n "))
        
        if (type(per) is not int or per == ""):
            
            while(type(per) is not int or per == ""):
                
                
                print("Tipo de dado incorreto favor colocar somente numeros \n ")

                per = int(input("Deseja continuar cadastrando ? 1 -  Sim 2 - Nao \n "))
                    
        if (per == 2):
                                
            for i in range (1,20):
                    
                print("\n")

                



def CadastroPreco(armazem):
            
    print(" -- Cadastrar Preço -- \n ")
    
    volt = 1
    
    while(volt == 1):
        
        prod = str(input("Digite o nome do produto: \n "))
               
        if (prod not in  armazem):
        
            print("Produto nao encontrado")
        
            main()
             

        prec = int(input("Digite o preço : \n "))

        if(type(prec) is not int or prec == ""):
            
            while(type(prec) is not int or prec == ""):

                print("Entrada de Preço invalido , favor digitar novamente \n ")
                
                prec = int(input("Digite o preço : \n "))

    
        if (prod not in  armazem):
            
                print("Seu produto ", prod , "ficara com o preço" , prec, "\n")
            
                resp = int(input("Tem certeza que deseja alterar o preço do produto? 1 - sim 2 - nao \n "))

                if(type(resp) is not int or resp == ""):
                    
                    while(type(resp) is not int or resp == ""):

                        print("Entrada de resposta invalida , favor digitar novamente \n ")
                        
                        resp = int(input("Tem certeza que deseja alterar o preço do produto? 1 - sim 2 - nao \n"))
                    
        
        if (resp == 1):
        
            armazem.update({prod:prec})
        
            print("Preço cadastrado com sucesso no produto ",prod,"\n")
        
        else:
        
            print("Preço de produto nao alterado! O valor continuara como antes \n  ")

        volt = int(input("Deseja alterar mais algum preço? 1- sim 2- nao \n "))

        if(type(volt) is not int or volt == ""):
            
            while(type(volt) is not int or volt == ""):
            
                print("Entrada invalida , favor digitar novamente: \n")
                
                volt = int(input("Deseja alterar mais algum preço? 1- sim 2- nao \n "))
                
            

        if(volt == 2):
                        
            for i in range (1,20):
                    
                print("\n")
                main()
                

            


def ExclusaoProduto(armazem):

    print(" -- Excluir  produto  -- \n ")

    pd = str(input("Digite o nome do produto: \n "))

    if (pd not in  armazem):

        print("Produto não cadastrado!! \n")

        main()
    

    

    
    




armazem  = {}

def main():
    
    
    print("----- Cadastro de Produtos ----- \n")

    

    res = 1

    while (res != 6):
            
        print("1 - Cadastrar produto \n ")

        print("2 - Cadastrar Preço \n")

        print("3 - Excluir  produto \n ")

        print("4 - Excluir  Preço \n ")

        print("5 - visualizar  \n ")

        print("6 - sair  \n ")

        res = int(input("Por gentileza digitar sua opção: \n "))

        if(res == 1):
        
            CadastroProdutos(armazem)   
               
        if(res == 2):
        
            CadastroPreco(armazem)

        if(res == 3):
            
            ExclusaoProduto(armazem)
    
            

        if(res == 4):
    
            print(" -- Excluir  Preço -- \n ")

        if(res == 5):
    
            print(" -- visualizar -- \n ")

            print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- \n")
            
            print("Os produtos cadastrados ate agora foram: \n ")
        
            for prod , prec in armazem.items():
                         
                print("Nome do produto :" , prod , "Preço: R$" ,prec, "\n")
                print("\n")
                

            print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- \n")

        
            

        if(res == 6):
        
            print(" Voce saiu!  \n ")



if(__name__ == '__main__'):
    
    main()
