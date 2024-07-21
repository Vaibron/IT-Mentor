CREATE TABLE  pupil(
	pupil_id SERIAL PRIMARY KEY,
	lastname VARCHAR(100),
	firstname VARCHAR(100),
	middlename VARCHAR(100)
);

CREATE TABLE  sections(
	sections_id SERIAL PRIMARY KEY,
	sectionsname VARCHAR(255),
	description TEXT
);

CREATE TABLE pupil_sections(
	pupil_id INT,
	sections_id INT,
	FOREIGN KEY (pupil_id) REFERENCES pupil(pupil_id),
	FOREIGN KEY (sections_id) REFERENCES sections(sections_id),
	PRIMARY KEY (pupil_id, sections_id)
);
