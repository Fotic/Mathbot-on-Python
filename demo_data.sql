-- Table with demo data

CREATE TABLE users(
	id INT AUTO_INCREMENT NOT NULL,
	user_name VARCHAR(255) NOT NULL,
	user_password VARCHAR(255) NOT NULL,
	f_name VARCHAR(255) NOT NULL,
	l_name VARCHAR(255) NOT NULL,
	prosthesi INT DEFAULT 0 NOT NULL,
	prosthesi_total INT DEFAULT 0 NOT NULL,
	afairesi INT DEFAULT 0 NOT NULL,
	afairesi_total INT DEFAULT 0 NOT NULL,
	pollaplasiasmo INT DEFAULT 0 NOT NULL,
	pollaplasiasmo_total INT DEFAULT 0 NOT NULL,
	diairesi INT DEFAULT 0 NOT NULL,
	diairesi_total INT DEFAULT 0 NOT NULL,
	PRIMARY KEY (id)
)

INSERT INTO users(user_name,user_password,f_name,l_name,prosthesi,prosthesi_total,afairesi,afairesi_total,pollaplasiasmo,pollaplasiasmo_total,diairesi,diairesi_total) VALUES
('fotis','1234--','Φώτης','Παπαρούνας',20,30,40,50,60,70,80,90),
('maria','--','Maria','Karra',11,22,33,44,55,66,77,88),
('kostas','--','Kostas','Spiropoulos',12,22,222,233,111,222,313,414),
('io','--','Ioanna','Ksara',233,311,222,501,62,744,855,911),
('Manolis','--','Manolis','Karanasios',66,77,11,44,123,321,77,94),
('xristakis','--','Xristos','Xristakidis',55,66,11,22,555,667,123,222),
('vas','--','Vasiliki','Mauriki',43,444,333,453,567,678,456,879),
('vlos','--','Pavlos','Tsiros',434,654,12,33,122,344,756,889),
('takis','--','Takis','Ioannou',233,331,323,474,876,987,123,322),
('marts','--','Maria','Tsampa',455,657,534,768,567,678,456,879),
('isis','--','Isivora','Kourtidou',453,545,452,657,123,422,212,533)