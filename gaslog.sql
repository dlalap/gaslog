PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE GAS(
ID INT PRIMARY KEY NOT NULL,
MILEAGE INT NOT NULL,
DATE NUMERIC NOT NULL,
GALLONS REAL NOT NULL,
COST REAL NOT NULL);
INSERT INTO GAS VALUES(1,274767,122217,8.2910000000000003694,24.859999999999999431);
COMMIT;
