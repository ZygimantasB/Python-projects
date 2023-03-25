SELECT * FROM nba_stats;
#
# Duomenys: [https://www.basketball-reference.com/leagues/NBA_2022_totals.html](https://www.basketball-reference.com/leagues/NBA_2022_totals.html)
#
# Užduotys:
#
# 1. Parsisiųskite duomenis iš [https://www.basketball-reference.com/leagues/NBA_2022_totals.html](https://www.basketball-reference.com/leagues/NBA_2022_totals.html)
#
# 2. Į duomenų bazę sukurkite naują lentele nba_players ir įkelkite duomenis (Pagalba: [https://www.dropbase.io/post/ways-to-convert-excel-files-to-databases-quickly](https://www.dropbase.io/post/ways-to-convert-excel-files-to-databases-quickly) ir iš jos  [https://sqlizer.io/#/)/](https://sqlizer.io/#/)/) (SQL Lite duomenų bazė turi apribojimą, todėl eilutėse su VARCHAR ištrinkite limitus).
#
# 3. Parašyti užklausas:
# 4. Pažiūrėti visus lentelės duomenis;

SELECT * FROM nba_stats;

# 5. Išrinkti stulpelius Player, Tm ir PTS;

SELECT Player, Tm, PTS FROM nba_stats;

# 6. Išrinkti stulpelius Players, Tm ir sukurtį naują stulpelį Points_per_game
# (PTS- viso taškų), kuriame suskaičiuoti kiek žaidėjas įmetė per varžybas.
# Išrušiuoti nuo daugiausiai įmetusio iki mažiausiai;

SELECT Player, Pos, PTS, G , ROUND(AVG(PTS / G), 2) AS AVG_PTS FROM nba_stats
GROUP BY Player, Pos, PTS, G
ORDER BY AVG_PTS DESC;

# 7. Sugrupuoti žaidėjus pagal pozicijas (Pos stulpelis – pozicijas, PTS - taškai),
# paimti laukelius Player, Pos, Tm, PTS;

SELECT Player, Pos, Tm, PTS FROM nba_stats
ORDER BY Pos, PTS DESC;

# 8. Išrinkti visus žaidėjuss, kurių vardas baigiasi ‚as‘;

SELECT Player FROM nba_stats WHERE player LIKE 'as %';

# 9. Išrinkti visus gynėjus, kurie žaidė bent 30 varžybų ir
# perdavimų vidurkis buvo didesnis nei 3;

SELECT Player, AST, G, AVG(AST / G) AS AVG_AST FROM nba_stats
WHERE Pos LIKE '_G' AND G > 30
GROUP BY Player, AST, G
HAVING AVG_AST > 3
ORDER BY AVG(AST / G) DESC;

# 10. Išrinkti visus žaidėjus, kurių atkovotų kamuolių
# vidurkis didesnis nei bendras žaidėjų vidurkius;

SELECT * FROM nba_stats;

SELECT Player, TRB, AVG(TRB / G) AS AVG_TRB FROM nba_stats
GROUP BY Player, TRB
HAVING AVG_TRB >= (SELECT AVG(TRB / G) FROM nba_stats)
ORDER BY AVG(TRB / G) DESC;

# 11. Apskaičiuoti įmestų taškų vidurkį pagal pozicijas.

SELECT Player, PTS,  G, Pos,  AVG(PTS / G) AS AVG_PTS FROM nba_stats
GROUP BY Player, PTS,  G, Pos
ORDER BY Pos, AVG_PTS DESC;

