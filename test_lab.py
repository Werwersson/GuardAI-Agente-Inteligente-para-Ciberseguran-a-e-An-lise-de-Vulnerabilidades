"""
test_lab.py — Suíte de testes automatizados para o laboratório GuardAI.

Compara o comportamento do app.py (vulnerável) com o app_secure.py (mitigado),
comprovando na prática as vulnerabilidades e a eficácia das correções.

Pode ser executado diretamente:
    python test_lab.py
Ou via pytest:
    pytest test_lab.py -v
"""

import unittest
import os
import sqlite3
import json
import sys

# Garante suporte a UTF-8 no terminal Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Importa as aplicações Flask e inicializadores
import app as vulnerable_module
import app_secure as secure_module


class TestVulnerableApp(unittest.TestCase):
    """Testes demonstrando as falhas de segurança no app.py."""

    @classmethod
    def setUpClass(cls):
        # Remove banco de teste anterior se existir e reinicializa
        if os.path.exists("users.db"):
            os.remove("users.db")
        vulnerable_module.init_db()
        cls.client = vulnerable_module.app.test_client()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists("users.db"):
            try:
                os.remove("users.db")
            except Exception:
                pass

    def test_sql_injection_bypass(self):
        """VULNERABILIDADE: SQL Injection permite bypass de autenticacao sem senha valida."""
        sqli_payload = "admin' OR '1'='1' --"
        response = self.client.post("/login", data={
            "username": sqli_payload,
            "password": "senha_completamente_falsa"
        })
        self.assertEqual(response.status_code, 200, "O SQL Injection deveria burlar a autenticação no app vulnerável.")
        data = response.get_json()
        self.assertIn("message", data)
        self.assertEqual(data["user"]["username"], "admin")
        print("\n[VULNERAVEL] SQL Injection bypass confirmado com sucesso no app.py!")

    def test_unauthorized_users_endpoint(self):
        """VULNERABILIDADE: /users expoe a lista completa sem qualquer autenticacao."""
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("users", data)
        self.assertGreaterEqual(len(data["users"]), 2)
        print("[VULNERAVEL] Endpoint /users acessivel sem autenticacao!")

    def test_plaintext_password_in_db(self):
        """VULNERABILIDADE: Senhas armazenadas em texto plano no banco de dados."""
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username='admin'")
        row = cursor.fetchone()
        conn.close()
        self.assertEqual(row[0], "admin123", "Senha deveria estar em texto plano no app vulnerável.")
        print("[VULNERAVEL] Senha 'admin123' encontrada em texto plano no SQLite!")


class TestSecureApp(unittest.TestCase):
    """Testes comprovando as mitigações implementadas no app_secure.py."""

    @classmethod
    def setUpClass(cls):
        if os.path.exists("users_secure.db"):
            os.remove("users_secure.db")
        secure_module.init_db()
        cls.client = secure_module.app.test_client()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists("users_secure.db"):
            try:
                os.remove("users_secure.db")
            except Exception:
                pass

    def test_sql_injection_blocked(self):
        """MITIGACAO: SQL Injection falha com 401 gracas a consultas parametrizadas."""
        sqli_payload = "admin' OR '1'='1' --"
        response = self.client.post("/login", data={
            "username": sqli_payload,
            "password": "senha_completamente_falsa"
        })
        self.assertEqual(response.status_code, 401, "A tentativa de SQL Injection deve retornar 401 Unauthorized.")
        data = response.get_json()
        self.assertEqual(data["error"], "Credenciais inválidas.")
        print("\n[SEGURO] SQL Injection bloqueado com sucesso no app_secure.py (401)!")

    def test_valid_login_succeeds(self):
        """FUNCIONALIDADE: Login legitimo com senha correta e aceito."""
        response = self.client.post("/login", data={
            "username": "admin",
            "password": "admin123"
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["message"], "Login bem-sucedido!")
        self.assertEqual(data["user"]["username"], "admin")
        print("[SEGURO] Login legitimo autenticado com sucesso!")

    def test_security_headers_present(self):
        """MITIGACAO: Headers de seguranca adicionados em todas as respostas."""
        response = self.client.get("/")
        self.assertEqual(response.headers.get("X-Content-Type-Options"), "nosniff")
        self.assertEqual(response.headers.get("X-Frame-Options"), "DENY")
        self.assertIn("default-src 'self'", response.headers.get("Content-Security-Policy", ""))
        print("[SEGURO] Headers de seguranca verificados com sucesso!")

    def test_unauthenticated_users_endpoint_blocked(self):
        """MITIGACAO: /users requer autenticacao e autorizacao de administrador."""
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 401, "Usuário não autenticado deve receber 401.")
        print("[SEGURO] Acesso nao autenticado a /users bloqueado com sucesso (401)!")

    def test_password_hashed_in_db(self):
        """MITIGACAO: Senhas sao armazenadas como hash seguro no banco."""
        conn = sqlite3.connect("users_secure.db")
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE username='admin'")
        row = cursor.fetchone()
        conn.close()
        password_hash = row[0]
        self.assertNotEqual(password_hash, "admin123")
        self.assertTrue(password_hash.startswith("pbkdf2:sha256:"), "Hash deve usar PBKDF2:SHA256.")
        print("[SEGURO] Senha armazenada como hash seguro PBKDF2:SHA256!")


if __name__ == "__main__":
    print("=" * 70)
    print("[*] SUITE DE TESTES DO LABORATORIO GUARDAI")
    print("=" * 70)
    unittest.main(verbosity=2)
