-- 1. Create Tables
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Author VARCHAR(100),
    ISBN VARCHAR(20),
    AvailableCopies INT
);

CREATE TABLE Members (
    MemberID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(15)
);

CREATE TABLE Transactions (
    TXNID INT PRIMARY KEY,
    BookID INT,
    MemberID INT,
    IssueDate DATE,
    ReturnDate DATE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);
