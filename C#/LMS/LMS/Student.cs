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
        private uint NumOfBooksCheckedOut;
        private uint NumOfBooksOverdue;
        private List<Book> BooksCheckedOut = new List<Book>();

        private Student()
        {

        }

        private Student(string Username, string Password, string Name, uint Id)
        {
            this.Username = Username;
            this.Password = Password;
            this.Name = Name;
            this.Id = Id;
        }
    }
}
