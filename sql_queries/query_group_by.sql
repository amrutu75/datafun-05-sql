-- group by what decade the book was published in
 SELECT 
   (year_published / 10) * 10 AS decade,
   COUNT(*) AS num_books,
   AVG(year_published - birth_year) AS avg_author_age
 FROM authors a
 JOIN books b ON a.author_id = b.author_id
 GROUP BY decade
 ORDER BY decade;


