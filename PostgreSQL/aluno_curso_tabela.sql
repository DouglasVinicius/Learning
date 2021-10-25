/*Utilizando chave primária, campo único e não nulo*/
CREATE TABLE Aluno (
	id SERIAL PRIMARY KEY,        /*Primary key = Único e não nulo, identificador*/
	nome VARCHAR(255) NOT NULL    /*Não pode ser nulo*/
);

/*Inserindo alguns valores para testes*/
INSERT 
	INTO Aluno(
		nome
	)
	VALUES(
		'Douglas'
	);
	
INSERT 
	INTO Aluno(
		nome
	)
	VALUES(
		'Gustavo'
	);
	
INSERT 
	INTO Aluno(
		nome
	)
	VALUES(
		'VASPP'
	);

/*Utilizando chave primária, campo único e não nulo*/
CREATE TABLE Curso (
	id INTEGER PRIMARY KEY,           /*Primary key = Único e não nulo, identificador*/
	nome VARCHAR(255) UNIQUE,         /*Único, não pode repetir*/
	professor VARCHAR(255) NOT NULL   /*Não pode ser nulo*/
);

/*Inserindo alguns valores para testes*/
INSERT 
	INTO Curso(
		professor,
		nome,
		id
	)
	VALUES(
		'Joao',
		'postgres',
		1
	);
	
INSERT 
	INTO Curso(
		professor,
		id
	)
	VALUES(
		'Jorge',
		2
	);
	
INSERT 
	INTO Curso(
		professor,
		nome,
		id
	)
	VALUES(
		'Jose',
		'Python',
		3
	);
	
INSERT 
	INTO Curso(
		professor,
		nome,
		id
	)
	VALUES(
		'Jair',
		'Java',
		4
	);
	
/*Criando uma tabela que faça a junção dos dois ids das tabelas acima*/
CREATE TABLE Aluno_curso (
	aluno_id INTEGER,
	curso_id INTEGER,
	
	PRIMARY KEY(aluno_id, curso_id), /*Criando uma chave primária composta, com os elementos aluno_id e curso_id*/
	
	FOREIGN KEY (aluno_id) REFERENCES Aluno (id)
	ON DELETE CASCADE   --Deleta em cascata quando for deletar um aluno da tabela Aluno, padrão é "ON DELETE RESTRICT", que não deixa isso acontecer  
	ON UPDATE CASCADE,  --Da mesma forma que o DELETE, porém para UPDATES agora
	FOREIGN KEY (curso_id) REFERENCES Curso (id)	 
	/*Criando duas chaves estrangeiras, linkando elas respectivamente com id da tabela Aluno e id da tabela Curso,
	fazendo com que para o elemento ser adicionado nessa nova tabela, ele deva estar contido na sua devida referencia*/
);

INSERT
	INTO Aluno_curso (
		aluno_id,
		curso_id
	)
	VALUES (
		1,
		2
	);
	
INSERT
	INTO Aluno_curso (
		aluno_id,
		curso_id
	)
	VALUES (
		1,
		1
	);
	
INSERT
	INTO Aluno_curso (
		aluno_id,
		curso_id
	)
	VALUES (
		2,
		3
	);

/*
INSERT
	INTO Aluno_curso (
		aluno_id,
		curso_id
	)
	VALUES (
		3,
		4
	);
					Aqui terá um erro, visto que não existe um curso de id 4 (por conta da referencia feita a id do curso)
*/

SELECT * FROM Aluno_curso;
SELECT * FROM Aluno;
ORDER BY 1,2;             --Ordenados primeiro pela primeira coluna e o critério de desempate é a segunda coluna

/* Buscando dados de duas tabelas utilizando o join*/
SELECT Aluno.nome AS "Nome do aluno", Curso.nome AS "Nome do curso"
	FROM
		Aluno JOIN Aluno_curso ON Aluno.id = Aluno_curso.aluno_id			-- Join == InnerJoin
		JOIN Curso ON Curso.id = Aluno_curso.curso_id;                      --Join irá buscar os dados onde o match em ambos os lados é válido
		
SELECT Aluno.nome AS "Nome do aluno", Curso.nome AS "Nome do curso"
	FROM
		Aluno LEFT JOIN Aluno_curso ON Aluno.id = Aluno_curso.aluno_id      --LeftJoin irá buscar os dados onde ambos dão match ou apenas o dado da esquerda
		LEFT JOIN Curso ON Curso.id = Aluno_curso.curso_id;
		
SELECT Aluno.nome AS "Nome do aluno", Curso.nome AS "Nome do curso"
	FROM
		Aluno RIGHT JOIN Aluno_curso ON Aluno.id = Aluno_curso.aluno_id      --RghtJoin irá buscar os dados onde ambos dão match ou apenas o dado da direita
		RIGHT JOIN Curso ON Curso.id = Aluno_curso.curso_id;
		
SELECT Aluno.nome AS "Nome do aluno", Curso.nome AS "Nome do curso"
	FROM
		Aluno FULL JOIN Aluno_curso ON Aluno.id = Aluno_curso.aluno_id
		FULL JOIN Curso ON Curso.id = Aluno_curso.curso_id;                      --FullJoin é uma junção dos três casos acima
		
SELECT Aluno.nome AS "Nome do aluno", Curso.nome AS "Nome do curso"
	FROM
		Aluno CROSS JOIN Curso;           --{a,b} CROSSJOIN {1,2} = {(a,1), (a,2), (b,1), (b,2)}
		
DELETE FROM Aluno WHERE id = 1; --Funciona porque estamos deletando em cascata na tabela Aluno_curso
UPDATE Aluno                    --Da mesma forma que em delete, aqui funciona porque fazemos o UPDATE na referência de Aluno_curso por cascata
	SET
		id = 1
	WHERE
		id = 4;
		
SELECT * FROM Aluno
ORDER BY Aluno.id;