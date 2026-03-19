# 🌡️📊 API Conversor & Promedio

Proyecto de APIs REST desarrolladas con **Flask** que ofrece dos microservicios:

1. **Conversor de Temperatura** — Convierte entre Celsius y Fahrenheit.
2. **Calculadora de Promedio** — Calcula el promedio de calificaciones de un estudiante.

---

## 📁 Estructura del Proyecto

```
API_CONVERSOR_PROMEDIO/
├── .env                  # Variables de entorno (no se sube al repo)
├── .gitignore            # Archivos y carpetas ignorados por Git
├── app_conversor.py      # API de conversión de temperatura
├── app_promedio.py       # API de cálculo de promedio
├── requirements.txt      # Dependencias del proyecto
└── README.md
```

---

## ⚙️ Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

---

## 🚀 Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/API_CONVERSOR_PROMEDIO.git
   cd API_CONVERSOR_PROMEDIO
   ```

2. **Crear y activar un entorno virtual:**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar las variables de entorno:**

   Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

   ```env
   FLASK_APP_PROMEDIO=app_promedio.py
   FLASK_APP_CONVERSOR=app_conversor.py
   FLASK_ENV=development
   FLASK_DEBUG=True
   FLASK_RUN_HOST=127.0.0.1
   FLASK_RUN_PORT=5000
   SECRET_KEY=tu_clave_secreta_aqui
   ```

---

## ▶️ Ejecución

Cada microservicio se ejecuta de forma independiente.

### Conversor de Temperatura

```bash
python app_conversor.py
```

### Calculadora de Promedio

```bash
python app_promedio.py
```

> **Nota:** Ambos servicios usan el puerto `5000` por defecto. Para ejecutarlos simultáneamente, cambia el valor de `FLASK_RUN_PORT` en el `.env` o ejecuta uno en un puerto diferente:
>
> ```bash
> FLASK_RUN_PORT=5001 python app_promedio.py
> ```

---

## 📡 Endpoints

### 1. Conversor de Temperatura

| Propiedad | Detalle |
|-----------|---------|
| **URL** | `/convertir-temperatura` |
| **Método** | `POST` |
| **Content-Type** | `application/json` |

#### Cuerpo de la petición

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `valor` | `number` | Temperatura a convertir |
| `escala` | `string` | `"C"` (Celsius → Fahrenheit) o `"F"` (Fahrenheit → Celsius) |

#### Ejemplo de petición

```bash
curl -X POST http://127.0.0.1:5000/convertir-temperatura \
  -H "Content-Type: application/json" \
  -d '{"valor": 100, "escala": "C"}'
```

#### Ejemplo de respuesta exitosa (`200`)

```json
{
  "valor_original": 100,
  "escala_origen": "Celsius",
  "resultado": 212.0,
  "escala_destino": "Fahrenheit",
  "mensaje": "100° Celsius equivale a 212.0°F"
}
```

#### Ejemplo de respuesta con error (`400`)

```json
{
  "error": "Se requieren los campos 'valor' y 'escala'"
}
```

---

### 2. Calculadora de Promedio

| Propiedad | Detalle |
|-----------|---------|
| **URL** | `/promedio` |
| **Método** | `POST` |
| **Content-Type** | `application/json` |

#### Cuerpo de la petición

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `nombre` | `string` | Nombre del estudiante |
| `calificaciones` | `array[number]` | Lista de calificaciones |

#### Ejemplo de petición

```bash
curl -X POST http://127.0.0.1:5000/promedio \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Juan Pérez", "calificaciones": [90, 85, 78, 92, 88]}'
```

#### Ejemplo de respuesta exitosa (`200`)

```json
{
  "nombre": "Juan Pérez",
  "calificaciones": [90, 85, 78, 92, 88],
  "promedio": 86.6
}
```

#### Ejemplo de respuesta con error (`400`)

```json
{
  "error": "Se requieren los campos 'nombre' y 'calificaciones'"
}
```

---

## 🛠️ Tecnologías

- **Python 3** — Lenguaje de programación
- **Flask 3.1.0** — Framework web ligero
- **python-dotenv 1.0.1** — Gestión de variables de entorno

---

## 🧪 Pruebas con Postman

Puedes importar las siguientes configuraciones en **Postman** para probar los endpoints:

1. Crear una nueva petición `POST`.
2. Configurar la URL correspondiente (`http://127.0.0.1:5000/convertir-temperatura` o `/promedio`).
3. En la pestaña **Body**, seleccionar **raw** y **JSON**.
4. Pegar el JSON de ejemplo y enviar la petición.

---

## 📝 Licencia

Este proyecto es de uso libre con fines educativos.