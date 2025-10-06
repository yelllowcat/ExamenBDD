drop database fintech;
create database fintech;
use  fintech;
CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(100) UNIQUE NOT NULL,
  nombre VARCHAR(50) NOT NULL,
  apellidos VARCHAR(100) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE cuentas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  numero_cuenta varchar(255) UNIQUE NOT NULL,
  saldo DECIMAL(12,2) DEFAULT 0.00,
  estado ENUM('ACTIVA', 'BLOQUEADA') DEFAULT 'ACTIVA',
  usuario_id INT NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
CREATE TABLE movimientos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  tipo_movimiento ENUM('APERTURA', 'TRANSFERENCIA_ENTRADA', 'TRANSFERENCIA_SALIDA') NOT NULL,
  cuenta_salida_id INT NULL,
  cuenta_entrada_id INT NULL,
  monto DECIMAL(12,2) NOT NULL,
  fecha_operacion DATETIME DEFAULT CURRENT_TIMESTAMP,
  nota VARCHAR(255),
  FOREIGN KEY (cuenta_salida_id) REFERENCES cuentas(id),
  FOREIGN KEY (cuenta_entrada_id) REFERENCES cuentas(id),
CONSTRAINT chk_monto CHECK (monto >=0)
);
-- 1. Procedimiento para registrar un usuario nuevo
DELIMITER $$

