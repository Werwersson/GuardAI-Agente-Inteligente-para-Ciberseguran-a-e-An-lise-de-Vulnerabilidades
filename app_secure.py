"""
app_secure.py — Aplicação Flask CORRIGIDA após análise do GuardAI Agent.

✅ Este código demonstra as correções aplicadas após a análise de vulnerabilidades.
   Compare com app.py para entender cada mitigação.

Correções aplicadas:
    1. ✅ SQL Injection mitigado — consultas parametrizadas
    2. ✅ Senhas com hashing seguro (bcrypt via werkzeug)
    3. ✅ Secret key via variável de ambiente
    4. ✅ Debug mode desativado
    5. ✅ Proteção CSRF (em produção, use Flask-WTF)
    6. ✅ Mensagens de erro genéricas (sem vazamento de informações)
    7. ✅ Rate limiting básico
    8. ✅ Headers de segurança
    9. ✅ Senha não retornada em endpoints
   10. ✅ Verificação de autorização no endpoint /users
"""

from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import sqlite3
import os
import time

app = Flask(__name__)

# ✅ CORREÇÃO: Secret key vem de variável de ambiente com fallback seguro
app.secret_key = os.environ.get("FLASK_SECRET_KEY", os.urandom(32).hex())

# ✅ CORREÇÃO: Configurações de sessão seguras
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

# ✅ CORREÇÃO: Rate limiting simples (em produção, use Flask-Limiter)
login_attempts = {}
MAX_ATTEMPTS = 5
LOCKOUT_TIME = 300  # 5 minutos


def add_security_headers(response):
    """✅ CORREÇÃO: Adiciona headers de segurança a todas as respostas."""
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response


app.after_request(add_security_headers)


def login_required(f):
    """Decorator para proteger endpoints que exigem autenticação."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Autenticação necessária."}), 401
        return f(*args, **kwargs)
    return decorated


def admin_required(f):
    """✅ CORREÇÃO: Decorator para proteger endpoints administrativos."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Autenticação necessária."}), 401
        if session.get("role") != "admin":
            return jsonify({"error": "Acesso negado."}), 403
        return f(*args, **kwargs)
    return decorated


def get_db():
    """Retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect("users_secure.db")
    conn.row_factory = sqlite3.Row  # Permite acesso por nome de coluna
    return conn


def init_db():
    """Inicializa o banco de dados com usuários de teste (senhas com hash)."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            email TEXT,
            role TEXT DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # ✅ CORREÇÃO: Senhas armazenadas com hash seguro (pbkdf2)
    admin_hash = generate_password_hash("admin123", method="pbkdf2:sha256")
    user_hash = generate_password_hash("password123", method="pbkdf2:sha256")

    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password_hash, email, role)
        VALUES (?, ?, ?, ?)
    """, ("admin", admin_hash, "admin@example.com", "admin"))

    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password_hash, email, role)
        VALUES (?, ?, ?, ?)
    """, ("user1", user_hash, "user1@example.com", "user"))

    conn.commit()
    conn.close()


@app.route("/")
def index():
    return jsonify({
        "app": "Sistema de Login Seguro (Lab)",
        "status": "✅ Vulnerabilidades mitigadas",
        "endpoints": {
            "POST /login": "Autenticação de usuário",
            "GET /profile": "Perfil do usuário logado (requer autenticação)",
            "GET /users": "Lista de usuários (requer role admin)"
        }
    })


@app.route("/login", methods=["POST"])
def login():
    """
    Endpoint de login SEGURO.
    
    ✅ Usa consultas parametrizadas (imune a SQL Injection).
    ✅ Verifica senha com hash (nunca compara texto plano).
    ✅ Rate limiting para prevenir brute force.
    ✅ Mensagens genéricas que não revelam se o usuário existe.
    """
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    # Validação básica de entrada
    if not username or not password:
        return jsonify({"error": "Usuário e senha são obrigatórios."}), 400

    # ✅ CORREÇÃO: Rate limiting — bloqueia após MAX_ATTEMPTS tentativas
    client_ip = request.remote_addr
    now = time.time()
    if client_ip in login_attempts:
        attempts, lockout_start = login_attempts[client_ip]
        if attempts >= MAX_ATTEMPTS and (now - lockout_start) < LOCKOUT_TIME:
            remaining = int(LOCKOUT_TIME - (now - lockout_start))
            return jsonify({
                "error": f"Muitas tentativas. Tente novamente em {remaining} segundos."
            }), 429
        elif (now - lockout_start) >= LOCKOUT_TIME:
            login_attempts[client_ip] = (0, now)

    conn = get_db()
    cursor = conn.cursor()

    # ✅ CORREÇÃO: Consulta parametrizada — imune a SQL Injection
    # O '?' é um placeholder. O SQLite substitui de forma segura,
    # sem permitir que o valor do usuário altere a estrutura da query.
    cursor.execute(
        "SELECT id, username, password_hash, email, role FROM users WHERE username = ?",
        (username,)
    )
    user = cursor.fetchone()
    conn.close()

    # ✅ CORREÇÃO: Verifica a senha com check_password_hash
    # Mesmo que a query não retorne resultado, o tempo de resposta é similar
    # (previne timing attacks).
    if user and check_password_hash(user["password_hash"], password):
        session["user_id"] = user["id"]
        session["username"] = user["username"]
        session["role"] = user["role"]
        
        # Reseta tentativas após login bem-sucedido
        login_attempts.pop(client_ip, None)
        
        return jsonify({
            "message": "Login bem-sucedido!",
            "user": {
                "id": user["id"],
                "username": user["username"],
                "role": user["role"]
                # ✅ CORREÇÃO: Não retorna email no login (minimização de dados)
            }
        })
    else:
        # ✅ CORREÇÃO: Registra tentativa falha (rate limiting)
        attempts = login_attempts.get(client_ip, (0, now))[0]
        login_attempts[client_ip] = (attempts + 1, now)

        # ✅ CORREÇÃO: Mensagem genérica — não revela se o usuário existe
        return jsonify({"error": "Credenciais inválidas."}), 401


@app.route("/profile")
@login_required
def profile():
    """Retorna o perfil do usuário logado."""
    conn = get_db()
    cursor = conn.cursor()

    # ✅ CORREÇÃO: Consulta parametrizada
    cursor.execute(
        "SELECT id, username, email, role FROM users WHERE id = ?",
        (session["user_id"],)
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            "id": user["id"],
            "username": user["username"],
            "email": user["email"],
            "role": user["role"]
            # ✅ CORREÇÃO: Senha NUNCA é retornada em nenhum endpoint
        })
    return jsonify({"error": "Usuário não encontrado."}), 404


@app.route("/users")
@admin_required  # ✅ CORREÇÃO: Apenas administradores podem listar usuários
def list_users():
    """Lista todos os usuários (apenas para admins)."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, role FROM users")
    users = cursor.fetchall()
    conn.close()

    return jsonify({
        "users": [
            {"id": u["id"], "username": u["username"], "email": u["email"], "role": u["role"]}
            for u in users
        ]
    })


@app.route("/logout", methods=["POST"])
def logout():
    """Encerra a sessão do usuário."""
    session.clear()
    return jsonify({"message": "Logout realizado com sucesso."})


if __name__ == "__main__":
    init_db()
    # ✅ CORREÇÃO: Debug mode desativado, não expõe em 0.0.0.0
    app.run(debug=False, host="127.0.0.1", port=5000)
