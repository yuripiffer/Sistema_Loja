import areaCliente
import areaConsulta


opcao = "0"
while opcao != "4":
    opcao = input("\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
                      "  Bem vinddo a loja da dona maria !!\n"
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
        pass
    elif opcao == "3":
        areaConsulta.area_Consulta()
    elif opcao == "4":
        print("Encerrando sessão ...")
