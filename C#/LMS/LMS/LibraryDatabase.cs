﻿using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;

namespace LMS
{
    internal class LibraryDatabase
    {
        private List<Student> StudentDatabase = new List<Student>();
        private List<Book> BookDatabase = new List<Book>();

        public void LoadLibrary()
        {
            try
            {
                string bookDB = File.ReadAllText(Path.Combine(Environment.CurrentDirectory, "json\\books.json"));
                BookDatabase = JsonConvert.DeserializeObject<List<Book>>(bookDB);
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        public Student Login(string username, string password)
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

        public void SignUp()
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

        public Book SearchBook(string title, string author)
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

        public string SearchOverdueBooks()
        {
            List<Book> overdueBooks;
            string overdueBookInfo = "";
            foreach(Student person in StudentDatabase)
            {
                overdueBooks = person.GetOverdueBooks();
                if (overdueBooks.Count > 0)
                {
                    foreach (var book in overdueBooks)
                    {
                        overdueBookInfo += string.Format("\n{0} : {1} - {2}", person.GetName(), book.GetTitle(), book.GetDuedate());
                    }
                }
            }
            return overdueBookInfo.Length > 0 ? overdueBookInfo : "No overdue books"; 
        }
    }
}
