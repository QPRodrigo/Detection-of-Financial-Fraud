from pathlib import Path
import random
import time
from datetime import datetime, timedelta, timezone

# Valores posibles para los campos
currencies = ["USD", "EUR", "PEN"]
merchant_categories = ["electronics", "food", "fashion", "travel", "utilities"]
payment_methods = ["credit_card", "debit_card", "bank_transfer", "e_wallet"]
channels = ["mobile_app", "web", "pos", "atm"]
cities = [("Lima", "PE", -12.0464, -77.0428), ("Cusco", "PE", -13.5319, -71.9675), ("Arequipa", "PE", -16.409, -71.537)]

# Generador de transacción aleatoria
def generar_log_linea():
    city, country, lat, lon = random.choice(cities)
    return (
        f"{datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')} INFO "
        f"[transaction_id] txn_{random.randint(100000000, 999999999)} "
        f"[user_id] user_{random.randint(1000, 9999)} "
        f"[amount] {round(random.uniform(5.0, 1000.0), 2)} "
        f"[currency] {random.choice(currencies)} "
        f"[merchant_id] mrc_{random.randint(1000, 9999)} "
        f"[merchant_category] {random.choice(merchant_categories)} "
        f"[payment_method] {random.choice(payment_methods)} "
        f"[channel] {random.choice(channels)} "
        f"[device_id] dev_{random.randint(1000, 9999)} "
        f"[location] {city}, {country} ({lat},{lon})"
    )


# Ruta al archivo
log_path = Path("..") / "data" / "transactions.log"

# Crear el directorio si no existe
log_path.parent.mkdir(parents=True, exist_ok=True)

# Abrir el archivo para agregar contenido
with open(log_path, "a", encoding="utf-8") as f:
    while True:
        linea = generar_log_linea()
        f.write(linea + "\n")
        f.flush()
        print("📝 Registro guardado:", linea)
        time.sleep(1)