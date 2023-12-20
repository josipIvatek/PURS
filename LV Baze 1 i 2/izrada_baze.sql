DROP DATABASE IF EXISTS lvj6;
CREATE DATABASE lvj6;
USE lvj6;

CREATE TABLE temperatura(
id INT PRIMARY KEY AUTO_INCREMENT,
datum DATETIME,
vrijednost int
);

INSERT INTO temperatura(datum, vrijednost) VALUES
	('2023-10-10 12:20:35', '23'),
    ('2023-10-11 11:20:35', '20'),
    ('2023-10-12 10:20:35', '22'),
    ('2023-10-13 09:20:35', '18');
    
CREATE TABLE ovlasti(
id INT PRIMARY KEY AUTO_INCREMENT,
naziv VARCHAR(100)
);

INSERT INTO ovlasti(naziv) VALUES
('Administrator'),
('Korisnik');

CREATE TABLE korisnik(
id INT PRIMARY KEY AUTO_INCREMENT,
ime CHAR(50),
prezime VARCHAR(50),
username VARCHAR(50),
password VARCHAR(50),
id_ovlasti INT,
FOREIGN KEY (id_ovlasti) REFERENCES ovlasti(id) ON UPDATE CASCADE ON DELETE SET NULL
);

INSERT INTO korisnik(ime, prezime, username, password, id_ovlasti) VALUES
('Ladislav','Kovač','lkovac','1234', '1'),
('Valentina', 'Ilić', 'vilic', 'abcd', '1'),
('Danko','Kovac','dkovac','ab12', '2'),
('Katija', 'Kolar', 'kkolar', '12ab', '2');

CREATE TABLE korisnikove_temperature(
id_korisnika INT,
FOREIGN KEY (id_korisnika) REFERENCES korisnik(id) ON UPDATE CASCADE ON DELETE CASCADE,
id_temperature INT,
FOREIGN KEY (id_temperature) REFERENCES temperatura(id) ON UPDATE CASCADE ON DELETE CASCADE,
PRIMARY KEY(id_korisnika, id_temperature)
);

INSERT INTO korisnikove_temperature(id_korisnika, id_temperature) VALUES
('1','1'),
('2','1'),
('1','2'),
('2','2'),
('1','3');

DROP USER IF EXISTS app;
CREATE USER app@'%' IDENTIFIED BY '1234';
GRANT SELECT, INSERT, UPDATE, DELETE ON lvj6.* TO app@'%';

    

