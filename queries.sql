-- 3. Queries

-- List all books issued to a specific member (example: MemberID = 1)
SELECT B.BookID, B.Author, B.ISBN
FROM Books B
JOIN Transactions T ON B.BookID = T.BookID
WHERE T.MemberID = 1;

-- List all books currently available for issue (i.e., AvailableCopies > 0)
SELECT * FROM Books
WHERE AvailableCopies > 0;
