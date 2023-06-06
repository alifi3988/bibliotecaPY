BEGIN TRANSACTION;
CREATE TABLE tb_leitores (
        id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome        TEXT NOT NULL,
        idade       INTEGER,
        cpf         VARCHAR(11) NOT NULL,
        email       TEXT NOT NULL,
        fone        TEXT,
        cidade      TEXT,
        uf          VARCHAR(2) NOT NULL,
        criado_em   DATE NOT NULL
    );
INSERT INTO "tb_leitores" VALUES(3,'Carlos Eduardo',25,'123.456.789-00','carlos@teste.com.br','16 98888-7777','Cravinhos','sp','2023-05-22');
INSERT INTO "tb_leitores" VALUES(4,'Leitor Leitor',23,'47013722857','alifi3988@gmail.com','19989763871','Riebirão Preto','SP','2023-05-23');
INSERT INTO "tb_leitores" VALUES(5,'Paty',28,'123.456.789-00','paty@fatec.com','11998776543','Araraquara','SP','2023-06-05');
CREATE TABLE tb_livros (
        id                  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo              VARCHAR(255) NOT NULL,
        autor               VARCHAR(255) NOT NULL,
        editora             VARCHAR(255) NOT NULL,
        anoLancamento       INTEGER NOT NULL,
        registrado          DATA NOT NULL,
        statusAssociativo   BOOL NOT NULL
    );
INSERT INTO "tb_livros" VALUES(7,'A arte da guerra','Sun Tzu','Obra complet',2019,'2023-05-19','True');
INSERT INTO "tb_livros" VALUES(10,'Java','Fabricio','Fatec',2020,'2023-05-22','True');
INSERT INTO "tb_livros" VALUES(13,'1984','George Orwell',' Penguin Books',1949,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(14,'Dom Quixote','Miguel de Cervantes','Livraria Estante',1605,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(15,'Orgulho e Preconceito','Jane Austen','Penguin Classics',1813,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(16,'Cem Anos de Solidão','Gabriel García Márquez','Harper & Row',1967,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(17,'Crime e Castigo','Fiódor Dostoiévski','Editora 34',1866,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(18,'O Apanhador no Campo de Centeio','J.D. Salinger','Little, Brown and Company',1951,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(19,'O Senhor dos Anéis','J.R.R. Tolkien','George Allen & Unwin',1954,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(20,'Ulisses','James Joyce','Sylvia Beach',1922,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(21,'Guerra e Paz','Liev Tolstói','The Russian Messenger',1869,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(22,'Harry Potter e a Pedra Filosofal','J.K. Rowling','Bloomsbury Publishing',2000,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(23,'Crepúsculo','Stephenie Meyer','Little, Brown and Company',2005,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(24,'A Culpa é das Estrelas','John Green',' Dutton Books',2012,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(25,'A Menina que Roubava Livros','Markus Zusak','Picador',2005,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(26,'A Sutil Arte de Ligar o F*da-se','Mark Manson','Intrínseca',2016,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(27,'Millennium: Os Homens que Não Amavam as Mulheres','Stieg Larsson','Norstedts Förlag',2005,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(28,'O Caçador de Pipas','Khaled Hosseini',' Riverhead Books',2003,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(29,'O Código Da Vinci',' Dan Brown','Doubleday',2003,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(30,'A Menina do Vale','Bel Pesce',' Editora Senai',2012,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(31,'A Rainha do Castelo de Ar',' Stieg Larsson',' Norstedts Förlag',2006,'2023-06-01','True');
INSERT INTO "tb_livros" VALUES(32,'Java','Fabrício','Fatec',2020,'2023-06-05','True');
CREATE TABLE tb_retirada(
        idLeitor            INTEGER NOT NULL,
        idLivro             INTEGER NOT NULL,
        dataRetirada        DATE NOT NULL,
        dataDevolucao       DATE NOT NULL,
        statusAssociativo   BOOL NOT NULL,
        CONSTRAINT pk_tbRetirada_double_key  PRIMARY KEY (idLeitor, idLivro),
        CONSTRAINT fk_tbRetirada_leitor FOREIGN KEY(idLeitor) REFERENCES tb_leitores(id),
        CONSTRAINT fk_tbRetirada_livro FOREIGN KEY(idLivro) REFERENCES tb_livros(id)
        );
INSERT INTO "tb_retirada" VALUES(3,32,'2023-06-05','2023-06-20','False');
CREATE TABLE tb_usuarios (
        id                  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome                TEXT NOT NULL,
        login               VARCHAR(20) NOT NULL UNIQUE,
        senha               VARCHAR(25) NOT NULL,
        dataCriacao         DATE NOT NULL,
        statusAssociativo   BOOL NOT NULL
    );
INSERT INTO "tb_usuarios" VALUES(9,'admin','admin','admin','2023-05-19','True');
INSERT INTO "tb_usuarios" VALUES(10,'ADMINISTRADOR','admin@','adminadmin','2023-05-25','True');
INSERT INTO "tb_usuarios" VALUES(11,'Rafael','rafa87','123456','2023-05-29','True');
INSERT INTO "tb_usuarios" VALUES(14,'Alifi Augusto Estevam dos Santos','alifi.santos','12345678','2023-05-31','True');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('tb_usuarios',14);
INSERT INTO "sqlite_sequence" VALUES('tb_livros',32);
INSERT INTO "sqlite_sequence" VALUES('tb_leitores',5);
COMMIT;
