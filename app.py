"""
app.py — Aplicação Flask VULNERÁVEL para demonstração educacional.

⚠️  ATENÇÃO: Este código contém vulnerabilidades INTENCIONAIS.
    Ele foi criado exclusivamente para fins de estudo e teste com o GuardAI Agent.
    NUNCA use este código em produção.

Vulnerabilidades presentes:
    1. SQL Injection no login (concatenação direta de strings em SQL)
    2. Senha armazenada em texto plano (sem hashing)
    3. Secret key hardcoded no código-fonte
    4. Debug mode ativo (expõe stack traces)
    5. Sem proteção CSRF
    6. Mensagens de erro revelam informações internas
    7. Sem rate limiting (permite brute force)
    8. Sem headers de segurança
"""

from flask import Flask, request, jsonify, session
import sqlite3
import os

# ❌ VULNERABILIDADE: Secret key hardcoded no código-fonte
app = Flask(__name__)
app.secret_key = "super_secret_key_123"


def init_db():
    """Inicializa o banco de dados com um usuário de teste."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT,
            role TEXT DEFAULT 'user'
        )
    """)
    # ❌ VULNERABILIDADE: Senha armazenada em texto plano
    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password, email, role)
        VALUES ('admin', 'admin123', 'admin@example.com', 'admin')
    """)
    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password, email, role)
        VALUES ('user1', 'password123', 'user1@example.com', 'user')
    """)
    conn.commit()
    conn.close()


@app.route("/")
def index():
    return jsonify({
        "app": "Sistema de Login Vulnerável (Lab)",
        "aviso": "⚠️ Este sistema contém vulnerabilidades intencionais para estudo.",
        "endpoints": {
            "POST /login": "Autenticação de usuário",
            "GET /profile": "Perfil do usuário logado",
            "GET /users": "Lista de usuários (admin)"
        }
    })


@app.route("/login", methods=["POST"])
def login():
    """
    Endpoint de login VULNERÁVEL a SQL Injection.
    
    O username e password são concatenados diretamente na query SQL,
    permitindo que um atacante manipule a consulta.
    
    Exemplo de exploração:
        username: admin' OR '1'='1' --
        password: qualquer_coisa
    """
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # ❌ VULNERABILIDADE: SQL Injection — concatenação direta
    # Um atacante pode enviar: username = admin' OR '1'='1' --
    # A query resultante seria:
    # SELECT * FROM users WHERE username='admin' OR '1'='1' --' AND password='...'
    # Isso retorna todos os usuários, fazendo login como o primeiro (admin).
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    # ❌ VULNERABILIDADE: Mensagem de erro revela a query SQL
    try:
        cursor.execute(query)
        user = cursor.fetchone()
    except Exception as e:
        conn.close()
        return jsonify({
            "error": "Erro no banco de dados",
            "detail": str(e),  # ❌ Expõe detalhes internos
            "query": query       # ❌ Expõe a query SQL executada
        }), 500

    conn.close()

    if user:
        session["user_id"] = user[0]
        session["username"] = user[1]
        session["role"] = user[4]
        return jsonify({
            "message": f"Login bem-sucedido! Bem-vindo, {user[1]}.",
            "user": {
                "id": user[0],
                "username": user[1],
                "email": user[3],
                "role": user[4]
            }
        })
    else:
        # ❌ VULNERABILIDADE: Mensagem revela que o usuário existe ou não
        return jsonify({"error": "Credenciais inválidas."}), 401


@app.route("/profile")
def profile():
    """Retorna o perfil do usuário logado."""
    if "user_id" not in session:
        return jsonify({"error": "Não autenticado."}), 401
    
    # ❌ VULNERABILIDADE: Busca por user_id da sessão sem validação adicional
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id={session['user_id']}"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            "id": user[0],
            "username": user[1],
            "password": user[2],  # ❌ VULNERABILIDADE: Retorna a senha na resposta!
            "email": user[3],
            "role": user[4]
        })
    return jsonify({"error": "Usuário não encontrado."}), 404


@app.route("/users")
def list_users():
    """
    Lista todos os usuários.
    ❌ VULNERABILIDADE: Sem verificação de autorização (qualquer um pode acessar).
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, role FROM users")
    users = cursor.fetchall()
    conn.close()

    return jsonify({
        "users": [
            {"id": u[0], "username": u[1], "email": u[2], "role": u[3]}
            for u in users
        ]
    })


if __name__ == "__main__":
    init_db()
    # ❌ VULNERABILIDADE: Debug mode ativo em "produção"
    # Expõe stack traces, permite execução de código via debugger
    app.run(debug=True, host="0.0.0.0", port=5000)
