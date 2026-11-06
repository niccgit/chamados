import sqlite3

DB_NAME = "chamados.db"

def conexao_banco():

    conexao = sqlite3.connect(DB_NAME)
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS chamados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        prioridade TEXT NOT NULL,
        status TEXT NOT NULL,
        usuario TEXT NOT NULL
    )
    """
    cursor.execute(sql)
    conexao.commit()
    return conexao

def popular_banco_inicial():

    conexao = conexao_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM chamados")
    total = cursor.fetchone()[0]
    if total == 0:
        chamados_pre_existentes = [
            ("Erro no login", "Alta", "Aberto", "Ana Silva"),
            ("Tela branca no app", "Crítica", "Aberto", "Bruno Costa"),
            ("Atualizar cadastro", "Baixa", "Em progresso", "Carlos Souza"),
            ("Boleto não gerado", "Média", "Aberto", "Daniela Lima"),
            ("Botão quebrado", "Baixa", "Aberto", "Eduardo Rocha"),
            ("Lentidão na busca", "Média", "Em progresso", "Fernanda Alves"),
            ("Recuperar senha", "Alta", "Aberto", "Gabriel Santos"),
            ("Erro no Pix", "Crítica", "Aberto", "Amanda Melo"),
            ("Mudar foto de perfil", "Baixa", "Fechado", "Igor Ribeiro"),
            ("Exportar PDF falhou", "Média", "Aberto", "Juliana Vieira"),
            ("Carrinho esvaziando", "Alta", "Em progresso", "Lucas Martins"),
            ("Cupom inválido", "Média", "Aberto", "Mariana Dias"),
            ("Página 404 no FAQ", "Baixa", "Aberto", "Nicolas Ferreira"),
            ("Atraso na entrega", "Alta", "Aberto", "Patricia Gomes"),
            ("Email de boas-vindas", "Baixa", "Fechado", "Rodrigo Ramos"),
            ("Estorno pendente", "Alta", "Em progresso", "Sabrina Oliveira"),
            ("Alerta de segurança", "Crítica", "Aberto", "Thiago Barbosa"),
            ("Link quebrado no menu", "Baixa", "Aberto", "Vanessa Cunha"),
            ("Nota fiscal sumiu", "Média", "Aberto", "Willian Cardoso"),
            ("Modo escuro travando", "Baixa", "Em progresso", "Yasmim Lopes"),
            ("Erro na API de CEP", "Alta", "Aberto", "Arthur Antunes"),
            ("Notificação duplicada", "Baixa", "Aberto", "Beatriz Mendes"),
            ("Sessão expirando rápido", "Média", "Em progresso", "Caio Nogueira"),
            ("Erro no cartão de crédito", "Crítica", "Aberto", "Diana Prince"),
            ("Traduzir termo em inglês", "Baixa", "Fechado", "Elton John"),
            ("Chat de suporte offline", "Alta", "Aberto", "Fábio Assunção"),
            ("Upload de comprovante", "Média", "Aberto", "Gisele Bündchen"),
            ("Histórico sumiu", "Alta", "Em progresso", "Heitor Villa"),
            ("Termos de uso desatualizados", "Baixa", "Aberto", "Isabela Garcia"),
            ("Erro 500 no checkout", "Crítica", "Aberto", "Jorge Ben"),
            ("Ajustar margem do header", "Baixa", "Em progresso", "Karina Bacchi"),
            ("Filtro por data quebrado", "Média", "Aberto", "Leonardo Dicaprio"),
            ("Assinatura não renovada", "Alta", "Aberto", "Marta Vieira"),
            ("Áudio do vídeo não funciona", "Média", "Aberto", "Neymar Junior"),
            ("Atualizar política de privacidade", "Baixa", "Fechado", "Otávio Mesquita"),
            ("Queda do servidor interno", "Crítica", "Em progresso", "Paula Toller"),
            ("Convite por email falhou", "Baixa", "Aberto", "Quintino Aires"),
            ("Extrato em branco", "Alta", "Aberto", "Renata Vasconcellos"),
            ("Ícone errado no painel", "Baixa", "Aberto", "Samuel Rosa"),
            ("Duplicidade de cobrança", "Crítica", "Aberto", "Tais Araújo"),
            ("Validação de CNPJ", "Média", "Em progresso", "Umberto Eco"),
            ("Mensagem de erro confusa", "Baixa", "Aberto", "Valéria Valenssa"),
            ("Problema com fonte negrito", "Baixa", "Aberto", "Wagner Moura"),
            ("Links de redes sociais fora do ar", "Média", "Aberto", "Xuxa Meneghel"),
            ("Sem sinal de geolocalização", "Alta", "Em progresso", "Yuri Gagarin"),
            ("Página recarregando sozinha", "Alta", "Aberto", "Zeca Pagodinho"),
            ("Gráfico de vendas travado", "Média", "Aberto", "Alinne Moraes"),
            ("Impossível remover endereço", "Média", "Em progresso", "Beto Jamaica"),
            ("Vazamento de memória na aba", "Crítica", "Aberto", "Cláudia Raia"),
            ("Ajustar alinhamento do rodapé", "Baixa", "Fechado", "Dado Dolabella"),
        ]
        cursor.executemany(
            "INSERT INTO chamados (titulo, prioridade, status, usuario) VALUES (?, ?, ?, ?)",
            chamados_pre_existentes
        )
        conexao.commit()
    conexao.close()



def filtrar_por_usuario():

    conexao = conexao_banco()
    cursor = conexao.cursor()

    nome = input("Digite o nome do usuário: ").strip()

    cursor.execute(
        "SELECT * FROM chamados WHERE usuario = ? ORDER BY id",
        (nome,)
    )

    buscas = cursor.fetchall()
    if len(buscas) == 0:
        print("Nenhum chamado encontrado para esse usuário.")
    else:
        for item in buscas:
            print(
                f"ID: {item['id']} | Título: {item['titulo']} | "
                f"Prioridade: {item['prioridade']} | Status: {item['status']} | "
                f"Usuário: {item['usuario']}"
            )

    conexao.close()



def filtrar_por_status():

    conexao = conexao_banco()
    cursor = conexao.cursor()

    status = input("Digite o status (Aberto/Em progresso/Fechado): ").strip()

    cursor.execute(
        "SELECT * FROM chamados WHERE status = ? ORDER BY id",
        (status,)
    )

    buscas = cursor.fetchall()

    if len(buscas) == 0:
        print("Nenhum chamado com esse status.")
    else:
        for item in buscas:
            print(
                f"ID: {item['id']} | Título: {item['titulo']} | "
                f"Prioridade: {item['prioridade']} | Status: {item['status']} | "
                f"Usuário: {item['usuario']}"
            )

    conexao.close()



def filtrar_por_prioridade():

    conexao = conexao_banco()
    cursor = conexao.cursor()

    prioridade = input("Digite a prioridade (Crítica/Alta/Média/Baixa): ").strip()

    cursor.execute(
        "SELECT * FROM chamados WHERE prioridade = ? ORDER BY id",
        (prioridade,)
    )

    buscas = cursor.fetchall()

    if len(buscas) == 0:
        print("Nenhum chamado com essa prioridade.")
    else:
        for item in buscas:
            print(
                f"ID: {item['id']} | Título: {item['titulo']} | "
                f"Prioridade: {item['prioridade']} | Status: {item['status']} | "
                f"Usuário: {item['usuario']}"
            )

    conexao.close()



def filtrar_chamados_urgentes():

    conexao = conexao_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM chamados WHERE prioridade = 'Crítica' AND status = 'Aberto' ORDER BY id"
    )

    buscas = cursor.fetchall()

    if len(buscas) == 0:
        print("Não há chamados urgentes abertos.")
    else:
        for item in buscas:
            print(
                f"ID: {item['id']} | Título: {item['titulo']} | "
                f"Prioridade: {item['prioridade']} | Status: {item['status']} | "
                f"Usuário: {item['usuario']}"
            )

    conexao.close()



def cadastrar_chamado():

    opcoes = ["Crítica", "Alta", "Média", "Baixa"]

    novo_titulo = input("Digite o título do novo chamado: ").strip()
    nova_prioridade = input("Digite a prioridade do novo chamado (Crítica/Alta/Média/Baixa): ").strip()
    novo_usuario = input("Digite o nome do usuário: ").strip()

    if not novo_titulo or not nova_prioridade or not novo_usuario:
        print("Todos os campos são de preenchimento obrigatório.")
        return

    if nova_prioridade not in opcoes:
        print("Prioridade inválida! Responda somente com 'Crítica', 'Alta', 'Média' ou 'Baixa'.")
        return

    conexao = conexao_banco()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO chamados (titulo, prioridade, status, usuario)
        VALUES (?, ?, ?, ?)
        """,
        (novo_titulo, nova_prioridade, "Aberto", novo_usuario)
    )

    conexao.commit()
    conexao.close()

    print("Novo chamado cadastrado com sucesso!")



