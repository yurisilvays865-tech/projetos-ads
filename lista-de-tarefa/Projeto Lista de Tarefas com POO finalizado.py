class Tarefa:
    def __init__(self,titulo,descricao):
        self.titulo=titulo
        self.descricao=descricao
        self.concluida=False

    def get_titulo(self):
        return self.titulo
    
    def get_descricao(self):
        return self.descricao
    
    def get_concluida(self):
        return self.concluida
    
    def concluir(self):
        self.concluida=True

    def exibir(self):
        status= "concluida" if self.concluida else "pendente"

        print(f"titulo: {self.titulo}")
        print(f"descrição: {self.descricao}")
        print(f"status: {status}\n")

class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def exibir_tarefas(self):
        if not self.tarefas:
            print("nenhuma tarefa cadastrada.\n")
        else:
            print("----lista de tarefas----")
            for i, tarefa in enumerate(self.tarefas):
                print(f"{i + 1}.{tarefa.titulo} - {'concluida' if tarefa.concluida else 'pendente'}")
                tarefa.exibir()
    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
            print(f"Tarefa '{self.tarefas[indice].titulo}' marcada como concluida!\n")
        else:
            print("indice invalido:\n")
    def ordenar_por_prioridade(self):
        prioridades = {"alta": 3,"media":  2,"baixa":1}

        self.tarefas.sort(key=lambda t:prioridades.get(getattr(t, "prioridade",""), 0),reverse=True)
        print("tarefas ordenadas por prioridade!\n")

    def filtrar_tarefas(self, tipo):
        if not self.tarefas:
            print("nenhuma tarefa cadastrada.\n")
            return
        print(f"---- tarefas {tipo} ----")
        encontrou = False

        for tarefa in self.tarefas:
            if tipo == "concluidas" and tarefa.concluida:
                tarefa.exibir()
                encontrou = True
            elif tipo == "pendentes" and not tarefa.concluida:
                tarefa.exibir()
                encontrou = True
            elif tipo == "prioritarias" and hasattr(tarefa, "prioridade"):
                tarefa.exibir()
                encontrou = True

        if not encontrou:
            print("nenhuma tarefa encontrada para esta filtro.\n")

class TarefaPrioritaria(Tarefa):
    def __init__(self, titulo, descricao,prioridade):
        super().__init__(titulo, descricao)
        self.prioridade = prioridade

    def exibir(self):
        status = "concluida" if self.concluida else "pendente"
        print(f"titulo: {self.titulo}")
        print(f"descriçao: {self.descricao}")
        print(f"prioridade: {self.prioridade}")
        print(f"status: {status}\n")

if __name__ == "__main__":
    
    lista = ListaDeTarefas()

    t1 = Tarefa("lavar o carro","lavar e encerar o carro da garagem")
    t2 = TarefaPrioritaria("reunião da equipe","reunião sobre o novo projeto","alta")

    
    t3 = TarefaPrioritaria("enviar relatório", "Enviar o relatório mensal","media")
    t4 = TarefaPrioritaria("Atualizar antivirus", "Atualizar o software de segurança", "baixa")

    lista.adicionar_tarefa(t3)
    lista.adicionar_tarefa(t4)
    lista.adicionar_tarefa(t1)
    lista.adicionar_tarefa(t2)

    lista.exibir_tarefas()

    lista.ordenar_por_prioridade()

    lista.exibir_tarefas()

    t1.concluir()
    t2.concluir()

    print(">>> Tarefas concluídas:")
    lista.filtrar_tarefas("concluidas")

    print(">>> Tarefas pendentes:")
    lista.filtrar_tarefas("pendentes")

    print(">>> Tarefas prioritárias:")
    lista.filtrar_tarefas("prioritarias")
    

    