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

        public Student(){}

        public Student(string Username, string Password, string Name, uint Id)
        {
            this.Username = Username;
            this.Password = Password;
            this.Name = Name;
            this.Id = Id;
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
            }
            else
                Console.WriteLine("No books checked out");
        }

        public void CheckIfStudentHasBooksOverdue()
        {
            string overdueBooks = "";

            foreach(var book in BooksCheckedOut)
            {
                if(book.CheckIfBookIsOverdue())
                {
                    NumOfBooksOverdue++;
                    overdueBooks += book.GetInfo();
                }
            }
            if (NumOfBooksOverdue > 0)
                Console.WriteLine(overdueBooks);
        }
    }
}