def resolver_chamado():

    id_buscado = input("Digite o ID do chamado que deseja alterar para 'Em progresso': ").strip()

    conexao = conexao_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE chamados SET status = ? WHERE id = ?",
        ("Em progresso", id_buscado)
    )

    if cursor.rowcount == 0:
        print("Nenhum chamado encontrado com esse ID.")
    else:
        print("Status atualizado para 'Em progresso' com sucesso!")

    conexao.commit()
    conexao.close()



def fechar_chamado():

    id_buscado = input("Digite o ID do chamado que deseja alterar para 'Fechado': ").strip()

    conexao = conexao_banco()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE chamados SET status = ? WHERE id = ?",
        ("Fechado", id_buscado)
    )

    if cursor.rowcount == 0:
        print("Nenhum chamado encontrado com esse ID.")
    else:
        print("Status atualizado para 'Fechado' com sucesso!")

    conexao.commit()
    conexao.close()



def menu():

    print("Bem-vindo ao sistema de Chamados!")

    while True:
        print("\n01 - Filtrar chamados por usuário")
        print("02 - Filtrar chamados por status")
        print("03 - Filtrar chamados por prioridade")
        print("04 - Filtrar chamados urgentes (Prioridade = Crítica e Status = Aberto)")
        print("05 - Cadastrar novo chamado")
        print("06 - Resolver chamado")
        print("07 - Fechar chamado")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "01":
            filtrar_por_usuario()
        elif opcao == "02":
            filtrar_por_status()
        elif opcao == "03":
            filtrar_por_prioridade()
        elif opcao == "04":
            filtrar_chamados_urgentes()
        elif opcao == "05":
            cadastrar_chamado()
        elif opcao == "06":
            resolver_chamado()
        elif opcao == "07":
            fechar_chamado()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == "__main__":
    popular_banco_inicial()
    menu()
