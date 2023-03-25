-- 1. Išrinkite visus duomenis iš lentelės “DARBUOTOJAI”.

select * from DARBUOTOJAS;

-- 2. Išrinkite visus duomenis iš stulpelio “GIMIMO_DATA” - lentelėje “DARBUOTOJAS”.

SELECT ASMENS_KODAS FROM DARBUOTOJAS;

-- 3. Išrinkite visus duomenis iš stulpelių “VARDAS”,”PAVARDĖ”, “PAREIGOS” - lentelėje “DARBUOTOJAI”.

SELECT VARDAS, PAVARDĖ, PAREIGOS FROM DARBUOTOJAS;

-- 4. Išrinkite skirtingas reikšmes iš stulpelio SKYRIUS_PAVADINIMAS - lentelėje “DARBUOTOJAI”

SELECT DISTINCT (SKYRIUS_ID) FROM DARBUOTOJAS;

-- 5. Išrinkite visus duomenis apie darbuotojus, kurie dirba Gamybos skyriuje.

SELECT *
FROM DARBUOTOJAS
JOIN SKYRIUS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
WHERE SKYRIUS.PAVADINIMAS='Gamybos';

-- 6. Išrinkite duomenis, kokias pareigas užima Giedrius

SELECT * FROM SKYRIUS
JOIN DARBUOTOJAS ON DARBUOTOJAS.SKYRIUS_ID = SKYRIUS.ID
WHERE DARBUOTOJAS.VARDAS = 'Giedrius';

-- 7. Išrinkite visus duomenis apie darbuotojus, kurių gimimo data - 1986-09-19

SELECT * FROM DARBUOTOJAS WHERE ASMENS_KODAS LIKE '%860919%';

-- 8. Išrinkite darbuotojų vardus, kurių pavardės yra Sabutis

SELECT * FROM DARBUOTOJAS WHERE PAVARDĖ='Sabutis';

-- 9. Išrinkite duomenis (vardą ir pavardę) apie programuotojus iš Gamybos skyriaus

SELECT * FROM DARBUOTOJAS
JOIN SKYRIUS ON SKYRIUS.ID = DARBUOTOJAS.SKYRIUS_ID
WHERE SKYRIUS.PAVADINIMAS = 'Gamybos' AND DARBUOTOJAS.PAREIGOS = 'Programuotojas';

-- 10. Įterpkite į lentelę “DARBUOTOJAI” naują darbuotoją, užpildydami
-- visus reikiamus laukus (vardą, pavardę, gimimo metus, pareigas, skyriaus pavadinimą).

INSERT INTO DARBUOTOJAS(VARDAS, PAVARDĖ, ASMENS_KODAS, PAREIGOS, DIRBA_NUO)
VALUES('Jonas', 'Jonaitis', 38510101212, 'Programuotojas', '2023-02-01');

SELECT * FROM DARBUOTOJAS;

-- 11. Įterpkite į lentelę “DARBUOTOJAI” naują darbuotoją,
-- užpildydami tik laukus (vardą, pavardę, gimimo metus).
-- Pareigas ir skyriaus pavadinimą palikite neužpildytus.

INSERT INTO DARBUOTOJAS (VARDAS, PAVARDĖ, ASMENS_KODAS)
VALUES ('Petras', 'Petraitis', 38907180000);

SELECT * FROM DARBUOTOJAS;

-- 12. Užpildykite likusius tuščius laukus “DARBUOTOJAI” lentelėje,
-- jūsų prieš tai įterptame įraše. Priskirkite darbuotojui pareigas
-- ir skyrių.

UPDATE DARBUOTOJAS SET PAREIGOS='Vadovas', DIRBA_NUO='2021-01-31'
WHERE VARDAS='Petras' AND PAVARDĖ='Petraitis';

SELECT * FROM DARBUOTOJAS;

-- 13. Ištrinkite lentelės “DARBUOTOJAI” įrašą, kurio gimimo data yra tokia, kurią jūs sukūrėte

SELECT * FROM DARBUOTOJAS WHERE ASMENS_KODAS=38907180000 OR ASMENS_KODAS=38510101212;

DELETE FROM DARBUOTOJAS WHERE ASMENS_KODAS=38907180000 OR ASMENS_KODAS=38510101212;

-- 14. Įterpkite, du darbuotojus, pavarde Antanaitis kurių pareigos būtų “Programuotojas”.

INSERT INTO DARBUOTOJAS(PAVARDĖ, PAREIGOS)
VALUES('Antanaitis', 'Programuotojas'),
('Antanaitis', 'Programuotojas');

SELECT * FROM DARBUOTOJAS;

-- 15. Pakeiskite, abiejų Antanaičių pareigas į “Testuotojas” vienu sakiniu

UPDATE DARBUOTOJAS SET PAREIGOS='Testuotojas'
WHERE PAVARDĖ='Antanaitis' AND PAREIGOS='Programuotojas';

SELECT * FROM DARBUOTOJAS;

-- 16. Suskaičiuokite, kiek įmonėje dirba Testuotojų.

SELECT PAREIGOS, COUNT(PAREIGOS)
FROM DARBUOTOJAS
WHERE PAREIGOS='Testuotojas'
GROUP BY PAREIGOS;
