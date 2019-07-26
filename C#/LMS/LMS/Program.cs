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
            LibraryDatabase libraryDB = new LibraryDatabase();
            Console.WriteLine(Environment.CurrentDirectory);
            //load library from JSON file

            while(continueOperations.Equals("yes", StringComparison.OrdinalIgnoreCase))
            {
                libraryDB.LoadLibrary();
                //prompt login or signup

                //prompt available operations:
                    //prompt return book if books are checked out
                    //prompt checkout book if
                        //books available for checkout
                        //student has no unpaid late fees
                    //see available books
                    //search for a book

                Console.Write("Continue operations? (yes/no) ");
                continueOperations = Console.ReadLine();
            }
        }
    }
}
