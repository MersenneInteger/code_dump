using System;
using System.Collections.Generic;

namespace LMS
{
    internal class Student
    {
        private string Username;
        private string Password;
        private uint NumOfBooksCheckedOut = 0;
        private uint NumOfBooksOverdue = 0;
        private List<Book> BooksCheckedOut = new List<Book>();
        private List<Book> OverdueBooks = new List<Book>();

        public Student(){}

        public Student(string Username, string Password)
        {
            this.Username = Username;
            this.Password = Password;
        }

        /// <summary>
        /// Return Student Username
        /// </summary>
        /// <returns>String</returns>
        public string GetUsername()
        {
            return Username;
        }

        /// <summary>
        /// Compare user-entered password with password associated with student username
        /// </summary>
        /// <param name="password">String</param>
        /// <returns>Bool</returns>
        /// 
        public bool ComparePasswords(string password)
        {
            if (Password.Equals(password))
                return true;
            return false;
        }

        /// <summary>
        /// Return number of books checked out under Student account
        /// </summary>
        /// <returns>uint</returns>
        public uint GetNumOfBooksCheckedOut()
        {
            return NumOfBooksCheckedOut;
        }

        /// <summary>
        /// Return number of books checked out under Student accoutn that are overdue
        /// </summary>
        /// <returns>uint</returns>
        public uint GetNumOfBooksOverdue()
        {
            return NumOfBooksOverdue;
        }

        /// <summary>
        /// Return list of Book objects checked out under Student that are overdue
        /// </summary>
        /// <returns>List<Book></returns>
        public List<Book> GetOverdueBooks()
        {
            return OverdueBooks;
        }

        /// <summary>
        /// Checkout book under student account
        /// </summary>
        /// <param name="book">Book</param>
        public void CheckOutBook(Book book)
        {
            NumOfBooksCheckedOut++;
            BooksCheckedOut.Add(book);
            book.CheckOutBook();
        }

        /// <summary>
        /// Return book checked out under Student account
        /// </summary>
        /// <param name="book">Book</param>
        public void ReturnBook(Book book)
        {
            if (NumOfBooksCheckedOut >= 0)
            {
                NumOfBooksCheckedOut--;
                BooksCheckedOut.Remove(book);
                book.ReturnBook();

                if(OverdueBooks.Contains(book))
                {
                    OverdueBooks.Remove(book);
                    NumOfBooksOverdue--;
                }
            }
            else
                Console.WriteLine("No books currently checked out");
        }

        /// <summary>
        /// Print list of books currently checked out under student account
        /// </summary>
        public void ViewBooksCheckedOut()
        {
            Console.WriteLine();
            if (NumOfBooksCheckedOut > 0)
            {
                foreach (Book book in BooksCheckedOut)
                {
                    Console.WriteLine($"{book.GetInfo()}\n");
                }
            }
            else
                Console.WriteLine("No books currently checked out");
        }

        /// <summary>
        /// Search for overdue books checked out under Student account, print book info if they exist
        /// </summary>
        public void CheckIfStudentHasBooksOverdue()
        {
            string overdueBooksInfo = "";

            foreach(var book in BooksCheckedOut)
            {
                if(book.CheckIfBookIsOverdue())
                {
                    NumOfBooksOverdue++;
                    overdueBooksInfo += book.GetInfo();
                    OverdueBooks.Add(book);
                }
            }
            if (NumOfBooksOverdue > 0)
                Console.WriteLine(overdueBooksInfo);
            else
                Console.WriteLine("No books overdue");
        }

        /// <summary>
        /// Return Book object given title of book
        /// </summary>
        /// <param name="title">string</param>
        /// <returns>Book</returns>
        public Book GetBookByTitle(string title)
        {
            foreach(Book book in BooksCheckedOut)
            {
                if (book.GetTitle().ToLower().Equals(title.ToLower()))
                {
                    return book;
                }
            }
            return null;
        }
    }
}
