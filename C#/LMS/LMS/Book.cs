using System;

namespace LMS
{
    internal class Book
    {
        private string Title;
        private string Author;
        private bool CheckedOut;
        private DateTime CheckOutDate;
        private DateTime ReturnDate;

        private Book(string Title, string Author, bool CheckedOut)
        {
            this.Title = Title;
            this.Author = Author;
            this.CheckedOut = CheckedOut;
        }

        private void CheckOutBook()
        {
            this.CheckedOut = true;
        }

        private void ReturnBook()
        {
            this.CheckedOut = false;
        }

        private void CheckIfBookIsOverdue()
        {

        }
    }
}
