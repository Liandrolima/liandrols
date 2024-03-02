create database loja_online
default character set utf8mb4
default collate utf8mb4_general_ci;
USE loja_online;

create table produtos(
id_produto INT PRIMARY KEY auto_increment,
nome varchar(100) not null,
preco DECIMAL(10,2),
quantidade_estoque INT NOT NULL,
CONSTRAINT chk_preco_positivo CHECK (preco > 0)
) default charset=utf8mb4;

create table clientes(
id_clientes INT PRIMARY KEY auto_increment,
nome varchar(100) not null,
email varchar(60) not null unique,
historico_compras text
) default charset=utf8mb4;

create table pedidos(
id_pedidos INT PRIMARY KEY auto_increment,
data_pedido DATE,
id_cliente INT,
status_pedido VARCHAR(50),
FOREIGN KEY (id_cliente) REFERENCES clientes(id_clientes)
) default charset=utf8mb4;

create table item_pedidos(
id_item_pedidos INT PRIMARY KEY auto_increment,
id_pedido INT,
id_produto INT,
quantidade INT NOT NULL,
CONSTRAINT ll_id_pedido FOREIGN KEY (id_pedido)
	REFERENCES pedidos (Id_pedidos) ON DELETE CASCADE,
CONSTRAINT ll_id_produto FOREIGN KEY (id_produto)
	REFERENCES produtos (id_produto) ON DELETE CASCADE
) default charset=utf8mb4;

ALTER TABLE item_pedidos DROP FOREIGN KEY ll_id_produto;

ALTER TABLE produtos MODIFY COLUMN id_produto INT NOT NULL AUTO_INCREMENT;

ALTER TABLE item_pedidos ADD CONSTRAINT ll_id_produto FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);

INSERT INTO produtos (nome, preco, quantidade_estoque)
VALUES
    ('Camiseta', 25.99, 50), ('Calça Jeans', 49.99, 30), ('Tênis', 79.99, 20), ('Boné', 15.99, 100), ('Mochila', 39.99, 40),
    ('Óculos de Sol', 29.99, 60), ('Relógio', 99.99, 15), ('Bolsa', 34.99, 25), ('Jaqueta', 89.99, 10), ('Sapato Social', 59.99, 35);

INSERT INTO clientes (nome, email, historico_compras)
VALUES
    ('João Silva', 'joao@example.com', 'Camiseta, Calça Jeans, Tênis'),
    ('Maria Souza', 'maria@example.com', 'Tênis, Boné, Mochila'),
    ('Pedro Santos', 'pedro@example.com', 'Relógio, Bolsa'),
    ('Ana Oliveira', 'ana@example.com', 'Calça Jeans, Óculos de Sol'),
    ('Lucas Ferreira', 'lucas@example.com', 'Jaqueta, Sapato Social'),
    ('Carla Lima', 'carla@example.com', 'Camiseta, Boné'),
    ('Rodrigo Almeida', 'rodrigo@example.com', 'Relógio, Mochila'),
    ('Patrícia Costa', 'patricia@example.com', 'Óculos de Sol, Bolsa'),
    ('Amanda Pereira', 'amanda@example.com', 'Jaqueta, Tênis'),
    ('Gustavo Oliveira', 'gustavo@example.com', 'Calça Jeans, Sapato Social');

INSERT INTO pedidos (data_pedido, id_cliente, status_pedido)
VALUES
    ('2024-01-01', 1, 'Em andamento'), ('2024-01-02', 2, 'Entregue'), ('2024-01-03', 3, 'Em andamento'), ('2024-01-04', 4, 'Entregue'),
    ('2024-01-05', 5, 'Em andamento'), ('2024-01-06', 6, 'Entregue'), ('2024-01-07', 7, 'Em andamento'), ('2024-01-08', 8, 'Entregue'),
    ('2024-01-09', 9, 'Em andamento'), ('2024-01-10', 10, 'Entregue');

INSERT INTO item_pedidos (id_pedido, id_produto, quantidade)
VALUES
    (1, 1, 2), (1, 2, 1), (2, 3, 3), (2, 4, 2), (3, 1, 1), (3, 3, 4), (4, 2, 3), (4, 5, 1), (5, 4, 2), (5, 6, 2);

    
SELECT * FROM produtos;
SELECT * FROM clientes;
SELECT * FROM pedidos;
SELECT * FROM item_pedidos;
select nome, preco from produtos
where preco > 50;

SELECT clientes.nome, pedidos.data_pedido
FROM clientes
INNER JOIN pedidos ON clientes.id_clientes = pedidos.id_cliente
WHERE pedidos.data_pedido = '2024-01-01';

SELECT
    pedidos.id_pedidos,
    SUM(produtos.preco * item_pedidos.quantidade) AS valor_total
FROM
    pedidos
INNER JOIN
    item_pedidos ON pedidos.id_pedidos = item_pedidos.id_pedido
INNER JOIN
    produtos ON item_pedidos.id_produto = produtos.id_produto
GROUP BY
    pedidos.id_pedidos;

    
    
    
    
    






















