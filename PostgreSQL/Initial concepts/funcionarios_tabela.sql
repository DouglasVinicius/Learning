DROP TABLE Funcionarios;

CREATE TABLE Funcionarios (
	id SERIAL PRIMARY KEY,
	matricula VARCHAR(10),
	nome VARCHAR(255),
	sobrenome VARCHAR(255)
);
		
INSERT
	INTO Funcionarios (
		matricula,
		nome,
		sobrenome
	)
	VALUES (
		'190150',
		'Douglas',
		'Dullius'
	);
	
INSERT
	INTO Funcionarios (
		matricula,
		nome,
		sobrenome
	)
	VALUES (
		'180135',
		'Gustavo',
		'Tameiosso'
	);
	
INSERT
	INTO Funcionarios (
		matricula,
		nome,
		sobrenome
	)
	VALUES (
		'102365',
		'Vinicius',
		'Souza'
	);
	
INSERT
	INTO Funcionarios (
		matricula,
		nome,
		sobrenome
	)
	VALUES (
		'945752',
		'Rafael',
		'Jarczewski'
	);
	
INSERT
	INTO Funcionarios (
		matricula,
		nome,
		sobrenome
	)
	VALUES (
		'123645',
		'Douglas',
		'Ledur'
	);
	
/*Testando ordenação de valores (ORDER BY)*/
SELECT * 
	FROM Funcionarios
	ORDER BY 3, 4, 2;   -- Ordenando por Nome, seguido como critério de desempate sobrenome e matricula respectivamente (utilizando index das colunas)
	
SELECT * 
	FROM Funcionarios
	ORDER BY nome, sobrenome, matricula;   -- Ordenando de forma semelhante a anterior, porém utilizando os nomes das colunas
	
SELECT * 
	FROM Funcionarios
	ORDER BY nome ASC, sobrenome DESC, matricula ASC;   -- Ordenando de forma semelhante a anterior, porém de maneira decrescente nos sobrenomes, ASC = crescente, porém é a ordenação padrão

/*Limitadores e offsets*/
SELECT *
	FROM Funcionarios
	ORDER BY id ASC
	LIMIT 3          -- Limit limita a quantidade de linhas que queremos buscar
	OFFSET 2;        -- Offset significa a quantidade de linhas que gostariamos de pular, neste caso ao invés de id's(1,2,3) temos id's(3,4,5)
	
/*Funções de agregação*/
SELECT
	COUNT(id) AS "Quantidade de ids",
	SUM(id) AS "Soma dos valores de ids",
	MAX(id) AS "Id máximo",
	MIN(id) AS "Id mínimo",
	ROUND(AVG(id), 3) AS "Id médio arredondado para três casas decimais"
	
	FROM Funcionarios;
	
/*Função que elimina repetições de campos*/
SELECT
	DISTINCT 
		nome
	FROM Funcionarios;
	
/*Agrupamentos de dados*/
SELECT
	nome, COUNT(id)
	
	FROM Funcionarios
	GROUP BY nome         -- Agrupando os nomes iguais e efetuando uma contagem deles
	ORDER BY 1;
	
SELECT
	nome, sobrenome, COUNT(id)
	
	FROM Funcionarios
	GROUP BY 2 ,1        -- Fazendo algo similar a situação acima, porém agrupando por ambos nome e sobrenome, e acessando eles como index 1 e 2
	ORDER BY nome ASC, sobrenome ASC;
	
SELECT
	nome, COUNT(id)
	
	FROM Funcionarios
	GROUP BY nome
	HAVING COUNT(id) > 1      --Vai coletar os funcionários que possuem nomes duplicados	
	ORDER BY nome;
	/*HAVING é similar a WHERE, porém ela é utilizada para agrupamentos, enquanto WHERE para itens isolados*/
	
SELECT
	nome, sobrenome, COUNT(id)
	
	FROM Funcionarios
	GROUP BY nome, sobrenome
	HAVING COUNT(id) = 1      --Vai coletar os funcionários que não possuem nomes e sobrenomes duplicados	
	ORDER BY nome, sobrenome;