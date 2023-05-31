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
INSERT INTO "tb_leitores" VALUES(1,'Teste',23,'47013722856','alifi3988@gmail.com','19989763871','Ribeirão Preto','SP','<bound method Leitor.getData of <objetosProjeto.entitys.leitor.Leitor object at 0x000001EED40B5360>>');
INSERT INTO "tb_leitores" VALUES(2,'Alifi ',23,'47013722855','alifi3988@gmail.com','19989763871','Ribeirão Preto','SP','<bound method Leitor.getData of <objetosProjeto.entitys.leitor.Leitor object at 0x000001E606145360>>');
INSERT INTO "tb_leitores" VALUES(3,'Carlos Eduardo',25,'123.456.789-00','carlos@teste.com.br','16 98888-7777','Cravinhos','sp','2023-05-22');
INSERT INTO "tb_leitores" VALUES(4,'Leitor Leitor',23,'47013722857','alifi3988@gmail.com','19989763871','Riebirão Preto','SP','2023-05-23');
CREATE TABLE tb_livros (
        id                  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo              VARCHAR(255) NOT NULL,
        autor               VARCHAR(255) NOT NULL,
        editora             VARCHAR(255) NOT NULL,
        anoLancamento       INTEGER NOT NULL,
        registrado          DATA NOT NULL,
        statusAssociativo   BOOL NOT NULL
    );
INSERT INTO "tb_livros" VALUES(1,'t','t','t',2000,'2023-05-18','True');
INSERT INTO "tb_livros" VALUES(2,'teste','teste','teste',2001,'2023-05-18','True');
INSERT INTO "tb_livros" VALUES(3,'A volta dos que não foram','Desconhecido','Desconhecido',1999,'2023-05-18','False');
INSERT INTO "tb_livros" VALUES(4,'A Culpa é das Estrelas','Desconhecido ','nenhuma',2019,'2023-05-18','True');
INSERT INTO "tb_livros" VALUES(5,'teste','teste','teste',2000,'2023-05-18','True');
INSERT INTO "tb_livros" VALUES(6,'Java','Geraldo','Fatec',2020,'2023-05-18','True');
INSERT INTO "tb_livros" VALUES(7,'A arte da guerra','Sun Tzu','Obra complet',2019,'2023-05-19','False');
INSERT INTO "tb_livros" VALUES(8,'Teste do livro Novo','Autor Novo','Editora Nova',2023,'2023-05-19','True');
INSERT INTO "tb_livros" VALUES(9,'Teste ano','Autor teste','teste',2023,'2023-05-19','True');
INSERT INTO "tb_livros" VALUES(10,'Java','Fabricio','Fatec',2020,'2023-05-22','False');
INSERT INTO "tb_livros" VALUES(11,'A volta dos que não foram parte II','Desconhecido','Desconhecido',2015,'2023-05-23','False');
CREATE TABLE tb_livrosWEB (
        id                  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo              VARCHAR(255) NOT NULL UNIQUE,
        autor               VARCHAR(255) NOT NULL UNIQUE,
        statusAssociativo   BOOL NOT NULL
    );
INSERT INTO "tb_livrosWEB" VALUES(1,'O Despertar de Tudo','David Graeber e David Wengrow','True');
INSERT INTO "tb_livrosWEB" VALUES(2,'Quando deixamos de entender o mundo','Benjamín Labatut','True');
INSERT INTO "tb_livrosWEB" VALUES(3,'O som do rugido da onça','Micheliny Verunschk','True');
INSERT INTO "tb_livrosWEB" VALUES(4,'A filha perdida','Elena Ferrante','True');
INSERT INTO "tb_livrosWEB" VALUES(5,'Solitária','Eliana Alves Cruz','True');
INSERT INTO "tb_livrosWEB" VALUES(6,'Memória de Ninguém','Helena Machado','True');
INSERT INTO "tb_livrosWEB" VALUES(7,'Torto arado','Itamar Vieira Junior','True');
INSERT INTO "tb_livrosWEB" VALUES(8,'Tempos ásperos','Mario Vargas Llosa','True');
INSERT INTO "tb_livrosWEB" VALUES(9,'Tudo sobre o amor','bell hooks','True');
INSERT INTO "tb_livrosWEB" VALUES(10,'A cachorra','Pilar Quintana','True');
INSERT INTO "tb_livrosWEB" VALUES(11,'Para Viver Em Paz o Milagre da Mente Alerta','Thich Nhat Hanh','True');
INSERT INTO "tb_livrosWEB" VALUES(12,'Os da minha rua','Ondjaki','True');
INSERT INTO "tb_livrosWEB" VALUES(13,'O dilema do porco-espinho','Leandro Karnal','True');
INSERT INTO "tb_livrosWEB" VALUES(14,'Felicidade Clandestina','Clarice Lispector','True');
INSERT INTO "tb_livrosWEB" VALUES(15,'Terra Sonâmbula','Mia Couto','True');
INSERT INTO "tb_livrosWEB" VALUES(16,'Toda poesia','Paulo Leminski','True');
INSERT INTO "tb_livrosWEB" VALUES(17,'A chave de casa','Tatiana Salem Levy','True');
INSERT INTO "tb_livrosWEB" VALUES(18,'Caim','José Saramago','True');
INSERT INTO "tb_livrosWEB" VALUES(19,'Elizabeth Costello','J. M. Coetzee','True');
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
INSERT INTO "tb_retirada" VALUES(2,7,'2023-05-22','2023-06-06','True');
INSERT INTO "tb_retirada" VALUES(2,3,'2023-05-22','2023-06-06','True');
INSERT INTO "tb_retirada" VALUES(3,10,'2023-05-22','2023-05-24','True');
INSERT INTO "tb_retirada" VALUES(4,11,'2023-05-23','2023-06-07','True');
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
INSERT INTO "tb_usuarios" VALUES(12,'admon@','','0','2023-05-29','False');
INSERT INTO "tb_usuarios" VALUES(13,'Alifi Augusto','t_asantos','123456','2023-05-29','True');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('tb_usuarios',13);
INSERT INTO "sqlite_sequence" VALUES('tb_livros',11);
INSERT INTO "sqlite_sequence" VALUES('tb_leitores',4);
INSERT INTO "sqlite_sequence" VALUES('tb_livrosWEB',19);
COMMIT;
