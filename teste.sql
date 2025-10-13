drop database if exists teste;
create database teste;

use teste;

create table servidor (
id int auto_increment primary key,
apelido varchar(100),
nome_maquina varchar(100) unique
);

create table componente (
id int auto_increment primary key,
tipo VARCHAR(40) unique,
numero_serie INT, /* Armazenará se é o componete 01, 02, 03, etc */
apelido varchar(20),
dt_cadastro datetime default current_timestamp,
ativo tinyint default 1,
fk_servidor int,
foreign key (fk_servidor) references servidor(id)
);

create table especificacao_componente (
id int auto_increment primary key,
nome_especificacao varchar(100),
valor varchar(100),
fk_componente int not null,
dt_cadastro datetime default current_timestamp,
foreign key (fk_componente) references componente(id)
);

create table medicao (
id int auto_increment primary key,
nome_medicao varchar(20),
medicao varchar(20),
unidade_medida varchar(100),
fk_componente int not null,
foreign key (fk_componente) references componente(id)
);

Select * from servidor;
select * from componente;	
select * from especificacao_componente;
