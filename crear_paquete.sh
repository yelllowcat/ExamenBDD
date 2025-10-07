#!/bin/bash
# Script para crear paquete de distribución

echo "Creando paquete de distribución..."

# Crear directorio de distribución
mkdir -p release/SistemaBancario

# Copiar el ejecutable
cp dist/SistemaBancario release/SistemaBancario/

# Copiar archivos necesarios
cp .env.example release/SistemaBancario/
cp examenPythonBD.sql release/SistemaBancario/
cp INSTRUCCIONES_EJECUTABLE.md release/SistemaBancario/README.md

# Crear archivo de versión
echo "Sistema Bancario Fintech v1.0" > release/SistemaBancario/VERSION.txt
echo "Fecha de compilación: $(date)" >> release/SistemaBancario/VERSION.txt

# Dar permisos de ejecución
chmod +x release/SistemaBancario/SistemaBancario

# Crear archivo comprimido
cd release
tar -czf SistemaBancario-Linux-v1.0.tar.gz SistemaBancario/
cd ..

echo "✅ Paquete creado exitosamente en: release/SistemaBancario-Linux-v1.0.tar.gz"
echo ""
echo "Contenido del paquete:"
ls -lh release/SistemaBancario/
