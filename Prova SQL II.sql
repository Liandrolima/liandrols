create database InformacoesPessoais
default character set utf8mb4
default collate utf8mb4_general_ci;

USE InformacoesPessoais;

create table pessoas(
id int not null auto_increment,
nome_completo varchar(100) not null,
nascimento date,
genero enum('M', 'F'),
nascionalidade varchar(50) default 'Brasil',
endereco varchar(255) not null,
email varchar(60) not null unique,
estado_civil varchar(30),
nome_do_pai varchar(100),
nome_da_mae varchar(100),
peso decimal(5,2),
altura decimal(3,2),
primary key(id)
) default charset=utf8mb4;

INSERT INTO pessoas (nome_completo, nascimento, genero, nacionalidade, endereco, email, estado_civil, nome_do_pai, nome_da_mae, peso, altura)
VALUES
    ('João Silva', '1990-05-15', 'M', 'Brasil', 'Rua Principal, 123', 'joao@example.com', 'Solteiro', 'José Silva', 'Maria Silva', 75.5, 1.80),
    ('Maria Souza', '1985-09-20', 'F', 'Brasil', 'Avenida Central, 456', 'maria@example.com', 'Casada', 'Antônio Souza', 'Ana Souza', 65.2, 1.65),
    ('Pedro Santos', '2000-03-10', 'M', 'Brasil', 'Rua da Paz, 789', 'pedro@example.com', 'Solteiro', 'Carlos Santos', 'Laura Santos', 80.0, 1.75);
select * from pessoas;

UPDATE pessoas
SET nome_completo = 'João Silva',
    nascimento = '1985-05-15',
    genero = 'M',
    nacionalidade = 'Brasil',
    email = 'joao_silva@example.com',
    estado_civil = 'Solteiro',
    nome_do_pai = 'José Silva',
    nome_da_mae = 'Maria Silva'
WHERE id = 1;

DELETE FROM pessoas WHERE id = 2; 



