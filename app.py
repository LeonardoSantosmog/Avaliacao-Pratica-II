from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sq

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
DB_PATH = "escola_fb.db"

def get_connection():
    return sq.connect(DB_PATH)

def criar_tabela():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                curso TEXT NOT NULL
            );
        ''')

criar_tabela()

@app.route('/')
def index():
    with get_connection() as conn:
        alunos = conn.execute('SELECT * FROM aluno').fetchall()
    
    alunos_list = []
    for aluno in alunos:
        alunos_list.append({
            'id': aluno[0],
            'nome': aluno[1],
            'idade': aluno[2],
            'curso': aluno[3]
        })
    
    return render_template('index.html', alunos=alunos_list)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        curso = request.form['curso']
        
        with get_connection() as conn:
            conn.execute(
                'INSERT INTO aluno (nome, idade, curso) VALUES (?, ?, ?)',
                (nome, idade, curso)
            )
            conn.commit()
        
        return redirect(url_for('index'))
    
    return render_template('cadastro.html')

@app.route('/editar/<int:id_aluno>', methods=['GET', 'POST'])
def editar_aluno(id_aluno):
    with get_connection() as conn:
        aluno = conn.execute("SELECT * FROM aluno WHERE id = ?", (id_aluno,)).fetchone()

    if aluno is None:
        flash("❌ Aluno não encontrado.", "error")
        return redirect(url_for('index'))

    if request.method == 'POST':
        novo_nome = request.form.get('nome')
        nova_idade = request.form.get('idade', type=int)
        novo_curso = request.form.get('curso')

        if not novo_nome or nova_idade is None or not novo_curso:
            flash("⚠️ Preencha todos os campos corretamente.", "error")
            return redirect(url_for('editar_aluno', id_aluno=id_aluno))

        try:
            with get_connection() as conn:
                conn.execute(
                    "UPDATE aluno SET nome = ?, idade = ?, curso = ? WHERE id = ?",
                    (novo_nome, nova_idade, novo_curso, id_aluno)
                )
                conn.commit()
            flash("✅ Aluno atualizado com sucesso!", "success")
        except sq.Error as e:
            flash(f"❌ Erro ao atualizar aluno: {e}", "error")

        return redirect(url_for('index'))

    return render_template('editar.html', aluno=aluno)

@app.route('/excluir/<int:id_aluno>', methods=['POST'])
def excluir_aluno(id_aluno):
    try:
        with get_connection() as conn:
            conn.execute("DELETE FROM aluno WHERE id = ?", (id_aluno,))
            conn.commit()
        flash("🗑️ Aluno excluído com sucesso!", "success")
    except sq.Error as e:
        flash(f"❌ Erro ao excluir aluno: {e}", "error")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)