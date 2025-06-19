from pathlib import Path
import random
import time
from datetime import datetime

# Datos simulados
currencies = ["USD", "EUR", "PEN"]
institutions = ["BCP", "BBVA", "Interbank", "Scotiabank"]
brands = ["Visa", "MasterCard", "Amex", "Diners"]
transaction_types = ["purchase", "cash_withdrawal", "balance_inquiry"]
response_codes = ["00", "05", "12", "91", "96"]  # ISO8583 response codes
card_services = ["101", "201", "301", "421"]  # Código de servicio de tarjeta

# Función para generar una trama tipo ISO8583
def generar_trama_iso8583():
    return (
        f"[timestamp] {datetime.utcnow().isoformat()} "
        f"[mtid] 0200 "  # Message Type ID para solicitud financiera
        f"[transaction_id] txn_{random.randint(100000000, 999999999)} "
        f"[user_id] user_{random.randint(1000, 9999)} "
        f"[amount] {round(random.uniform(5.0, 1000.0), 2)} "
        f"[currency] {random.choice(currencies)} "
        f"[response_code] {random.choice(response_codes)} "
        f"[card_service] {random.choice(card_services)} "
        f"[institution_id] {random.choice(institutions)} "
        f"[brand] {random.choice(brands)} "
        f"[transaction_type] {random.choice(transaction_types)} "
        f"[response_time_ms] {random.randint(50, 500)}"
    )

# Ruta de log
log_path = Path(__file__).resolve().parent / "data" / "transactions.log"
log_path.parent.mkdir(parents=True, exist_ok=True)

print(f"📂 Guardando logs ISO8583 en: {log_path}")

# Escritura continua
try:
    with open(log_path, "a", encoding="utf-8") as f:
        for _ in range(1000000):
            linea = generar_trama_iso8583()
            f.write(linea + "\n")
            f.flush()
            print("📝 Trama generada:", linea)
            time.sleep(4)  # Pausa entre tramas
except Exception as e:
    print("❌ Error al escribir en el archivo:", e)