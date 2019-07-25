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

        public string GetTitle()
        {
            return Title;
        }

        public string GetAuthor()
        {
            return Author;
        }

        public void CheckOutBook()
        {
            CheckedOut = true;
            CheckOutDate = DateTime.Today;
            CalculateDueDate(CheckOutDate);
        }

        public void ReturnBook()
        {
            CheckedOut = false;
            CheckOutDate = DateTime.MinValue;
            DueDate = DateTime.MinValue;
            
        }

        private void CalculateDueDate(DateTime checkOutDate)
        {
            DueDate = checkOutDate.AddDays(CheckoutPeriod);
        }

        public bool CheckIfBookIsCheckedOut()
        {
            return CheckedOut;
        }

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

        public string GetInfo()
        {
            return string.Format("Title: {0}\nAuthor: {1}\nCheckout Date: {2}\nDue: {3}", 
                this.Title, this.Author, this.CheckOutDate.Date, this.DueDate.Date);
        }
    }
}
