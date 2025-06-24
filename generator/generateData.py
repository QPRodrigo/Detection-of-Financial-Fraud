from pathlib import Path
import random
import time
from datetime import datetime

# Datos simulados
response_codes = ["00", "05", "12", "91", "96"]  # ISO8583 response codes
institutions = ["BCP", "BBVA", "Interbank", "Scotiabank"]
brands = ["Visa", "MasterCard", "Amex", "Diners"]
service_types = ["Tarjeta de Credito", "Tarjeta de Debito", "Tarjeta Prepago"]
currencies = ["USD", "EUR", "PEN"]
transaction_types = ["compra", "Retiro de Efectivo", "Consulta de Saldo"]

# Función para generar una trama tipo ISO8583
def generar_trama_iso8583():
    return (
        f"[timestamp] {datetime.utcnow().isoformat()} "
        f"[transaction_id] txn_{random.randint(100000000, 999999999)} "
        f"[mtid] 0200 "  # Message Type ID para solicitud financiera
        f"[response_code] {random.choice(response_codes)} "
        f"[service_types] {random.choice(service_types)} "
        f"[institution_id] {random.choice(institutions)} "
        f"[brand] {random.choice(brands)} "
        f"[transaction_type] {random.choice(transaction_types)} "
        f"[user_id] user_{random.randint(1000, 9999)} "
        f"[currency] {random.choice(currencies)} "
        f"[amount] {round(random.uniform(5.0, 1000.0), 2)} "
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