--order by author name alphabetically
 SELECT a.name, b.title, b.year_published
 FROM authors a
 JOIN books b ON a.author_id = b.author_id
 ORDER BY a.name;