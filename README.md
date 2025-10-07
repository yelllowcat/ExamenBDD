# Sistema Bancario Fintech 🏦

Sistema de gestión bancaria desarrollado en Python con interfaz gráfica Tkinter y base de datos MySQL. Permite a los usuarios registrarse, iniciar sesión, crear cuentas bancarias, realizar transferencias y consultar el historial de transacciones.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Base de Datos](#base-de-datos)
- [Arquitectura](#arquitectura)
- [Funcionalidades](#funcionalidades)
- [Contribuir](#contribuir)

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

- Python 3.8 o superior
- MySQL 5.7 o superior
- pip (gestor de paquetes de Python)

## 📦 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/yelllowcat/ExamenBDD.git
   cd ExamenBDD
   ```

2. **Crear entorno virtual (recomendado)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Linux/Mac
   # o
   .venv\Scripts\activate  # En Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install mysql-connector-python python-dotenv
   ```

## ⚙️ Configuración

1. **Configurar la base de datos**
   
   Ejecutar el script SQL para crear la base de datos y los procedimientos almacenados:
   ```bash
   mysql -u root -p < examenPythonBD.sql
   ```

2. **Configurar variables de entorno**
   
   Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:
   ```env
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=fintech
   DB_USER=tu_usuario
   DB_PASSWORD=tu_contraseña
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
