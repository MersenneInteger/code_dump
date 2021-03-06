﻿using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;

namespace LMS
{
    internal sealed class LibraryDatabase
    {
        private List<Student> StudentDatabase = new List<Student>();
        private List<Book> BookDatabase = new List<Book>();

        /// <summary>
        /// load library of books from JSON file
        /// </summary>
        public void LoadLibrary()
        {
            try
            {
                List<BookBuild> bookBuild;
                
                string bookDB = File.ReadAllText(Path.Combine(Environment.CurrentDirectory, "json\\books.json"));
                bookBuild = JsonConvert.DeserializeObject<List<BookBuild>>(bookDB);

                foreach(BookBuild book in bookBuild)
                    BookDatabase.Add(new Book(book.Title, book.Author, false));
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        /// <summary>
        /// Allow a Student to login using username and password
        /// </summary>
        /// <param name="username">String</param>
        /// <param name="password">String</param>
        /// <returns>Student</returns>
        public Student Login()
        {
            string username, password;
            Console.Write("Enter username: ");
            username = Console.ReadLine();
            Console.Write("Enter password: ");
            password = Console.ReadLine();

            foreach (Student person in StudentDatabase)
            {
                if(person.GetUsername().Equals(username) && person.ComparePasswords(password))
                {
                    return person;
                }
            }
            return null;
        }

        /// <summary>
        /// Sign Student up for the library database, register name, id, username and password
        /// </summary>
        public bool SignUp()
        {
            string username, password;

            Console.Write("1) Enter your Username: ");
            username = Console.ReadLine();

            Console.Write("2) Enter your password: ");
            password = Console.ReadLine();

            foreach(Student person in StudentDatabase)
            {
                if(person.GetUsername().Equals(username))
                {
                    Console.WriteLine("That username is already taken. Please try again with a different username");
                    return false;
                }
            }

            StudentDatabase.Add(new Student(username, password));
            Console.WriteLine("Welcome. You can now login\n");
            return true;
        }

        /// <summary>
        /// Search for book in BookDatabase
        /// </summary>
        /// <param name="title">String</param>
        /// <param name="author">String</param>
        /// <returns>Book</returns>
        public Book SearchBook(string keyword)
        {
            foreach (Book book in BookDatabase)
            {
                if (book.GetTitle().Equals(keyword))
                {
                    return book;
                }
            }
            return null;
        }

        /// <summary>
        /// Search BookDatabase for overdue books, return list of overdue books
        /// </summary>
        /// <returns>String</returns>
        public string SearchOverdueBooks()
        {
            List<Book> overdueBooks;
            string overdueBookInfo = "";

            foreach (Student person in StudentDatabase)
            {
                overdueBooks = person.GetOverdueBooks();
                if (overdueBooks.Count > 0)
                {
                    foreach (var book in overdueBooks)
                    {
                        overdueBookInfo += string.Format($"\n{book.GetInfo()}");
                    }
                }
            }
            return overdueBookInfo.Length > 0 ? overdueBookInfo : "No overdue books"; 
        }

        /// <summary>
        /// return string of all books available for checkout
        /// </summary>
        /// <returns>String</returns>
        public string SearchForAvailableBooks()
        {
            string availableBooks = "";

            foreach(Book book in BookDatabase)
            {
                if(book.CheckIfBookIsCheckedOut() == false)
                {
                    availableBooks += string.Format("\n{0} - {1}", book.GetTitle(), book.GetAuthor());
                }
            }
            if (availableBooks.Length > 0)
                return availableBooks;
            else
                return "No books available to check out at the moment";
        }
    }
}
