# Guía de Compilación del Ejecutable 🔨

Esta guía explica cómo compilar el Sistema Bancario Fintech en un ejecutable para diferentes sistemas operativos.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes)
- PyInstaller

## Instalación de PyInstaller

### En entorno virtual (recomendado)

```bash
# Activar entorno virtual
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Instalar PyInstaller
pip install pyinstaller
```

### Instalación global

```bash
pip install pyinstaller
```

## Compilación

### Método 1: Usando el archivo .spec (Recomendado)

El proyecto incluye un archivo `main.spec` preconfigurado:

```bash
# Activar entorno virtual
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Compilar
pyinstaller main.spec
```

El ejecutable estará en: `dist/SistemaBancario`

### Método 2: Comando directo

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

## Compilación por Sistema Operativo

### 🐧 Linux

```bash
# 1. Activar entorno virtual
source .venv/bin/activate

# 2. Compilar
pyinstaller main.spec

# 3. Dar permisos de ejecución
chmod +x dist/SistemaBancario

# 4. Crear paquete de distribución
./crear_paquete.sh
```

**Resultado**: `release/SistemaBancario-Linux-v1.0.tar.gz`

### 🪟 Windows

```batch
REM 1. Activar entorno virtual
.venv\Scripts\activate

REM 2. Compilar
pyinstaller main.spec

REM 3. El ejecutable estará en dist\SistemaBancario.exe
```

**Crear paquete manualmente**:
1. Crear carpeta `SistemaBancario`
2. Copiar:
   - `dist\SistemaBancario.exe`
   - `.env.example`
   - `examenPythonBD.sql`
   - `INSTRUCCIONES_EJECUTABLE.md`
3. Comprimir en ZIP

### 🍎 macOS

```bash
# 1. Activar entorno virtual
source .venv/bin/activate

# 2. Compilar
pyinstaller main.spec

# 3. Dar permisos de ejecución
chmod +x dist/SistemaBancario

# 4. Crear paquete
tar -czf SistemaBancario-macOS-v1.0.tar.gz dist/SistemaBancario .env.example examenPythonBD.sql INSTRUCCIONES_EJECUTABLE.md
```

## Estructura del archivo main.spec

El archivo `main.spec` está configurado con:

```python
# Dependencias ocultas necesarias
hiddenimports=['mysql.connector', 'dotenv', '_mysql_connector']

# Archivos adicionales a incluir
datas=[('.env.example', '.'), ('examenPythonBD.sql', '.')]

# Nombre del ejecutable
name='SistemaBancario'

# Sin consola (GUI pura)
console=False
```

## Personalización

### Cambiar el nombre del ejecutable

Edita `main.spec`, línea 28:

```python
name='TuNombreAqui',
```

### Agregar un ícono

1. Consigue un archivo `.ico` (Windows) o `.icns` (macOS)
2. Edita `main.spec`:

```python
exe = EXE(
    ...
    icon='ruta/a/tu/icono.ico',  # Agregar esta línea
    ...
)
```

### Incluir archivos adicionales

Edita `main.spec`, línea 9:

```python
datas=[
    ('.env.example', '.'),
    ('examenPythonBD.sql', '.'),
    ('tu_archivo.txt', '.'),  # Agregar más archivos
],
```

## Solución de Problemas

### Error: "command not found: pyinstaller"

**Solución**:
```bash
pip install pyinstaller
# o
source .venv/bin/activate && pip install pyinstaller
```

### Error: "No module named 'mysql'"

**Solución**: Agregar a `hiddenimports` en `main.spec`:
```python
hiddenimports=['mysql.connector', '_mysql_connector', 'mysql'],
```

### Error: "Failed to execute script"

**Solución**: Compilar con modo debug para ver errores:
```bash
pyinstaller --debug=all main.spec
```

### El ejecutable es muy grande

**Soluciones**:

1. **Usar UPX** (compresor):
```bash
# Instalar UPX
sudo apt install upx  # Linux
brew install upx      # macOS

# Ya está habilitado en main.spec (upx=True)
```

2. **Excluir módulos innecesarios**:
```python
# En main.spec
excludes=['matplotlib', 'numpy', 'pandas'],  # Módulos que no usas
```

### Error en Windows: "VCRUNTIME140.dll not found"

**Solución**: Instalar [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)

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

### Verificar dependencias (Linux)

```bash
ldd dist/SistemaBancario
```

### Verificar tamaño

```bash
ls -lh dist/SistemaBancario
```

## Crear Paquete de Distribución

### Script automático (Linux/Mac)

```bash
chmod +x crear_paquete.sh
./crear_paquete.sh
```

### Manual

1. Crear carpeta `SistemaBancario/`
2. Copiar:
   - Ejecutable (`dist/SistemaBancario`)
   - `.env.example`
   - `examenPythonBD.sql`
   - `INSTRUCCIONES_EJECUTABLE.md` (renombrar a `README.md`)
3. Comprimir:
   ```bash
   # Linux/Mac
   tar -czf SistemaBancario-v1.0.tar.gz SistemaBancario/
   
   # Windows
   # Usar 7-Zip o WinRAR para crear .zip
   ```

## Distribución

### Contenido del paquete final

```
SistemaBancario/
├── SistemaBancario (o .exe en Windows)
├── .env.example
├── examenPythonBD.sql
├── README.md (instrucciones de instalación)
└── VERSION.txt (opcional)
```

### Publicar en GitHub Releases

1. Crear un tag:
```bash
git tag -a v1.0 -m "Release v1.0"
git push origin v1.0
```

2. Ir a GitHub → Releases → New Release
3. Subir el archivo comprimido
4. Agregar notas de la versión

## Compilación Cruzada

**Nota**: PyInstaller NO soporta compilación cruzada. Para crear ejecutables para diferentes sistemas operativos, debes compilar en cada sistema.

### Opciones:

1. **Máquinas virtuales**: Usar VirtualBox/VMware
2. **GitHub Actions**: Automatizar compilación en la nube
3. **Docker**: Usar contenedores para cada OS

## Automatización con GitHub Actions

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
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt pyinstaller
      - run: pyinstaller main.spec
      - uses: actions/upload-artifact@v2
        with:
          name: SistemaBancario-Linux
          path: dist/SistemaBancario

  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt pyinstaller
      - run: pyinstaller main.spec
      - uses: actions/upload-artifact@v2
        with:
          name: SistemaBancario-Windows
          path: dist/SistemaBancario.exe
```

## Recursos Adicionales

- [Documentación PyInstaller](https://pyinstaller.org/en/stable/)
- [PyInstaller GitHub](https://github.com/pyinstaller/pyinstaller)
- [Troubleshooting Guide](https://github.com/pyinstaller/pyinstaller/wiki/If-Things-Go-Wrong)

---

**¡Compilación exitosa!** 🎉

Si tienes problemas, consulta la sección de Solución de Problemas o abre un issue en GitHub.
