# Cómo Compilar para Windows 🪟

Tienes 3 opciones para crear el ejecutable de Windows.

## Opción 1: GitHub Actions (Automático) ⭐ RECOMENDADO

GitHub compilará automáticamente para Windows, Linux y macOS.

### Pasos:

1. **Subir el workflow a GitHub**:
```bash
git add .github/workflows/build.yml
git commit -m "Add GitHub Actions workflow for multi-platform builds"
git push origin main
```

2. **Ejecutar el workflow manualmente**:
   - Ve a tu repositorio en GitHub
   - Click en **"Actions"**
   - Selecciona **"Build Executables"**
   - Click en **"Run workflow"** → **"Run workflow"**
   
3. **Esperar a que termine** (5-10 minutos)

4. **Descargar los ejecutables**:
   - En la página del workflow, verás 3 artifacts:
     - `SistemaBancario-Windows` (Windows .exe)
     - `SistemaBancario-Linux` (Linux)
     - `SistemaBancario-macOS` (macOS)
   - Click en cada uno para descargar

### Ventajas:
- ✅ Compila para 3 sistemas operativos
- ✅ Totalmente automático
- ✅ No necesitas Windows
- ✅ Gratis con GitHub

---

## Opción 2: Compilar en Windows Directamente

Si tienes acceso a una máquina Windows:

### Requisitos:
- Windows 10/11
- Python 3.8+
- Git

### Pasos:

1. **Clonar el repositorio**:
```cmd
git clone https://github.com/yelllowcat/ExamenBDD.git
cd ExamenBDD
```

2. **Crear entorno virtual**:
```cmd
python -m venv .venv
.venv\Scripts\activate
```

3. **Instalar dependencias**:
```cmd
pip install mysql-connector-python python-dotenv pyinstaller
```

4. **Compilar**:
```cmd
pyinstaller main.spec
```

5. **El ejecutable estará en**:
```
dist\SistemaBancario.exe
```

6. **Crear paquete de distribución**:
```cmd
mkdir SistemaBancario-Windows
copy dist\SistemaBancario.exe SistemaBancario-Windows\
copy .env.example SistemaBancario-Windows\
copy examenPythonBD.sql SistemaBancario-Windows\
copy INSTRUCCIONES_EJECUTABLE.md SistemaBancario-Windows\README.md

REM Comprimir en ZIP
powershell Compress-Archive -Path SistemaBancario-Windows -DestinationPath SistemaBancario-Windows-v1.0.zip
```

---

## Opción 3: Usar Máquina Virtual

Si no tienes Windows pero quieres compilar localmente:

### Requisitos:
- VirtualBox o VMware
- ISO de Windows 10/11

### Pasos:

1. **Instalar VirtualBox**:
   - Descargar: https://www.virtualbox.org/

2. **Descargar Windows 10 ISO**:
   - https://www.microsoft.com/software-download/windows10
   - Puedes usar la versión de evaluación (90 días gratis)

3. **Crear VM**:
   - Abrir VirtualBox
   - Nueva VM
   - Tipo: Microsoft Windows
   - Versión: Windows 10 (64-bit)
   - RAM: 4 GB mínimo
   - Disco: 50 GB

4. **Instalar Windows en la VM**

5. **Dentro de Windows**:
   - Instalar Python: https://www.python.org/downloads/
   - Instalar Git: https://git-scm.com/download/win
   - Seguir los pasos de la Opción 2

---

## Comparación de Opciones

| Opción | Tiempo | Dificultad | Costo | Sistemas |
|--------|--------|------------|-------|----------|
| **GitHub Actions** | 10 min | Fácil | Gratis | Windows, Linux, macOS |
| **Windows directo** | 5 min | Fácil | Gratis* | Solo Windows |
| **Máquina Virtual** | 2 horas | Media | Gratis | Solo Windows |

*Requiere acceso a Windows

---

## Resultado Esperado

Después de compilar, tendrás:

### Windows:
```
SistemaBancario-Windows-v1.0.zip
└── SistemaBancario-Windows/
    ├── SistemaBancario.exe    ← Ejecutable
    ├── .env.example
    ├── examenPythonBD.sql
    └── README.md
```

### Linux:
```
SistemaBancario-Linux-v1.0.tar.gz
└── SistemaBancario-Linux/
    ├── SistemaBancario        ← Ejecutable (sin extensión)
    ├── .env.example
    ├── examenPythonBD.sql
    └── README.md
```

### macOS:
```
SistemaBancario-macOS-v1.0.tar.gz
└── SistemaBancario-macOS/
    ├── SistemaBancario        ← Ejecutable (sin extensión)
    ├── .env.example
    ├── examenPythonBD.sql
    └── README.md
```

---

## Crear Paquete Completo para Entrega

Una vez que tengas los ejecutables de todos los sistemas:

```bash
# Crear estructura
mkdir EntregaCompleta
mkdir EntregaCompleta/CodigoFuente
mkdir EntregaCompleta/Ejecutables

# Copiar código fuente
cp -r . EntregaCompleta/CodigoFuente/
# (excluir .git, .venv, etc.)

# Copiar ejecutables
cp SistemaBancario-Windows-v1.0.zip EntregaCompleta/Ejecutables/
cp SistemaBancario-Linux-v1.0.tar.gz EntregaCompleta/Ejecutables/
cp SistemaBancario-macOS-v1.0.tar.gz EntregaCompleta/Ejecutables/

# Crear README
cat > EntregaCompleta/README.txt << 'EOF'
Sistema Bancario Fintech
========================

Integrante: David González

Contenido:
- CodigoFuente/: Código fuente completo
- Ejecutables/: Ejecutables para Windows, Linux y macOS

Instrucciones en CodigoFuente/README.md
EOF

# Comprimir todo
zip -r EntregaCompleta.zip EntregaCompleta/
```

---

## Solución de Problemas

### Error: "VCRUNTIME140.dll not found" (Windows)

**Solución**: Instalar Visual C++ Redistributable
- https://aka.ms/vs/17/release/vc_redist.x64.exe

### Error: "pyinstaller: command not found" (Windows)

**Solución**:
```cmd
python -m pip install --upgrade pip
pip install pyinstaller
```

### El ejecutable no inicia en Windows

**Solución**: Compilar con modo debug:
```cmd
pyinstaller --debug=all main.spec
```

---

## Recomendación Final

Para entregar al profesor, usa **GitHub Actions** (Opción 1):

1. ✅ Compila para 3 sistemas operativos
2. ✅ Totalmente automático
3. ✅ No necesitas Windows
4. ✅ Resultados profesionales

Luego crea el paquete `EntregaCompleta.zip` con:
- Código fuente
- Ejecutables para Windows, Linux y macOS
- Documentación completa

---

**¿Necesitas ayuda?** Abre un issue en GitHub o consulta la documentación.
