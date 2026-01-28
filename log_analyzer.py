from collections import defaultdict

LOG_FILE = "auth.log"
FAILED_LIMIT = 3

failed_attempts = defaultdict(int)

with open(LOG_FILE, "r") as log:
    for line in log:
        if "Failed password" in line:
            ip = line.split("from")[1].split()[0]
            failed_attempts[ip] += 1

print("=== Análise de Logs de Autenticação ===\n")

for ip, attempts in failed_attempts.items():
    print(f"IP: {ip} | Tentativas falhas: {attempts}")
    if attempts >= FAILED_LIMIT:
        print(f"[ALERTA] Possível ataque de força bruta detectado ({ip})\n")
