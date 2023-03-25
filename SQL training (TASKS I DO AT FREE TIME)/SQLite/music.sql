SELECT * FROM albums;
SELECT * FROM artists;
SELECT * FROM songs;
SELECT * FROM sqlite_master;

SELECT * FROM songs
WHERE _id=367;

SELECT * FROM albums ORDER BY name;
SELECT * FROM albums ORDER BY name COLLATE NOCASE;
SELECT * FROM albums ORDER BY name COLLATE NOCASE DESC;
SELECT * FROM albums ORDER BY artist, name COLLATE NOCASE;

SELECT * FROM songs ORDER BY album, track;
SELECT * FROM albums WHERE _id=439;
SELECT * FROM artists WHERE _ID=133;

SELECT * FROM artists
ORDER BY name ASC;

SELECT * FROM songs
WHERE songs.title LIKE '%Forbidden%';

SELECT * FROM songs
WHERE title LIKE '%Deep Purple%';

SELECT COUNT(*) FROM songs;


SELECT songs.title FROM songs INNER JOIN albums ON songs.album = albums._id WHERE albums.name = "Forbidden";

SELECT songs.track, songs.title FROM songs INNER JOIN albums ON songs.album = albums._id WHERE albums.name = "Forbidden" ORDER BY songs.track;

SELECT songs.title FROM songs
    INNER JOIN albums ON songs.album = albums._id
    INNER JOIN artists ON albums.artist = artists._id WHERE artists.name = "Deep Purple";

UPDATE artists SET name = "One Kitten" WHERE artists.name = "Mehitable";

SELECT * FROM artists WHERE artists.name = "One Kitten";


