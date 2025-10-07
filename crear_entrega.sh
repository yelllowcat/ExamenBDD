#!/bin/bash
# Script para crear paquete de entrega completo

echo "📦 Creando paquete de entrega para el profesor..."

# Crear estructura de directorios
mkdir -p EntregaExamen/CodigoFuente
mkdir -p EntregaExamen/Ejecutable

echo "📁 Copiando código fuente..."
# Copiar código fuente (sin archivos innecesarios)
rsync -av --exclude='.git' \
          --exclude='.venv' \
          --exclude='__pycache__' \
          --exclude='build' \
          --exclude='dist' \
          --exclude='release' \
          --exclude='.env' \
          --exclude='*.pyc' \
          --exclude='path' \
          --exclude='EntregaExamen' \
          --exclude='EntregaExamen.zip' \
          ./ EntregaExamen/CodigoFuente/

echo "🔧 Copiando ejecutable..."
# Copiar ejecutable si existe
if [ -f "dist/SistemaBancario" ]; then
    cp dist/SistemaBancario EntregaExamen/Ejecutable/
    cp .env.example EntregaExamen/Ejecutable/
    cp examenPythonBD.sql EntregaExamen/Ejecutable/
    cp INSTRUCCIONES_EJECUTABLE.md EntregaExamen/Ejecutable/README.md
    chmod +x EntregaExamen/Ejecutable/SistemaBancario
else
    echo "⚠️  Ejecutable no encontrado. Ejecuta 'pyinstaller main.spec' primero."
fi

# Crear archivo de información
cat > EntregaExamen/LEEME.txt << 'EOF'
╔════════════════════════════════════════════════════════════════╗
║          SISTEMA BANCARIO FINTECH - EXAMEN BDD                 ║
║                                                                ║
║  Integrante: David González (Responsable)                     ║
╚════════════════════════════════════════════════════════════════╝

📂 CONTENIDO DE ESTA ENTREGA:

1. CodigoFuente/
   - Código fuente completo del proyecto
   - Arquitectura MVC (Modelo-Vista-Controlador)
   - Script SQL con tablas, procedimientos y datos de prueba
   - README.md con instrucciones completas
   
2. Ejecutable/ (opcional)
   - Ejecutable compilado para Linux
   - Listo para ejecutar (requiere MySQL)
   - Instrucciones de instalación incluidas

═══════════════════════════════════════════════════════════════

🚀 OPCIÓN 1: EJECUTAR DESDE CÓDIGO FUENTE (Recomendado)

1. Requisitos:
   - Python 3.8+
   - MySQL 5.7+

2. Instalación:
   cd CodigoFuente
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   pip install mysql-connector-python python-dotenv

3. Configurar Base de Datos:
   mysql -u root -p < examenPythonBD.sql

4. Configurar .env:
   cp .env.example .env
   # Editar .env con tus credenciales de MySQL

5. Ejecutar:
   python main.py

═══════════════════════════════════════════════════════════════

🎯 OPCIÓN 2: EJECUTAR DESDE EJECUTABLE (Solo Linux)

1. Requisitos:
   - MySQL 5.7+

2. Instalación:
   cd Ejecutable
   mysql -u root -p < examenPythonBD.sql
   cp .env.example .env
   # Editar .env con tus credenciales

3. Ejecutar:
   ./SistemaBancario

═══════════════════════════════════════════════════════════════

👤 USUARIOS DE PRUEBA:

Email: david@mail.com    | Contraseña: hash123
Email: ana@mail.com      | Contraseña: hash456
Email: luis@mail.com     | Contraseña: hash789
Email: carla@mail.com    | Contraseña: hash101

═══════════════════════════════════════════════════════════════

📋 CARACTERÍSTICAS IMPLEMENTADAS:

✅ Registro e inicio de sesión de usuarios
✅ Creación de cuentas bancarias (Apertura/Depósito)
✅ Transferencias entre cuentas
✅ Consulta de historial de movimientos
✅ Validaciones de negocio (fondos, cuentas activas, etc.)
✅ Procedimientos almacenados en MySQL
✅ Arquitectura MVC
✅ Interfaz gráfica con Tkinter

═══════════════════════════════════════════════════════════════

📖 DOCUMENTACIÓN:

- CodigoFuente/README.md: Instrucciones completas
- CodigoFuente/COMPILAR.md: Cómo compilar el ejecutable
- Ejecutable/README.md: Instrucciones del ejecutable

═══════════════════════════════════════════════════════════════

Para más información, consultar el README.md en CodigoFuente/

EOF

# Crear archivo ZIP
echo "🗜️  Comprimiendo..."
zip -r EntregaExamen.zip EntregaExamen/

# Limpiar directorio temporal
rm -rf EntregaExamen/

echo ""
echo "✅ ¡Paquete creado exitosamente!"
echo ""
echo "📦 Archivo: EntregaExamen.zip"
echo "📊 Tamaño: $(du -h EntregaExamen.zip | cut -f1)"
echo ""
echo "📤 Listo para entregar al profesor"
