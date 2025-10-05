--find age when published and put into column age_when_published
--scatter plot of age vs year printed? 
-- distribution of ages when published?
WITH authors_books AS (
    SELECT a.author_id, a.name, a.birth_year, b.book_id, b.title, b.year_published
    FROM authors a
    JOIN books b ON a.author_id = b.author_id
)

SELECT year_published, year_published - birth_year as age_when_published 
FROM authors_books