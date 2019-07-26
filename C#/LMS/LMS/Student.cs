using System;
using System.Collections.Generic;

namespace LMS
{
    internal class Student
    {
        private string Username;
        private string Password;
        private string Name;
        private uint Id;
        private uint NumOfBooksCheckedOut = 0;
        private uint NumOfBooksOverdue = 0;
        private List<Book> BooksCheckedOut = new List<Book>();
        private List<Book> OverdueBooks = new List<Book>();

        public Student(){}

        public Student(string Username, string Password, string Name, uint Id)
        {
            this.Username = Username;
            this.Password = Password;
            this.Name = Name;
            this.Id = Id;
        }

        public string GetName()
        {
            return Name;
        }

        public string GetUsername()
        {
            return Username;
        }

        public bool ComparePasswords(string password)
        {
            if (Password.Equals(password))
                return true;
            return false;
        }
        public uint GetNumOfBooksCheckedOut()
        {
            return NumOfBooksCheckedOut;
        }

        public uint GetNumOfBooksOverdue()
        {
            return NumOfBooksOverdue;
        }

        public List<Book> GetOverdueBooks()
        {
            return OverdueBooks;
        }

        public void CheckOutBook(Book book)
        {
            NumOfBooksCheckedOut++;
            BooksCheckedOut.Add(book);
        }

        public void ReturnBook(Book book)
        {
            if (NumOfBooksCheckedOut >= 0)
            {
                NumOfBooksCheckedOut--;
                BooksCheckedOut.Remove(book);

                if(OverdueBooks.Contains(book))
                {
                    OverdueBooks.Remove(book);
                    NumOfBooksOverdue--;
                }
            }
            else
                Console.WriteLine("No books checked out");
        }

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
        }
    }
}
