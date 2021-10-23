CREATE TABLE aluno(
	id SERIAL,
	idade INTEGER,
	mensalidade NUMERIC(10,2),
	nota real,
	nome VARCHAR(255),
	cpf CHAR(11),
	observacao TEXT,
	matricula_trancada BOOLEAN,
	data_nascimento DATE,
	horario_primeira_aula TIME,
	data_matricula timestamp
);

INSERT INTO aluno (
	idade,
	mensalidade,
	nota,
	nome,
	cpf,
	observacao,
	matricula_trancada,
	data_nascimento,
	horario_primeira_aula,
	data_matricula
) VALUES(
	21,
	99.99,
	9.02,
	'Douglas',
	01234567890,
	'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec congue molestie tellus nec maximus. Donec mollis erat quis pulvinar auctor. Etiam consectetur mi non quam commodo dapibus. Phasellus id aliquam dolor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum ut est eleifend purus placerat mattis non eget enim. Proin pellentesque, ipsum vitae luctus placerat, arcu elit ullamcorper mauris, eget hendrerit urna nunc iaculis tellus. In facilisis nunc ac nisi faucibus fermentum. Donec quis tempor ligula, vel pellentesque ligula. Donec vehicula faucibus lectus, in suscipit sem interdum in. Morbi sit amet ultricies mauris, sit amet molestie erat. Quisque diam metus, pulvinar eget viverra sed, malesuada molestie sapien. Cras et accumsan sapien, a efficitur justo. Maecenas vitae velit ut ipsum porta tempus. Vivamus posuere id arcu eget suscipit. Phasellus at quam odio. Proin maximus, dolor ut feugiat fermentum, magna enim hendrerit mi, sit amet accumsan nisi enim non mauris. Fusce posuere rhoncus sapien, vel egestas lectus suscipit non. Sed eu est in tellus dapibus congue. Cras ut augue quis ex mollis malesuada sit amet a libero. Donec eleifend convallis auctor. Morbi dictum ultricies aliquet. Phasellus tristique mi justo, a eleifend tortor rhoncus id. Maecenas et hendrerit leo. Maecenas auctor tempus vulputate. Quisque mollis luctus sem, quis interdum lorem ultrices et. Sed ut leo vel leo lobortis rhoncus a ut erat. Nulla facilisi. Nullam aliquam hendrerit nibh, in tincidunt ligula malesuada in. Donec tincidunt fermentum metus quis consectetur. Nullam semper nibh vitae vestibulum viverra. Proin sed nisl a velit pulvinar dictum. Nunc finibus nulla in ipsum lobortis mattis. Duis auctor odio ac placerat egestas. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nunc leo nunc, porttitor nec porttitor in, viverra sit amet neque. Mauris eu lorem quis elit hendrerit aliquam at vitae erat. Proin ut magna leo. Nunc pulvinar ornare felis a ullamcorper. Vivamus scelerisque venenatis felis, sed ullamcorper nulla molestie eu. Nunc finibus orci at pharetra tincidunt. Maecenas tempus urna diam, quis aliquam purus rutrum ornare. Aliquam molestie fringilla leo. Nunc aliquam lacinia ante, sed vulputate mi consequat eget. Mauris hendrerit eget erat ac tempor. Nunc laoreet, nisl pellentesque sollicitudin pulvinar, ante mi tristique nisl, non facilisis sapien tellus id turpis. Praesent pellentesque ultricies odio, sit amet ultrices orci vehicula id. Pellentesque dolor turpis, ornare maximus imperdiet id, laoreet vitae felis. Cras tempor lectus eget purus malesuada, eu dictum leo ultricies.',
	FALSE,
	'2000-09-13',
	'18:30:00',
	'2018-12-20 10:00:00'
);

SELECT * FROM aluno;

SELECT * FROM aluno
	WHERE matricula_trancada = FALSE;

UPDATE aluno
	SET
		data_matricula = '2021-01-25',
		mensalidade = 115.90
	WHERE
		matricula_trancada = FALSE;

SELECT * FROM aluno
	WHERE idade >= 18;

DELETE FROM aluno
	WHERE idade >= 18;