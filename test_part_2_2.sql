SELECT u.name AS USER, b.name AS book, max(b.date) as date
FROM users u
INNER JOIN book b ON u.id = b.user_id
GROUP BY u.name
ORDER BY u.id