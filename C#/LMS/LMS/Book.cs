using System;

namespace LMS
{
    internal class Book
    {
        private string Title;
        private string Author;
        private bool CheckedOut;
        private DateTime CheckOutDate;
        private DateTime DueDate;
        private DateTime CurrentDate;
        private const int CheckoutPeriod = 14;

        public Book(){}

        public Book(string Title, string Author, bool CheckedOut)
        {
            this.Title = Title;
            this.Author = Author;
            this.CheckedOut = CheckedOut;
        }

        /// <summary>
        /// Return Title of Book
        /// </summary>
        /// <returns>String</returns>
        public string GetTitle()
        {
            return Title;
        }

        /// <summary>
        /// Return Author of Book
        /// </summary>
        /// <returns>String</returns>
        public string GetAuthor()
        {
            return Author;
        }

        /// <summary>
        /// Return DueDate as DateTime object
        /// </summary>
        /// <returns>String</returns>
        public string GetDuedate()
        {
            return string.Format("{0}/{1}/{2}", DueDate.Month, DueDate.Day, DueDate.Year);
        }

        /// <summary>
        /// Checkout book and assign CheckOutdate and DueDate (checkOutDate + 2 weeks)
        /// </summary>
        public void CheckOutBook()
        {
            CheckedOut = true;
            CheckOutDate = DateTime.Today;
            CalculateDueDate(CheckOutDate);
        }

        /// <summary>
        /// Return book
        /// </summary>
        public void ReturnBook()
        {
            CheckedOut = false;
            CheckOutDate = DateTime.MinValue;
            DueDate = DateTime.MinValue;
            
        }

        /// <summary>
        /// utility function to calculate DueDate
        /// </summary>
        /// <param name="checkOutDate">DateTime</param>
        private void CalculateDueDate(DateTime checkOutDate)
        {
            DueDate = checkOutDate.AddDays(CheckoutPeriod);
        }

        /// <summary>
        /// Return boolean value if Book is currently checked out
        /// </summary>
        /// <returns></returns>
        public bool CheckIfBookIsCheckedOut()
        {
            return CheckedOut;
        }

        /// <summary>
        /// Check if Book is overdue and return boolean value
        /// </summary>
        /// <returns>Bool</returns>
        public bool CheckIfBookIsOverdue()
        {
            CurrentDate = DateTime.Today;
            Console.WriteLine("{0}/{1}", CurrentDate.Day, CurrentDate.Month);

            if(CurrentDate.Day == DueDate.Day && CurrentDate.Month == DueDate.Month)
            {
                Console.WriteLine("Book is due today");
                return false;
            }
            else if(CurrentDate.Day > DueDate.Day && CurrentDate.Month >= DueDate.Month)
            {
                Console.WriteLine("Book is overdue");
                return true;
            }
            else if(CurrentDate.Day < DueDate.Day && CurrentDate.Month <= DueDate.Month)
            {
                Console.WriteLine("Book is due {1}", DueDate.Date);
                return false;
            }
            return false;
        }

        /// <summary>
        /// Return information about Book
        /// </summary>
        /// <returns></returns>
        public string GetInfo()
        {
            return string.Format("Title: {0}\nAuthor: {1}\nCheckout Date: {2}\nDue: {3}", 
                this.Title, this.Author, this.CheckOutDate.Date, this.DueDate.Date);
        }
    }
}
