import areaCliente
import areaConsulta
import areaProduto

while True:
    opcao = input("\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
                  "  Bem vindo a loja da dona maria !!\n"
                  " -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
                  " Opções:\n"
                  "1 -> Clientes:\n"
                  "2 -> Produtos:\n"
                  "3 -> Consultas:\n"
                  "4 -> Sair\n"
                  " Opção: ")
    if opcao == "1":
        areaCliente.area_Cliente()
    elif opcao == "2":
        areaProduto.area_Produto()
    elif opcao == "3":
        areaConsulta.area_Consulta()
    elif opcao == "4":
        print("Encerrando sessão ...")
        break
