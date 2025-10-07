# Sistema Bancario Fintech 🏦

Sistema de gestión bancaria desarrollado en Python con interfaz gráfica Tkinter y base de datos MySQL. Permite a los usuarios registrarse, iniciar sesión, crear cuentas bancarias, realizar transferencias y consultar el historial de transacciones.

## 👥 Integrantes del Equipo

- **David González** - Responsable del proyecto

## 📋 Tabla de Contenidos

- [Integrantes del Equipo](#integrantes-del-equipo)
- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
- [Ejecutar la Base de Datos](#ejecutar-la-base-de-datos)
- [Ejecutar la Aplicación](#ejecutar-la-aplicación)
- [Usuarios y Cuentas de Prueba](#usuarios-y-cuentas-de-prueba)
- [Ejemplos de Operaciones](#ejemplos-de-operaciones)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Base de Datos](#base-de-datos)
- [Arquitectura](#arquitectura)
- [Compilar Ejecutable](#compilar-ejecutable)

## ✨ Características

- **Gestión de Usuarios**
  - Registro de nuevos usuarios
  - Inicio de sesión seguro
  - Validación de credenciales

- **Gestión de Cuentas**
  - Creación de cuentas bancarias con saldo inicial
  - Generación automática de números de cuenta únicos
  - Visualización de cuentas del usuario con saldos actualizados

- **Transferencias**
  - Transferencias entre cuentas
  - Validación de fondos suficientes
  - Notas opcionales en transferencias
  - Registro automático de movimientos

- **Historial de Transacciones**
  - Consulta de historial completo de movimientos
  - Visualización detallada de transferencias entrantes y salientes
  - Filtrado por cuenta

## 🔧 Requisitos Previos

- **Python 3.8 o superior**
- **MySQL 5.7 o superior**
- **pip** (gestor de paquetes de Python)

## 📦 Instalación y Configuración

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/yelllowcat/ExamenBDD.git
cd ExamenBDD
```

### Paso 2: Crear entorno virtual (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # En Linux/Mac
# o
.venv\Scripts\activate  # En Windows
```

### Paso 3: Instalar dependencias

```bash
pip install mysql-connector-python python-dotenv
```

### Paso 4: Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=fintech
DB_USER=root
DB_PASSWORD=tu_contraseña_mysql
```

**Importante**: Reemplaza `tu_contraseña_mysql` con tu contraseña real de MySQL.

## 🗄️ Ejecutar la Base de Datos

### Opción 1: Desde la línea de comandos

```bash
mysql -u root -p < examenPythonBD.sql
```

Ingresa tu contraseña de MySQL cuando se te solicite.

### Opción 2: Desde el cliente MySQL

```bash
# Acceder a MySQL
mysql -u root -p

# Dentro de MySQL, ejecutar:
source /ruta/completa/a/examenPythonBD.sql
# o en Windows:
\. C:\ruta\completa\a\examenPythonBD.sql
```

### Verificar la instalación

```sql
-- Mostrar bases de datos
SHOW DATABASES;

-- Usar la base de datos
USE fintech;

-- Verificar tablas
SHOW TABLES;

-- Verificar procedimientos almacenados
SHOW PROCEDURE STATUS WHERE Db = 'fintech';
```

Deberías ver:
- **Base de datos**: `fintech`
- **Tablas**: `usuarios`, `cuentas`, `movimientos`
- **Procedimientos**: `registrar_usuario`, `iniciar_sesion`, `obtener_detalles_usuario`, `abrir_cuenta`, `transferir_dinero`

## 🚀 Ejecutar la Aplicación

Una vez configurada la base de datos y el archivo `.env`:

```bash
# Asegúrate de estar en el directorio del proyecto
cd ExamenBDD

# Activar entorno virtual (si lo usas)
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Ejecutar la aplicación
python main.py
```

La ventana de inicio de sesión debería aparecer.

## 👤 Usuarios y Cuentas de Prueba

El script SQL incluye usuarios y cuentas de prueba pre-configurados:

### Usuarios Registrados

| Email | Contraseña | Nombre Completo |
|-------|------------|-----------------|
| david@mail.com | hash123 | David González |
| ana@mail.com | hash456 | Ana López |
| luis@mail.com | hash789 | Luis Martínez |
| carla@mail.com | hash101 | Carla Fernández |

### Cuentas Bancarias

| Número de Cuenta | Saldo Inicial | Propietario | Estado |
|------------------|---------------|-------------|--------|
| ACC10001 | $1,000.00 | David González | ACTIVA |
| ACC10002 | $250.00 | David González | ACTIVA |
| ACC20001 | $500.00 | Ana López | ACTIVA |
| ACC30001 | $750.00 | Luis Martínez | ACTIVA |
| ACC40001 | $1,200.00 | Carla Fernández | ACTIVA |

## 💡 Ejemplos de Operaciones

### 1. Iniciar Sesión

1. Ejecutar `python main.py`
2. Ingresar credenciales:
   - **Email**: `david@mail.com`
   - **Contraseña**: `hash123`
3. Click en "Iniciar Sesión"

### 2. Crear Nueva Cuenta Bancaria (Apertura)

1. Desde la pantalla principal, click en **"Crear Cuenta"**
2. Ingresar saldo inicial: `5000`
3. Click en **"Crear Cuenta"**
4. Se generará automáticamente un número de cuenta único
5. Se registrará un movimiento de tipo **APERTURA**

**Resultado esperado**:
- Nueva cuenta creada con saldo de $5,000.00
- Número de cuenta generado (formato: `1001-XXXX-XXXX-XXXX`)
- Movimiento de apertura registrado en el historial

### 3. Realizar Transferencia

1. Desde la pantalla principal, click en **"Transferir"**
2. Completar el formulario:
   - **Monto**: `500`
   - **Transferir a (ID de Cuenta)**: Seleccionar cuenta destino (ej: `2`)
   - **Nota**: `Pago de servicios` (opcional)
3. Click en **"Transferir"**

**Resultado esperado**:
- Se resta $500.00 de tu cuenta
- Se suma $500.00 a la cuenta destino
- Se registran 2 movimientos:
  - **TRANSFERENCIA_SALIDA** en tu cuenta
  - **TRANSFERENCIA_ENTRADA** en la cuenta destino

**Validaciones automáticas**:
- ✅ Verifica fondos suficientes
- ✅ Verifica que ambas cuentas estén activas
- ✅ Verifica que no se transfiera a la misma cuenta
- ✅ Verifica que el monto sea mayor a cero

### 4. Consultar Historial de Movimientos

1. Desde la pantalla principal, seleccionar una cuenta del desplegable
2. Click en **"Consultar Historial"**
3. Se mostrará una tabla con todas las transacciones:
   - ID del movimiento
   - Tipo de movimiento
   - Cuenta de salida
   - Cuenta de entrada
   - Monto
   - Fecha y hora
   - Nota

**Tipos de movimientos que verás**:
- **APERTURA**: Creación de la cuenta
- **TRANSFERENCIA_SALIDA**: Dinero que sale de tu cuenta
- **TRANSFERENCIA_ENTRADA**: Dinero que entra a tu cuenta

### 5. Ejemplo Completo de Flujo

```
1. Iniciar sesión con david@mail.com / hash123
2. Ver cuentas disponibles: ACC10001 ($1,000.00) y ACC10002 ($250.00)
3. Crear nueva cuenta con saldo inicial de $5,000.00
4. Transferir $200.00 de ACC10001 a cuenta de Ana (ID: 3)
5. Consultar historial de ACC10001 para ver la transferencia
6. Cerrar sesión
```

### Ejemplo desde MySQL (Consultas Directas)

```sql
-- Ver todos los usuarios
SELECT * FROM usuarios;

-- Ver todas las cuentas
SELECT 
    c.numero_cuenta,
    c.saldo,
    c.estado,
    u.nombre,
    u.apellidos
FROM cuentas c
JOIN usuarios u ON c.usuario_id = u.id;

-- Ver historial de movimientos
SELECT 
    m.id,
    m.tipo_movimiento,
    cs.numero_cuenta AS cuenta_salida,
    ce.numero_cuenta AS cuenta_entrada,
    m.monto,
    m.fecha_operacion,
    m.nota
FROM movimientos m
LEFT JOIN cuentas cs ON m.cuenta_salida_id = cs.id
LEFT JOIN cuentas ce ON m.cuenta_entrada_id = ce.id
ORDER BY m.fecha_operacion DESC;

-- Realizar una transferencia manualmente
CALL transferir_dinero(1, 2, 100.00, 'Transferencia de prueba');

-- Ver saldo de una cuenta específica
SELECT numero_cuenta, saldo FROM cuentas WHERE numero_cuenta = 'ACC10001';
```

## 📁 Estructura del Proyecto

```
ExamenBDD/
│
├── config/
│   └── db.py                    # Configuración de base de datos
│
├── controller/
│   └── userController.py        # Controlador principal de la aplicación
│
├── models/
│   ├── db/
│   │   └── db_connector.py      # Conector a la base de datos
│   └── users_model.py           # Modelo de datos de usuarios y cuentas
│
├── views/
│   ├── loginView.py             # Vista de inicio de sesión
│   ├── register_view.py         # Vista de registro
│   ├── home_view.py             # Vista principal (home)
│   ├── create_account_view.py   # Vista para crear cuentas
│   ├── transfer_view.py         # Vista para transferencias
│   └── consult_history_view.py  # Vista de historial de transacciones
│
├── .env                         # Variables de entorno (no incluido en git)
├── .gitignore                   # Archivos ignorados por git
├── examenPythonBD.sql          # Script de base de datos
├── main.py                      # Punto de entrada de la aplicación
└── README.md                    # Este archivo
```

## 🚀 Uso

1. **Iniciar la aplicación**
   ```bash
   python main.py
   ```

2. **Flujo de uso**
   - Al iniciar, se mostrará la ventana de inicio de sesión
   - Si no tienes cuenta, haz clic en "Registrarse"
   - Completa el formulario de registro con tus datos
   - Inicia sesión con tu email y contraseña
   - Desde la pantalla principal podrás:
     - Crear nuevas cuentas bancarias
     - Realizar transferencias entre cuentas
     - Consultar el historial de transacciones

## 🗄️ Base de Datos

### Tablas Principales

#### `usuarios`
- `id`: Identificador único
- `email`: Correo electrónico (único)
- `nombre`: Nombre del usuario
- `apellidos`: Apellidos del usuario
- `password_hash`: Contraseña (en texto plano - **Nota**: en producción debería estar hasheada)
- `fecha_creacion`: Fecha de registro

#### `cuentas`
- `id`: Identificador único
- `numero_cuenta`: Número de cuenta único (formato: 1001-XXXX-XXXX-XXXX)
- `saldo`: Saldo actual
- `estado`: Estado de la cuenta (ACTIVA/BLOQUEADA)
- `usuario_id`: Referencia al usuario propietario

#### `movimientos`
- `id`: Identificador único
- `tipo_movimiento`: Tipo (APERTURA, TRANSFERENCIA_ENTRADA, TRANSFERENCIA_SALIDA)
- `cuenta_salida_id`: Cuenta de origen (puede ser NULL)
- `cuenta_entrada_id`: Cuenta de destino (puede ser NULL)
- `monto`: Cantidad transferida
- `fecha_operacion`: Fecha y hora del movimiento
- `nota`: Nota opcional

### Procedimientos Almacenados

- **`registrar_usuario`**: Registra un nuevo usuario en el sistema
- **`iniciar_sesion`**: Valida credenciales de usuario
- **`obtener_detalles_usuario`**: Obtiene información del usuario
- **`abrir_cuenta`**: Crea una nueva cuenta bancaria
- **`transferir_dinero`**: Realiza transferencias entre cuentas

## 🏗️ Arquitectura

El proyecto sigue el patrón **MVC (Modelo-Vista-Controlador)**:

- **Modelo (`models/`)**: Maneja la lógica de negocio y acceso a datos
  - `UserModel`: Gestiona operaciones de usuarios y cuentas
  - `DBConnector`: Maneja la conexión a la base de datos

- **Vista (`views/`)**: Interfaces gráficas con Tkinter
  - Cada vista es una ventana independiente
  - Diseño responsivo y amigable

- **Controlador (`controller/`)**: Coordina la comunicación entre modelo y vista
  - `UserController`: Gestiona el flujo de la aplicación
  - Maneja eventos de usuario
  - Valida datos antes de enviarlos al modelo

## 🎯 Funcionalidades

### 1. Registro de Usuario
- Validación de campos obligatorios
- Verificación de email único
- Almacenamiento seguro de credenciales

### 2. Inicio de Sesión
- Autenticación mediante email y contraseña
- Validación de credenciales
- Redirección a pantalla principal

### 3. Creación de Cuentas
- Saldo inicial configurable
- Generación automática de número de cuenta
- Registro de movimiento de apertura
- Actualización automática de la lista de cuentas

### 4. Transferencias
- Selección de cuenta destino
- Validación de fondos suficientes
- Validación de cuentas activas
- Notas opcionales
- Registro dual de movimientos (entrada y salida)

### 5. Consulta de Historial
- Visualización en tabla ordenada
- Filtrado por cuenta
- Información detallada de cada transacción
- Formato de moneda

## 🔒 Consideraciones de Seguridad

**Nota Importante**: Este es un proyecto educativo. Para un entorno de producción, se recomienda:

- Implementar hash de contraseñas (bcrypt, argon2)
- Usar HTTPS para comunicaciones
- Implementar autenticación de dos factores
- Agregar límites de intentos de inicio de sesión
- Validar y sanitizar todas las entradas de usuario
- Implementar logging de auditoría
- Usar variables de entorno para credenciales sensibles

## 📦 Compilar Ejecutable

Para crear un ejecutable independiente de la aplicación:

### Instalación de PyInstaller

```bash
pip install pyinstaller
```

### Compilar

```bash
# Activar entorno virtual
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Compilar usando el archivo de especificación
pyinstaller main.spec
```

El ejecutable estará en `dist/SistemaBancario`

### Crear Paquete de Distribución

```bash
# Linux/Mac
chmod +x crear_paquete.sh
./crear_paquete.sh
```

Para instrucciones detalladas, consulta [COMPILAR.md](COMPILAR.md).

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👥 Autor

Desarrollado como proyecto de examen de Base de Datos.

## 📞 Soporte

Para reportar problemas o sugerencias, por favor abre un issue en el repositorio de GitHub.
