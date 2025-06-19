# 📊 Dataset de Transacciones Financieras - Detección de Fraude

Este repositorio contiene un ejemplo de dataset simulado para detección de fraude en transacciones financieras, incluyendo una clasificación por categorías y una tabla funcional con tipos de datos y ejemplos.

---

## 🔢 Campos de la Transacción

### 📁 Categorías de cada campo

| Campo               | Categoría         | Descripción                                  |
|--------------------|-------------------|----------------------------------------------|
| transaction_id     | Identificador     | ID único de la transacción                   |
| timestamp          | Temporal          | Fecha y hora de la transacción               |
| user_id            | Usuario           | ID del usuario que realiza la transacción    |
| amount             | Financiero        | Monto de la transacción                      |
| currency           | Financiero        | Tipo de moneda (ISO 4217)                    |
| merchant_id        | Comercio          | ID del comercio donde se realiza la compra   |
| merchant_category  | Comercio          | Categoría del comercio (por rubro)           |
| payment_method     | Medio de pago     | Método utilizado para pagar                  |
| channel            | Canal             | Canal por el que se realiza la operación     |
| device_id          | Dispositivo       | ID del dispositivo desde el que se paga      |
| location.lat       | Geolocalización   | Latitud de la transacción                    |
| location.lon       | Geolocalización   | Longitud de la transacción                   |
| location.city      | Geolocalización   | Ciudad                                       |
| location.country   | Geolocalización   | País (ISO 3166-1 alpha-2)                    |

---

## 📘 Campo - Tipo de Dato - Descripción Funcional - Ejemplos

| Campo             | Tipo de dato       | Descripción funcional                                 | Ejemplos                        |
|------------------|--------------------|--------------------------------------------------------|----------------------------------|
| transaction_id   | string             | Identificador único de transacción                     | "txn_987654321"                 |
| timestamp        | string (ISO 8601)  | Fecha y hora de la transacción                         | "2025-06-05T13:45:12Z"          |
| user_id          | string             | ID del usuario que realiza la transacción              | "user_1024"                     |
| amount           | float              | Monto total de la transacción                          | 824.75                          |
| currency         | string (ISO)       | Código de moneda de la transacción                     | "USD"                           |
| merchant_id      | string             | Identificador del comercio                             | "mrc_5487"                      |
| merchant_category| string             | Categoría del comercio o rubro                         | "electronics"                   |
| payment_method   | string             | Método de pago utilizado                               | "credit_card", "debit_card"     |
| channel          | string             | Canal utilizado para la transacción                    | "mobile_app", "web", "ATM"      |
| device_id        | string             | Identificador del dispositivo usado                    | "dev_2323abc"                   |
| location.lat     | float              | Latitud desde donde se realizó la transacción          | -12.0464                        |
| location.lon     | float              | Longitud desde donde se realizó la transacción         | -77.0428                        |
| location.city    | string             | Ciudad donde ocurrió la transacción                    | "Lima"                          |
| location.country | string (ISO)       | País de la transacción                                 | "PE"                            |

---

## 🚀 Objetivo del Proyecto

Este dataset está diseñado para probar soluciones de analítica en tiempo real, como detección de fraude financiero utilizando tecnologías como Python, OpenSearch, Kafka o Spark Streaming.

---

# 🐳 Proyecto con Docker Compose: OpenSearch + Dashboards + Filebeat + Logstash

Este proyecto contiene una arquitectura básica usando Docker Compose para levantar un entorno con:

- Generador de logs (`generator`)
- Filebeat
- Logstash
- OpenSearch
- OpenSearch Dashboards

---

## 🚀 Instrucciones de uso

### 1. Clona el repositorio y ubícate en la raíz del proyecto

```bash
git clone https://github.com/tuusuario/tu-proyecto.git
cd tu-proyecto
```

---

### 2. 🛠️ Construye los contenedores

Desde la raíz del proyecto, ejecuta:

```bash
docker-compose build
```

Esto construirá la imagen personalizada para el generador de logs (`generator`), y descargará las demás imágenes necesarias.

---

### 3. ▶️ Ejecuta todos los contenedores

```bash
docker-compose up
```

Esto levantará todos los servicios definidos en `docker-compose.yml`.

Puedes agregar `-d` para ejecutarlos en segundo plano:

```bash
docker-compose up -d
```

---

## 🧪 Verifica

- Abre OpenSearch Dashboards en: [http://localhost:5601](http://localhost:5601)
- Verifica que el archivo `generator/data/output.txt` se haya generado correctamente
- Filebeat leerá ese archivo, y Logstash lo enviará a OpenSearch

---

## 🛑 Detener los contenedores

```bash
docker-compose down
```

---

## 📦 Requisitos

- Docker
- Docker Compose v1.29+ o Docker Compose v2

---

## 📁 Estructura esperada del proyecto

```
.
├── docker-compose.yml
├── Dockerfile
├── generator/
│   ├── generateData.py
│   └── data/
│       └── transactions.log
├── filebeat/
│   └── filebeat.yml
├── logstash/
│   └── pipeline/
│       └── logstash.conf
└── opensearch-dashboards/
    └── opensearch_dashboards.yml
```

---

## 👨‍💻 Credenciales por defecto

- **Usuario:** `admin`
- **Contraseña:** `Contrasena123456789$` (definida en las variables de entorno)

---