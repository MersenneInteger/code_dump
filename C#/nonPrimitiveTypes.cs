using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace nonPrimativeTypes
{
    public class Person
    {
        public string firstName;
        public string lastName;

        public Person()
        {
            Console.WriteLine("Initializing Person...");
        }
        public void introduce()
        {
            Console.WriteLine("This is " + firstName + " " + lastName);
        }
    }   

    public struct RgbColor
    {
        public int red;
        public int green;
        public int blue;
    }

    class Program
    {
        static void Main(string[] args)
        {
            Person john = new Person();
            john.firstName = "John";
            john.lastName = "Smith";
            john.introduce();

            RgbColor yellow;
            yellow.red = 255;
            yellow.green = 255;
            yellow.blue = 0;
            Console.WriteLine(yellow.red);
            
            var numArray = new int[3];
            int i;
            for(i = 0; i < 3; i++)
                numArray[i] = i * 3;
            Console.WriteLine(numArray[1]);
            
            var names = new string[3] {"Red", "Green", "Blue"};
            foreach (string n in names)
            {
                Console.WriteLine(n);
            }

            string fname = "John";
            string lname = "Smith";
            string fullName = string.Format("{0} {1}", fname, lname);
            Console.WriteLine(fullName);
            
            var nums = new int[3] {1,2,3};
            string nList = string.Join(",",nums);
            Console.WriteLine(nList);

            Console.WriteLine(fname[2]);

            //like python strings are immutable
            
            //normal string with back-slashes
            string path = "\\Home\\Desktop\\files\\file.txt";
            Console.WriteLine(path);
            path = @"\Home\Desktop\files\file.txt";
            Console.WriteLine(path);

            



        }
    }
}//end of namespace
