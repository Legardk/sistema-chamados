chamados = []

from lib import *

def exibir_menu():
    try:
        print("\n*** Sistema de Chamados ***")
        print("1. Cadastrar novo chamado")
        print("2. Buscar chamado por ID ou descrição")
        print("3. Remover chamados finalizados")
        print("4. Listar chamados por prioridade")
        print("5. Exibir estatísticas dos chamados")
        print("6. Limpar lista de chamados")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        return opcao
    except Exception as e:
        print(f"Erro ao exibir o menu: {e}")
        return None

def main():
    while True:
        try:
            opcao = exibir_menu()
            if opcao is None:
                continue

            if opcao == "1":
                try:
                    id_chamado = int(input("Digite o ID do chamado: "))
                    descricao = input("Digite a descrição do chamado: ")
                    prioridade = int(input("Digite a prioridade (1-3, sendo 1 a mais alta): "))
                    cadastrar_chamado(id_chamado, descricao, prioridade)
                except ValueError:
                    print("Erro: ID e prioridade devem ser números inteiros.")
                except Exception as e:
                    print(f"Erro inesperado: {e}")

            elif opcao == "2":
                busca = input("Buscar por ID ou descrição? (Digite 'ID' ou 'Descrição'): ").strip().lower()
                if busca == "id":
                    try:
                        id_chamado = int(input("Digite o ID do chamado: "))
                        buscar_chamado(id_chamado=id_chamado)
                    except ValueError:
                        print("Erro: O ID deve ser um número inteiro.")
                elif busca == "descrição":
                    descricao = input("Digite a descrição do chamado: ")
                    buscar_chamado(descricao=descricao)
                else:
                    print("Opção inválida.")

            elif opcao == "3":
                remover_chamados_finalizados()

            elif opcao == "4":
                listar_chamados_por_prioridade()

            elif opcao == "5":
                exibir_estatisticas()

            elif opcao == "6":
                limpar_lista_chamados()

            elif opcao == "0":
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida, tente novamente.")

        except Exception as e:
            print(f"Erro inesperado no programa: {e}")

if __name__ == "__main__":
    main()
