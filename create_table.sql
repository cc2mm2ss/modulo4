CREATE TABLE parametros (
  CIUDAD VARCHAR(50)
);

CREATE TABLE salida (
	FECHA DATE,
	CIUDAD VARCHAR(50),
	TEMPERATURA DECIMAL(3,2),
	SENSACION DECIMAL(3,2)
);

INSERT INTO parametros(CIUDAD) VALUES('Buenos Aires');

COMMIT;

