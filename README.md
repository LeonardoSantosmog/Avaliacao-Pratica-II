# Avaliação Prática – Aplicação CRUD de Alunos com Flask & SQLite

## Instruções Iniciais – IMPORTANTE  
Antes de começar a prova, siga estes passos obrigatórios:

1. **Faça o fork do repositório oficial da atividade** disponibilizado no github do professor, nome do repositorio: Avaliacao-Pratica-II.  
2. No seu fork, você já encontrará os arquivos:  
   - `app.py` (pré-criado)  
   - `schema.sql` (pré-criado)  
   - Pasta `templates/` contendo os templates base da prova  
3. A partir disso, você deve desenvolver toda a lógica solicitada **dentro do seu próprio repositório (fork)**.

---

## Objetivo  
Desenvolver uma aplicação web simples usando Flask e SQLite que permita cadastrar e listar alunos.

---

## Descrição da tarefa  
Você deverá completar a aplicação garantindo:

- Comunicação correta com o banco de dados SQLite  
- Leitura do arquivo `schema.sql` para criação das tabelas  
- Implementação das rotas necessárias  
- Exibição dos alunos cadastrados  
- Cadastro de novos alunos  

O arquivo `app.py` já existe no repositório — você deve completar, ajustar e finalizar o código conforme solicitado.

---

## Requisitos obrigatórios  

### 1. Banco de Dados (schema.sql)

O arquivo já existe, mas deve conter exatamente:

```sql
CREATE TABLE IF NOT EXISTS aluno (
    id,
    nome,
    idade,
    curso,
);
```

### 2. Funcionalidades da aplicação

#### Rotas obrigatórias:

- **`/` (GET)**  
  Exibe todos os alunos cadastrados, mostrando:  
  - ID  
  - Nome  
  - Idade  
  - Curso  

- **`/cadastro` (GET + POST)**  
  GET → Exibe formulário de cadastro  
  POST → Recebe dados, insere no banco e redireciona para `/`

### 3. No arquivo `app.py` (já criado):

Você deve garantir:

- Conexão ao banco com:  
  ```python
  sqlite3.connect(...)
  ```

- Uso de:
  ```python
  conn.row_factory = sqlite3.Row
  ```

- Criação da função `start_db()` que lê o `schema.sql` ao iniciar a aplicação.

- Chamado obrigatório dentro de:
  ```python
  if __name__ == '__main__':
  ```

- Fechar conexões após cada consulta ou inserção (`conn.close()`)

---

## Templates obrigatórios  

### `index.html`
- Exibir os registros da tabela `aluno` em uma tabela HTML

### `cadastro.html`
- Formulário com os campos:
  - nome  
  - idade  
  - curso  
- Botão **Cadastrar**

---

## Critérios de Avaliação

| Critério                                | Peso | 
|-----------------------------------------|------|
| Função de UPDATE E DELETE funcionando corretamente | 50% | Desejável |
| Schema correto conforme especificado     | 10%  | Crítico |
| Funcionalidade de listagem implementada | 10%  | Crítico |
| Funcionalidade de cadastro implementada | 10%  | Crítico |
| Organização e clareza do código         | 10%  | Crítico |
| Uso correto de templates                | 5%   | Crítico |
| Boas práticas (commit, fechar conexões) | 5%   | Crítico |

---

## Instruções para entrega  

Você deverá entregar **apenas o link do seu fork** no GitHub contendo:

- `app.py`  
- `schema.sql`  
- Pasta `templates/` com `index.html` e `cadastro.html`
- (Opcional) Pasta `static/` com `style.css`

Além disso:

- Incluir no topo do `README.md`:  
  **nome do estudante, turma e data**
- Adicionar comentários no `app.py`
- Garantir que o projeto está rodando corretamente em Python 3.x

---

## Observações finais  

- **UPDATE/DELETE não são obrigatórios**, mas valem **ponto extra** se implementados.  
- CSS é opcional, mas recomendável.  

---

Boa prova!  
