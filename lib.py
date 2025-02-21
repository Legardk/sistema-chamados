def cadastrar_chamado(id_chamado, descricao, prioridade):
    try:
        if not isinstance(id_chamado, int) or not isinstance(prioridade, int):
            raise ValueError("ID e Prioridade devem ser inteiros.")
        if prioridade not in [1, 2, 3]:
            raise ValueError("Prioridade deve ser 1 (alta), 2 (média) ou 3 (baixa).")
        chamado = {
            "id": id_chamado,
            "descricao": descricao,
            "prioridade": prioridade,
            "status": "Aberto"
        }
        chamados.append(chamado)
        print(f"Chamado {id_chamado} cadastrado com sucesso!")
    except ValueError as e:
        print(f"Erro ao cadastrar chamado: {e}")

def buscar_chamado(id_chamado=None, descricao=None):
    try:
        resultados = []
        if id_chamado:
            if not isinstance(id_chamado, int):
                raise ValueError("ID do chamado deve ser um número inteiro.")
            for chamado in chamados:
                if chamado["id"] == id_chamado:
                    resultados.append(chamado)
        elif descricao:
            if not isinstance(descricao, str):
                raise ValueError("Descrição deve ser uma string.")
            for chamado in chamados:
                if descricao.lower() in chamado["descricao"].lower():
                    resultados.append(chamado)

        if resultados:
            for resultado in resultados:
                print(f"ID: {resultado['id']}, Descrição: {resultado['descricao']}, Prioridade: {resultado['prioridade']}, Status: {resultado['status']}")
        else:
            print("Nenhum chamado encontrado.")
    except ValueError as e:
        print(f"Erro na busca de chamados: {e}")

def remover_chamados_finalizados():
    try:
        global chamados
        chamados = [chamado for chamado in chamados if chamado["status"] != "Finalizado"]
        print("Chamados finalizados removidos com sucesso!")
    except Exception as e:
        print(f"Erro ao remover chamados finalizados: {e}")

def listar_chamados_por_prioridade():
    try:
        chamados_ordenados = sorted(chamados, key=lambda x: x["prioridade"], reverse=True)
        if chamados_ordenados:
            for chamado in chamados_ordenados:
                print(f"ID: {chamado['id']}, Descrição: {chamado['descricao']}, Prioridade: {chamado['prioridade']}, Status: {chamado['status']}")
        else:
            print("Nenhum chamado para listar.")
    except Exception as e:
        print(f"Erro ao listar chamados por prioridade: {e}")

def exibir_estatisticas():
    try:
        total_chamados = len(chamados)
        chamados_abertos = sum(1 for chamado in chamados if chamado["status"] == "Aberto")
        chamados_finalizados = total_chamados - chamados_abertos
        print(f"Total de chamados: {total_chamados}")
        print(f"Chamados abertos: {chamados_abertos}")
        print(f"Chamados finalizados: {chamados_finalizados}")
    except Exception as e:
        print(f"Erro ao exibir estatísticas: {e}")

def limpar_lista_chamados():
    try:
        global chamados
        chamados = []
        print("Lista de chamados limpa com sucesso!")
    except Exception as e:
        print(f"Erro ao limpar lista de chamados: {e}")

