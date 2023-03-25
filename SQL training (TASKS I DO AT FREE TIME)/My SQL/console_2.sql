USE ig_clone;

SELECT username, created_at
FROM users
ORDER BY created_at DESC
LIMIT 5;

SELECT DAYNAME(created_at), COUNT(*)
FROM users
GROUP BY DAYNAME(created_at);

SELECT username
FROM users
LEFT JOIN photos ON users.id = photos.user_id
WHERE photos.created_at IS NULL;

SELECT users.username, COUNT(likes.user_id)
FROM likes
JOIN photos ON likes.photo_id = photos.id
JOIN users ON photos.user_id  = users.id
GROUP BY likes.photo_id
ORDER BY COUNT(likes.photo_id) DESC
LIMIT 1;

SELECT ((SELECT COUNT(*) FROM photos) / (SELECT count(*) FROM users));

SELECT tag_name, COUNT(tag_name)
FROM tags
JOIN photo_tags ON photo_tags.tag_id = tags.id
GROUP BY tag_name
ORDER BY COUNT(tag_name) DESC
LIMIT 5;


SELECT username, Count(*) AS num_likes
FROM   users
INNER JOIN likes ON users.id = likes.user_id
GROUP  BY likes.user_id
HAVING num_likes = (SELECT Count(*) FROM photos);




