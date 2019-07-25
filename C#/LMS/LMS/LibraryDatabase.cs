using System;
using System.Collections.Generic;
using Newtonsoft.Json;

namespace LMS
{
    internal class LibraryDatabase
    {
        private List<Student> StudentDatabase = new List<Student>();
        private List<Book> BookDatabase = new List<Book>();

        private void LoadLibrary()
        {

        }

        private Student Login(string username, string password)
        {
            foreach(Student person in StudentDatabase)
            {
                if(person.GetUsername().Equals(username) && person.ComparePasswords(password))
                {
                    return person;
                }
            }
            return null;
        }

        private void SignUp()
        {
            string username, password, name;
            uint id;

            Console.Write("1) Enter your Name: ");
            name = Console.ReadLine();
            Console.Write("2) Enter your student ID: ");
            id = Convert.ToUInt16(Console.ReadLine());
            Console.Write("3) Enter your Username: ");
            username = Console.ReadLine();
            Console.Write("4) Enter your password: ");
            password = Console.ReadLine();

            StudentDatabase.Add(new Student(username, password, name, id));
            Console.WriteLine("Welcome. You can now login");
        }

        private Book SearchBook(string title, string author)
        {
            foreach (Book book in BookDatabase)
            {
                if (book.GetTitle().Equals(title) && book.GetAuthor().Equals(author))
                {
                    return book;
                }
            }
            return null;
        }

        private void SearchOverdueBooks()
        {

        }
    }
}
