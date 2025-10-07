# Guía de Compilación del Ejecutable 🔨

Esta guía explica cómo compilar el Sistema Bancario Fintech en un ejecutable para diferentes sistemas operativos.

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Instalación de PyInstaller](#instalación-de-pyinstaller)
- [Compilación Rápida](#compilación-rápida)
- [Compilación por Sistema Operativo](#compilación-por-sistema-operativo)
- [Personalización](#personalización)
- [Solución de Problemas](#solución-de-problemas)
- [Distribución](#distribución)

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes)
- Git (para clonar el repositorio)
- MySQL 5.7+ (para probar el ejecutable)

## Instalación de PyInstaller

### Opción 1: En entorno virtual (Recomendado)

```bash
# Activar entorno virtual
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instalar PyInstaller
pip install pyinstaller
```

### Opción 2: Instalación global

```bash
pip install pyinstaller
```

## Compilación Rápida

### Paso 1: Clonar el repositorio (si no lo tienes)

```bash
git clone https://github.com/yelllowcat/ExamenBDD.git
cd ExamenBDD
```

### Paso 2: Compilar

```bash
# Activar entorno virtual
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Compilar usando el archivo de especificación
pyinstaller main.spec
```

### Paso 3: Ubicación del ejecutable

El ejecutable estará en:
```
dist/SistemaBancario       # Linux/Mac
dist/SistemaBancario.exe   # Windows
```

## Compilación por Sistema Operativo

### 🐧 Linux

```bash
# 1. Activar entorno virtual
source .venv/bin/activate

# 2. Instalar PyInstaller (si no está instalado)
pip install pyinstaller

# 3. Compilar
pyinstaller main.spec

# 4. Dar permisos de ejecución
chmod +x dist/SistemaBancario

# 5. Probar el ejecutable
cd dist
./SistemaBancario

# 6. Crear paquete de distribución
cd ..
./crear_paquete.sh
```

**Resultado**: `release/SistemaBancario-Linux-v1.0.tar.gz`

**Contenido del paquete**:
- Ejecutable `SistemaBancario`
- `.env.example` (plantilla de configuración)
- `examenPythonBD.sql` (script de base de datos)
- `README.md` (instrucciones)
- `VERSION.txt` (información de versión)

### 🪟 Windows

```batch
REM 1. Activar entorno virtual
.venv\Scripts\activate

REM 2. Instalar PyInstaller (si no está instalado)
pip install pyinstaller

REM 3. Compilar
pyinstaller main.spec

REM 4. El ejecutable estará en dist\SistemaBancario.exe

REM 5. Probar
cd dist
SistemaBancario.exe
```

**Crear paquete de distribución manualmente**:

1. Crear carpeta `SistemaBancario`
2. Copiar los siguientes archivos:
   ```
   SistemaBancario/
   ├── SistemaBancario.exe
   ├── .env.example
   ├── examenPythonBD.sql
   └── README.md (copiar INSTRUCCIONES_EJECUTABLE.md)
   ```
3. Comprimir en ZIP usando 7-Zip o WinRAR

### 🍎 macOS

```bash
# 1. Activar entorno virtual
source .venv/bin/activate

# 2. Instalar PyInstaller
pip install pyinstaller

# 3. Compilar
pyinstaller main.spec

# 4. Dar permisos de ejecución
chmod +x dist/SistemaBancario

# 5. Probar
cd dist
./SistemaBancario

# 6. Crear paquete
cd ..
tar -czf SistemaBancario-macOS-v1.0.tar.gz \
    dist/SistemaBancario \
    .env.example \
    examenPythonBD.sql \
    INSTRUCCIONES_EJECUTABLE.md
```

## Método Alternativo: Comando Directo

Si no quieres usar el archivo `main.spec`, puedes compilar directamente:

```bash
pyinstaller --onefile \
    --windowed \
    --name "SistemaBancario" \
    --hidden-import=mysql.connector \
    --hidden-import=dotenv \
    --hidden-import=_mysql_connector \
    --add-data ".env.example:." \
    --add-data "examenPythonBD.sql:." \
    main.py
```

**Parámetros explicados**:
- `--onefile`: Crea un solo archivo ejecutable
- `--windowed`: No muestra consola (solo GUI)
- `--name`: Nombre del ejecutable
- `--hidden-import`: Módulos que PyInstaller no detecta automáticamente
- `--add-data`: Archivos adicionales a incluir (formato: `origen:destino`)

## Personalización

### Cambiar el nombre del ejecutable

Edita `main.spec`, línea 28:

```python
name='MiSistemaBancario',  # Cambia aquí
```

### Agregar un ícono

1. Consigue un archivo de ícono:
   - Windows: `.ico`
   - macOS: `.icns`
   - Linux: `.png` (convertir a .ico)

2. Coloca el ícono en la raíz del proyecto

3. Edita `main.spec`, línea 28:

```python
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SistemaBancario',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='icono.ico',  # ← Agregar esta línea
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

### Incluir archivos adicionales

Edita `main.spec`, línea 9:

```python
datas=[
    ('.env.example', '.'),
    ('examenPythonBD.sql', '.'),
    ('logo.png', '.'),           # ← Agregar más archivos
    ('manual.pdf', 'docs'),      # ← En subcarpeta
],
```

### Excluir módulos innecesarios

Para reducir el tamaño del ejecutable, edita `main.spec`, línea 14:

```python
excludes=['test', 'unittest', 'pydoc', 'doctest'],
```

## Estructura del archivo main.spec

El archivo `main.spec` incluido está configurado con:

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],                    # Archivo principal
    pathex=[],
    binaries=[],
    datas=[                         # Archivos adicionales
        ('.env.example', '.'),
        ('examenPythonBD.sql', '.')
    ],
    hiddenimports=[                 # Dependencias ocultas
        'mysql.connector',
        'dotenv',
        '_mysql_connector'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SistemaBancario',         # Nombre del ejecutable
    debug=False,                    # Sin modo debug
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,                       # Comprimir con UPX
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,                  # Sin consola (GUI pura)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

## Solución de Problemas

### Error: "command not found: pyinstaller"

**Causa**: PyInstaller no está instalado o no está en el PATH.

**Solución**:
```bash
# Verificar instalación
pip list | grep pyinstaller

# Instalar si no está
pip install pyinstaller

# O con entorno virtual
source .venv/bin/activate && pip install pyinstaller
```

### Error: "No module named 'mysql'"

**Causa**: PyInstaller no detectó la dependencia de MySQL.

**Solución**: Agregar a `hiddenimports` en `main.spec`:
```python
hiddenimports=[
    'mysql.connector',
    '_mysql_connector',
    'mysql',                # ← Agregar
    'mysql.connector.locales.eng',
],
```

### Error: "No module named 'dotenv'"

**Causa**: Falta la dependencia python-dotenv.

**Solución**:
```bash
pip install python-dotenv
```

Y asegúrate de que esté en `hiddenimports`:
```python
hiddenimports=['mysql.connector', 'dotenv', '_mysql_connector'],
```

### Error: "Failed to execute script"

**Causa**: Error en tiempo de ejecución que no se muestra.

**Solución**: Compilar con modo debug:
```bash
pyinstaller --debug=all main.spec
```

O temporalmente cambiar en `main.spec`:
```python
console=True,  # Cambiar a True para ver errores
```

### El ejecutable es muy grande (~20 MB)

**Esto es normal**, pero puedes reducirlo:

1. **Usar UPX** (compresor, ya habilitado):
```bash
# Instalar UPX
sudo apt install upx-ucl  # Linux
brew install upx          # macOS
choco install upx         # Windows

# Ya está habilitado en main.spec (upx=True)
```

2. **Excluir módulos innecesarios**:
```python
# En main.spec
excludes=[
    'matplotlib',
    'numpy',
    'pandas',
    'scipy',
    'PIL',
],
```

3. **Usar --onedir en lugar de --onefile**:
```bash
# Crea una carpeta con el ejecutable y DLLs separadas
# Más rápido de iniciar, pero más archivos
pyinstaller --onedir main.py
```

### Error en Windows: "VCRUNTIME140.dll not found"

**Causa**: Faltan las bibliotecas de Visual C++.

**Solución**: Instalar [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)

### Error en Linux: "libpython3.X.so not found"

**Causa**: Falta la biblioteca compartida de Python.

**Solución**:
```bash
# Ubuntu/Debian
sudo apt-get install python3-dev

# Fedora
sudo dnf install python3-devel
```

### Error: Tkinter no funciona

**En Linux**, instalar dependencias de Tkinter:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk tk-dev

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

### El ejecutable inicia pero no conecta a MySQL

**Causa**: Falta el archivo `.env` o está mal configurado.

**Solución**:
1. Verificar que existe `.env` en la misma carpeta que el ejecutable
2. Verificar las credenciales en `.env`
3. Verificar que MySQL está corriendo:
```bash
sudo systemctl status mysql  # Linux
```

## Verificación del Ejecutable

### Probar el ejecutable

```bash
# Linux/Mac
cd dist
./SistemaBancario

# Windows
cd dist
SistemaBancario.exe
```

### Verificar dependencias del sistema (Linux)

```bash
ldd dist/SistemaBancario
```

Deberías ver solo bibliotecas estándar del sistema:
```
linux-vdso.so.1
libdl.so.2
libz.so.1
libpthread.so.0
libc.so.6
```

### Verificar tamaño

```bash
ls -lh dist/SistemaBancario
# Debería ser ~20 MB
```

### Verificar que incluye los archivos adicionales

```bash
# Linux/Mac
strings dist/SistemaBancario | grep -i "\.env\|\.sql"

# Deberías ver referencias a .env.example y examenPythonBD.sql
```

## Crear Paquete de Distribución

### Script automático (Linux/Mac)

El proyecto incluye un script para crear el paquete automáticamente:

```bash
chmod +x crear_paquete.sh
./crear_paquete.sh
```

Esto creará: `release/SistemaBancario-Linux-v1.0.tar.gz`

### Manual (Todos los sistemas)

#### Linux/Mac:

```bash
# 1. Crear directorio
mkdir -p release/SistemaBancario

# 2. Copiar archivos
cp dist/SistemaBancario release/SistemaBancario/
cp .env.example release/SistemaBancario/
cp examenPythonBD.sql release/SistemaBancario/
cp INSTRUCCIONES_EJECUTABLE.md release/SistemaBancario/README.md

# 3. Dar permisos
chmod +x release/SistemaBancario/SistemaBancario

# 4. Comprimir
cd release
tar -czf SistemaBancario-Linux-v1.0.tar.gz SistemaBancario/
cd ..
```

#### Windows:

1. Crear carpeta `SistemaBancario`
2. Copiar:
   - `dist\SistemaBancario.exe`
   - `.env.example`
   - `examenPythonBD.sql`
   - `INSTRUCCIONES_EJECUTABLE.md` (renombrar a `README.md`)
3. Clic derecho → Enviar a → Carpeta comprimida (ZIP)

## Distribución

### Contenido del paquete final

```
SistemaBancario/
├── SistemaBancario (o .exe en Windows)
├── .env.example
├── examenPythonBD.sql
├── README.md
└── VERSION.txt (opcional)
```

### Publicar en GitHub Releases

1. **Crear un tag**:
```bash
git tag -a v1.0 -m "Release v1.0 - Sistema Bancario Fintech"
git push origin v1.0
```

2. **Crear el Release en GitHub**:
   - Ve a: https://github.com/TU_USUARIO/ExamenBDD/releases/new
   - Selecciona el tag `v1.0`
   - Título: `Sistema Bancario Fintech v1.0`
   - Descripción: Ver ejemplo abajo
   - Arrastra el archivo `.tar.gz` o `.zip`
   - Click en "Publish release"

**Ejemplo de descripción del release**:

```markdown
## 🏦 Sistema Bancario Fintech v1.0

Primera versión estable del sistema de gestión bancaria.

### ✨ Características

- Registro e inicio de sesión de usuarios
- Creación de múltiples cuentas bancarias
- Transferencias entre cuentas
- Consulta de historial de transacciones

### 📦 Descarga

- **Linux**: SistemaBancario-Linux-v1.0.tar.gz
- **Windows**: SistemaBancario-Windows-v1.0.zip
- **macOS**: SistemaBancario-macOS-v1.0.tar.gz

### 📋 Requisitos

- MySQL 5.7 o superior

### 📖 Instalación

Ver el archivo README.md incluido en el paquete.

### 👥 Usuarios de Prueba

- david@mail.com / hash123
- ana@mail.com / hash456
```

## Compilación Cruzada

**Importante**: PyInstaller **NO** soporta compilación cruzada. Para crear ejecutables para diferentes sistemas operativos, **debes compilar en cada sistema**.

### Opciones para compilar en múltiples plataformas:

#### 1. Máquinas Virtuales

- **VirtualBox** o **VMware**
- Instalar Windows/Linux/macOS en VM
- Compilar en cada sistema

#### 2. GitHub Actions (Automatización)

Crear `.github/workflows/build.yml`:

```yaml
name: Build Executables

on:
  push:
    tags:
      - 'v*'

jobs:
  build-linux:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install mysql-connector-python python-dotenv pyinstaller
      - name: Build
        run: pyinstaller main.spec
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: SistemaBancario-Linux
          path: dist/SistemaBancario

  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install mysql-connector-python python-dotenv pyinstaller
      - name: Build
        run: pyinstaller main.spec
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: SistemaBancario-Windows
          path: dist/SistemaBancario.exe

  build-macos:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install mysql-connector-python python-dotenv pyinstaller
      - name: Build
        run: pyinstaller main.spec
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: SistemaBancario-macOS
          path: dist/SistemaBancario
```

#### 3. Servicios en la Nube

- **AWS EC2**: Crear instancias de Windows/Linux
- **Azure VMs**: Máquinas virtuales
- **Google Cloud**: Compute Engine

## Recursos Adicionales

- [Documentación oficial de PyInstaller](https://pyinstaller.org/en/stable/)
- [PyInstaller en GitHub](https://github.com/pyinstaller/pyinstaller)
- [Guía de solución de problemas](https://github.com/pyinstaller/pyinstaller/wiki/If-Things-Go-Wrong)
- [PyInstaller Hooks](https://github.com/pyinstaller/pyinstaller-hooks-contrib)

## Preguntas Frecuentes

### ¿Puedo compilar para Windows desde Linux?

No, PyInstaller no soporta compilación cruzada. Necesitas compilar en Windows.

### ¿El ejecutable funciona sin Python instalado?

Sí, el ejecutable incluye todo lo necesario. El usuario **NO** necesita tener Python instalado.

### ¿Por qué el ejecutable es tan grande?

Incluye el intérprete de Python y todas las bibliotecas necesarias (~20 MB es normal).

### ¿Puedo reducir el tamaño?

Sí, usando UPX (ya habilitado) y excluyendo módulos innecesarios.

### ¿El antivirus detecta el ejecutable como virus?

A veces sí (falso positivo). Puedes:
- Firmar el ejecutable digitalmente
- Reportar el falso positivo al antivirus
- Distribuir el código fuente también

### ¿Funciona en todas las versiones de Linux?

Generalmente sí, si tienen las mismas bibliotecas base (glibc, etc.).

---

**¡Compilación exitosa!** 🎉

Si tienes problemas, consulta la sección de [Solución de Problemas](#solución-de-problemas) o abre un issue en GitHub.
