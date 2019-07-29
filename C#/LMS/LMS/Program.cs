using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LMS
{
    class Program
    {
        static void Main(string[] args)
        {
            string continueOperations = "yes";
            string title;
            ushort menuNavValue = 0;
            bool signedIn = false;
            LibraryDatabase libraryDB = new LibraryDatabase();
            Student user = new Student();

            //load library from JSON file
            libraryDB.LoadLibrary();

            while (continueOperations.Equals("yes", StringComparison.OrdinalIgnoreCase))
            {
                if (!signedIn)
                {
                    //prompt login or signup
                    Console.WriteLine("\nWelcome to X library. Please choose one of the following:" +
                                    "\n1) Login\n2)Sign Up\n3)Quit");

                    try
                    {
                        menuNavValue = Convert.ToUInt16(Console.ReadLine());
                    }
                    catch (Exception e)
                    {
                        Console.WriteLine(e.Message);
                        Console.Clear();
                        continue;
                    }

                    if (menuNavValue > 3 || menuNavValue < 1) //out of range
                    {
                        Console.WriteLine("Please enter a valid operation");
                        menuNavValue = 0;
                        Console.Clear();
                        continue;
                    }
                    else if (menuNavValue == 3) //quit
                    {
                        Console.Clear();
                        break;
                    }
                    else if (menuNavValue == 1) //login
                    {
                        user = libraryDB.Login();
                        if (ValidateLogin(user) == false)
                        {
                            ClearConsole();
                            continue;
                        }
                        else
                        {
                            Console.WriteLine("Login Successful");
                            signedIn = true;
                            ClearConsole();
                        }
                    }
                    else if (menuNavValue == 2) //signup
                    {
                        if (libraryDB.SignUp() == false)
                        {
                            ClearConsole();
                            continue;
                        }
                        user = libraryDB.Login();
                        if (ValidateLogin(user) == false)
                        {
                            ClearConsole();
                            continue;
                        }
                        else
                        {
                            Console.WriteLine("Login Successful");
                            signedIn = true;
                            ClearConsole();
                        }
                    }
                }

                //prompt available operations:
                Console.WriteLine("Choose one of the following: " +
                    "\n1)Return book\n2)Check out book\n3)Check if you have overdue books\n4)Quit");
                try
                {
                    menuNavValue = Convert.ToUInt16(Console.ReadLine());
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                    Console.Clear();
                    signedIn = false;
                    continue;
                }

                if (menuNavValue == 4) //quit
                {
                    Console.Clear();
                    signedIn = false;
                    break;
                }
                else if (menuNavValue > 4 || menuNavValue < 1) //out of range
                {
                    Console.WriteLine("Please enter a valid operation");
                    menuNavValue = 0;
                    Console.Clear();
                    continue;
                }
                else if (menuNavValue == 1) //return book
                {
                    Console.WriteLine("Currently checked out: \n");
                    user.ViewBooksCheckedOut();
                    Console.WriteLine("Enter the title of the name of the book you would like to return");
                    title = Console.ReadLine();
                    Book book = user.GetBookByTitle(title);
                    if (book != null)
                    {
                        user.ReturnBook(book);
                        Console.WriteLine("Book returned. Thank you\n");
                    }
                    else
                    {
                        Console.WriteLine("That book is not currently checked out under your name");
                        signedIn = false;
                        continue;
                    }
                }
                else if(menuNavValue == 2) //check out book
                {
                    Console.WriteLine("Enter the title of the name of the book you would like to check out");
                    title = Console.ReadLine();
                    Book book = libraryDB.SearchBook(title);
                    if(book != null)
                    {
                        user.CheckOutBook(book);
                        Console.WriteLine("{0} checked out", book.GetTitle());
                        continue;
                    }
                    else
                    {
                        Console.WriteLine("Book is currently unavailable");
                        continue;
                    }
                }
                else if(menuNavValue == 3) //check for overdue books
                {
                    user.CheckIfStudentHasBooksOverdue();
                    continue;
                }

                menuNavValue = 0;
                Console.Write("Continue operations? (yes/no) ");
                continueOperations = Console.ReadLine();
            }
        }

        /// <summary>
        /// Check is Student object is null which indicates an unsuccessful login
        /// </summary>
        /// <param name="user">Student</param>
        /// <returns>Bool</returns>
        static bool ValidateLogin(Student user)
        {
            if (user == null)
            {
                Console.WriteLine("Invalid login or password. Please try again.");
                return false;
            }
            return true;
        }

        /// <summary>
        /// Sleep for 1 sec and clear console
        /// </summary>
        static void ClearConsole()
        {
            System.Threading.Thread.Sleep(100);
            Console.Clear();
        }
    }
}
