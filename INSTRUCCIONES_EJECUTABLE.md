# Instrucciones de Instalación - Sistema Bancario Fintech

## Requisitos Previos

Antes de ejecutar la aplicación, necesitas tener instalado:

1. **MySQL Server 5.7 o superior**
   - Descargar desde: https://dev.mysql.com/downloads/mysql/

## Pasos de Instalación

### 1. Configurar la Base de Datos

Abre una terminal o línea de comandos y ejecuta:

```bash
# Acceder a MySQL
mysql -u root -p

# Crear la base de datos (desde MySQL)
source examenPythonBD.sql
# o en Windows:
\. examenPythonBD.sql
```

Si prefieres usar la línea de comandos directamente:

```bash
mysql -u root -p < examenPythonBD.sql
```

### 2. Configurar el Archivo .env

1. Renombra el archivo `.env.example` a `.env`
2. Abre el archivo `.env` con un editor de texto
3. Configura tus credenciales de MySQL:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=fintech
DB_USER=root
DB_PASSWORD=tu_contraseña_mysql
```

**Importante**: Reemplaza `tu_contraseña_mysql` con tu contraseña real de MySQL.

### 3. Ejecutar la Aplicación

#### En Windows:
- Doble clic en `SistemaBancario.exe`

#### En Linux:
```bash
chmod +x SistemaBancario
./SistemaBancario
```

#### En macOS:
```bash
./SistemaBancario
```

## Usuarios de Prueba

La base de datos incluye usuarios de prueba:

| Email | Contraseña |
|-------|------------|
| david@mail.com | hash123 |
| ana@mail.com | hash456 |
| luis@mail.com | hash789 |
| carla@mail.com | hash101 |

## Solución de Problemas

### Error: "Por favor, crea un archivo .env..."

**Causa**: No existe el archivo `.env` o está mal ubicado.

**Solución**: 
- Asegúrate de que el archivo `.env` esté en la misma carpeta que el ejecutable
- Verifica que se llame exactamente `.env` (sin extensión adicional)

### Error: "Error connecting to database"

**Causa**: Credenciales incorrectas o MySQL no está corriendo.

**Solución**:
1. Verifica que MySQL esté en ejecución
2. Revisa las credenciales en el archivo `.env`
3. Asegúrate de que la base de datos `fintech` exista

### Error: "PROCEDURE fintech.registrar_usuario does not exist"

**Causa**: La base de datos no se creó correctamente.

**Solución**:
```bash
mysql -u root -p < examenPythonBD.sql
```

### La aplicación no inicia

**En Linux**: Puede que necesites permisos de ejecución
```bash
chmod +x SistemaBancario
```

**En Windows**: Verifica que no esté bloqueado por el antivirus

## Estructura de Archivos

```
SistemaBancario/
├── SistemaBancario.exe (o SistemaBancario en Linux/Mac)
├── .env (debes crearlo desde .env.example)
├── .env.example
├── examenPythonBD.sql
└── INSTRUCCIONES_EJECUTABLE.md (este archivo)
```

## Soporte

Para reportar problemas o solicitar ayuda:
- GitHub: https://github.com/yelllowcat/ExamenBDD/issues
