CREATE DATABASE bd_laptops;
use bd_laptops;

CREATE TABLE fabricantes(
Id int PRIMARY KEY AUTO_INCREMENT,
nombre varchar(50),
pais varchar(50)
);

CREATE TABLE laptops (
Id int PRIMARY KEY auto_increment,
Procesador varchar(50),
Almacenamiento varchar(50),
Ram varchar(50),
Gpu varchar(50),
TamañoBateria varchar(50),
TamañoPantalla varchar(50),
IdFabricante int,
constraint fk_laptops_fabricantes foreign key (IdFabricante) references fabricantes(Id)
);

select * from fabricantes;

INSERT INTO fabricantes VALUES (1,'HP', 'Argentina');
INSERT INTO fabricantes VALUES (2,'Dell', 'Brasil');
INSERT INTO fabricantes VALUES (3,'Lenovo', 'China');
INSERT INTO fabricantes VALUES (4,'Asus', 'Japon');
INSERT INTO fabricantes VALUES (5,'Acer', 'Taiwán');

select * from laptops; 

INSERT INTO laptops (Procesador, Almacenamiento, Ram, Gpu, TamañoBateria, TamañoPantalla, IdFabricante)
VALUES ('Intel Core i7', '512GB SSD', '16GB', 'NVIDIA GTX 1650', '56Wh', '15.6"', 1);

INSERT INTO laptops (Procesador, Almacenamiento, Ram, Gpu, TamañoBateria, TamañoPantalla, IdFabricante)
VALUES ('AMD Ryzen 5', '256GB SSD', '8GB', 'AMD Radeon Vega 8', '48Wh', '14"', 2);

INSERT INTO laptops (Procesador, Almacenamiento, Ram, Gpu, TamañoBateria, TamañoPantalla, IdFabricante)
VALUES ('Intel Core i5', '1TB HDD', '8GB', 'Intel UHD Graphics', '42Wh', '14"', 3);

INSERT INTO laptops (Procesador, Almacenamiento, Ram, Gpu, TamañoBateria, TamañoPantalla, IdFabricante)
VALUES ('AMD Ryzen 7', '1TB SSD', '16GB', 'NVIDIA RTX 2060', '60Wh', '15.6"', 4);

INSERT INTO laptops (Procesador, Almacenamiento, Ram, Gpu, TamañoBateria, TamañoPantalla, IdFabricante)
VALUES ('Intel Core i9', '2TB SSD', '32GB', 'NVIDIA RTX 3080', '90Wh', '17.3"', 1);

INSERT INTO laptops (Procesador, Almacenamiento, Ram, Gpu, TamañoBateria, TamañoPantalla, IdFabricante)
VALUES ('AMD Ryzen 9', '512GB SSD', '16GB', 'AMD Radeon RX 5700', '57Wh', '15.6"', 5);

INSERT INTO laptops (Procesador, Almacenamiento, Ram, Gpu, TamañoBateria, TamañoPantalla, IdFabricante)
VALUES ('Intel Core i3', '256GB SSD', '4GB', 'Intel UHD Graphics', '35Wh', '13.3"', 2);

INSERT INTO laptops (Procesador, Almacenamiento, Ram, Gpu, TamañoBateria, TamañoPantalla, IdFabricante)
VALUES ('Apple M1', '512GB SSD', '8GB', 'Apple Integrated', '49.9Wh', '13.3"', 4);

INSERT INTO laptops (Procesador, Almacenamiento, Ram, Gpu, TamañoBateria, TamañoPantalla, IdFabricante)
VALUES ('Intel Core i5', '512GB SSD', '8GB', 'NVIDIA MX250', '60Wh', '14"', 3);

INSERT INTO laptops (Procesador, Almacenamiento, Ram, Gpu, TamañoBateria, TamañoPantalla, IdFabricante)
VALUES ('AMD Ryzen 5', '1TB SSD', '16GB', 'NVIDIA GTX 1660', '65Wh', '15.6"', 5);




select id, Procesador, Almacenamiento
from laptops
where id = 5;

select id, ram, gpu
from laptops;

select id, TamañoBateria, TamañoPantalla
from laptops;

select id, nombre
from fabricantes
where nombre like 'Dell';

select id, pais
from fabricantes
where id = 3;


Insert into fabricantes values (6,'samsung','españa' )