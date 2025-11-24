# 📝 Lista de Tarefas (POO em Python)

Este é um projeto desenvolvido para praticar **Programação Orientada a Objetos (POO)** em Python, com foco em **herança**, **sobrescrita de métodos** e **organização de código**.

---

## 🚀 Funcionalidades

- Adicionar novas tarefas
- Concluir tarefas
- Exibir todas as tarefas com status (pendente/concluída)
- Criar tarefas com diferentes níveis de **prioridade**
- Filtrar tarefas (concluídas, pendentes, prioritárias)
- Ordenar tarefas por prioridade (Alta → Média → Baixa)

---

## 🧠 Conceitos de POO aplicados

- **Classe base (`Tarefa`)** com atributos e métodos comuns  
- **Herança:** classe `TarefaPrioritaria` deriva de `Tarefa`  
- **Sobrescrita de método (`exibir`)** para personalizar a saída  
- **Encapsulamento** com métodos getters  
- **Composição:** classe `ListaDeTarefas` gerencia várias instâncias de `Tarefa`

---

## 🖥️ Exemplo de uso

```python
t1 = Tarefa("Lavar o carro", "Lavar e encerar o carro da garagem")
t2 = TarefaPrioritaria("Reunião da equipe", "Reunião sobre o novo projeto", "alta")

lista = ListaDeTarefas()
lista.adicionar_tarefa(t1)
lista.adicionar_tarefa(t2)

lista.exibir_tarefas()


Saída esperada:

----lista de tarefas----
1. Lavar o carro - pendente
2. Reunião da equipe - pendente


🧩 Tecnologias utilizadas

Python 3.12

Programação Orientada a Objetos (POO)

Execução via terminal (CLI)

📁 Estrutura do projeto
lista-de-tarefas/
│
├── tarefa.py
├── lista_de_tarefas.py
├── main.py
└── README.md


(ou apenas um arquivo único, se estiver tudo no mesmo .py)

👨‍💻 Autor

Desenvolvido por Yuri Magalhães – estudante de Análise e Desenvolvimento de Sistemas.


🏁 Status do projeto

✅ Finalizado e funcional