CREATE PROCEDURE registrar_usuario(
    IN p_email VARCHAR(100),
    IN p_nombre VARCHAR(50),
    IN p_apellidos VARCHAR(100),
    IN p_password_hash VARCHAR(255)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Error al registrar usuario';
    END;
    
    START TRANSACTION;
    
    -- Validar que el email no esté vacío
    IF p_email IS NULL OR p_email = '' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El email es obligatorio';
    END IF;
    
    -- Validar que el nombre no esté vacío
    IF p_nombre IS NULL OR p_nombre = '' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El nombre es obligatorio';
    END IF;
    
    -- Insertar usuario
    INSERT INTO usuarios (email, nombre, apellidos, password_hash)
    VALUES (p_email, p_nombre, p_apellidos, p_password_hash);
    
    COMMIT;
END$$

DELIMITER ;

-- 2. Procedimiento para abrir una cuenta bancaria
DELIMITER $$

CREATE PROCEDURE abrir_cuenta(
    IN p_numero_cuenta VARCHAR(255),
    IN p_saldo_inicial DECIMAL(12,2),
    IN p_usuario_id INT
)
BEGIN
    DECLARE v_cuenta_id INT;
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Error al abrir cuenta';
    END;
    
    START TRANSACTION;
    
    -- Validar que el usuario exista
    IF NOT EXISTS (SELECT 1 FROM usuarios WHERE id = p_usuario_id) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El usuario no existe';
    END IF;
    
    -- Validar saldo inicial no negativo
    IF p_saldo_inicial < 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El saldo inicial no puede ser negativo';
    END IF;
    
    -- Crear cuenta
    INSERT INTO cuentas (numero_cuenta, saldo, usuario_id)
    VALUES (p_numero_cuenta, p_saldo_inicial, p_usuario_id);
    
    SET v_cuenta_id = LAST_INSERT_ID();
    
    -- Registrar movimiento de apertura
    INSERT INTO movimientos (tipo_movimiento, cuenta_entrada_id, monto, nota)
    VALUES ('APERTURA', v_cuenta_id, p_saldo_inicial, 'Apertura de cuenta');
    
    COMMIT;
END$$

DELIMITER ;

-- 3. Procedimiento para transferir dinero entre cuentas
DELIMITER $$

CREATE PROCEDURE transferir_dinero(
    IN p_cuenta_salida_id INT,
    IN p_cuenta_entrada_id INT,
    IN p_monto DECIMAL(12,2),
    IN p_nota VARCHAR(255)
)
BEGIN
    DECLARE v_saldo_origen DECIMAL(12,2);
    DECLARE v_estado_origen VARCHAR(20);
    DECLARE v_estado_destino VARCHAR(20);
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Error al realizar transferencia';
    END;
    
    START TRANSACTION;
    
    -- Validar monto positivo
    IF p_monto <= 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El monto debe ser mayor a cero';
    END IF;
    
    -- Validar que las cuentas sean diferentes
    IF p_cuenta_salida_id = p_cuenta_entrada_id THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'No se puede transferir a la misma cuenta';
    END IF;
    
    -- Validar que la cuenta de salida exista y esté activa
    SELECT saldo, estado INTO v_saldo_origen, v_estado_origen
    FROM cuentas
    WHERE id = p_cuenta_salida_id
    FOR UPDATE;
    
    IF v_estado_origen IS NULL THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'La cuenta de origen no existe';
    END IF;
    
    IF v_estado_origen != 'ACTIVA' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'La cuenta de origen no está activa';
    END IF;
    
    -- Validar que la cuenta de entrada exista y esté activa
    SELECT estado INTO v_estado_destino
    FROM cuentas
    WHERE id = p_cuenta_entrada_id
    FOR UPDATE;
    
    IF v_estado_destino IS NULL THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'La cuenta de destino no existe';
    END IF;
    
    IF v_estado_destino != 'ACTIVA' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'La cuenta de destino no está activa';
    END IF;
    
    -- Validar fondos suficientes
    IF v_saldo_origen < p_monto THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Fondos insuficientes';
    END IF;
    
    -- Realizar transferencia
    UPDATE cuentas SET saldo = saldo - p_monto WHERE id = p_cuenta_salida_id;
    UPDATE cuentas SET saldo = saldo + p_monto WHERE id = p_cuenta_entrada_id;
    
    -- Registrar movimiento de salida
    INSERT INTO movimientos (tipo_movimiento, cuenta_salida_id, cuenta_entrada_id, monto, nota)
    VALUES ('TRANSFERENCIA_SALIDA', p_cuenta_salida_id, p_cuenta_entrada_id, p_monto, p_nota);
    
    -- Registrar movimiento de entrada
    INSERT INTO movimientos (tipo_movimiento, cuenta_salida_id, cuenta_entrada_id, monto, nota)
    VALUES ('TRANSFERENCIA_ENTRADA', p_cuenta_salida_id, p_cuenta_entrada_id, p_monto, p_nota);
    
    COMMIT;
END$$

DELIMITER ;

-- Procedimiento para iniciar sesión
DELIMITER $$

CREATE PROCEDURE iniciar_sesion(
    IN p_email VARCHAR(100),
    IN p_password_hash VARCHAR(255)
)
BEGIN
    DECLARE v_usuario_id INT;
    DECLARE v_nombre VARCHAR(50);
    DECLARE v_apellidos VARCHAR(100);
    DECLARE v_password_hash VARCHAR(255);
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Error al iniciar sesión';
    END;
    
    -- Validar que el email no esté vacío
    IF p_email IS NULL OR p_email = '' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El email es obligatorio';
    END IF;
    
    -- Validar que el password no esté vacío
    IF p_password_hash IS NULL OR p_password_hash = '' THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'La contraseña es obligatoria';
    END IF;
    
    -- Buscar usuario por email
    SELECT id, nombre, apellidos, password_hash
    INTO v_usuario_id, v_nombre, v_apellidos, v_password_hash
    FROM usuarios
    WHERE email = p_email;
    
    -- Validar que el usuario exista
    IF v_usuario_id IS NULL THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Credenciales inválidas';
    END IF;
    
    -- Validar contraseña
    IF v_password_hash != p_password_hash THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Credenciales inválidas';
    END IF;
    
    -- Retornar información del usuario
    SELECT 
        v_usuario_id AS id,
        p_email AS email,
        v_nombre AS nombre,
        v_apellidos AS apellidos,
        'Inicio de sesión exitoso' AS mensaje;
        
END$$

DELIMITER ;

-- PRUEBAS DEL PROCEDIMIENTO
-- -----------------------------------
select * from usuarios;
-- Inicio de sesión exitoso
CALL iniciar_sesion(
    'juan.perez@email.com',
    '$2y$10$abcdefghijklmnopqrstuvwxyz123456'
);

-- Inicio de sesión con otro usuario
CALL iniciar_sesion(
    'maria.lopez@email.com',
    '$2y$10$zyxwvutsrqponmlkjihgfedcba654321'
);
