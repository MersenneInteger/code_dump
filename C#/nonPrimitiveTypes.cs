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
    
    //enums
    public enum ShippingMethod
    {
        RegularAirMail = 1, RegisteredAirMail = 2, Express = 3
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

            //enums
            foreach(var method in Enum.GetNames(typeof(ShippingMethod)))
            {
                Console.WriteLine(method);
            }
            var smethod = ShippingMethod.Express;
            Console.WriteLine((int)smethod);
            Console.WriteLine(smethod);
            string shippingStr = "Shipping Method: " + smethod.ToString();
            Console.WriteLine(shippingStr);
            var aMethod = "RegularAirMail";
            var shippingMethod = (ShippingMethod)Enum.Parse(typeof(ShippingMethod), aMethod);

            Console.WriteLine(shippingMethod);

            int a = 10;
            int b = a;
            b++;
            Console.WriteLine(String.Format("A: {0}, B: {1}",a, b));

            var arr1 = new int[3] {1,2,3};
            var arr2 = arr1;
            arr2[1] = 0;
            i = 0;
            for(i = 0; i < arr1.Length; i++) 
            {
                Console.WriteLine(String.Format("Arr1[{0}] = {1}",i, arr1[i]));
                Console.WriteLine(String.Format("Arr2[{0}] = {1}", i, arr2[i]));
            }

            //conditional statements and loops
            a = 5;
            b = 3;
            var c = 8;
            if(a > b)
                Console.WriteLine("a > b");
            else if(a == b)
                Console.WriteLine("a == b");
            else
                Console.WriteLine("a < b");
            
            var greater = a > b? a : b;
            Console.WriteLine(greater);

            switch(c)
            {
                case 1: 
                {
                    Console.WriteLine("blah");
                    break;
                }
                case 8: 
                {
                    Console.WriteLine("blah blah");
                    break;
                }
            }
            
            //for loop
            for(var j = 1; j <= 100; j++)
            {
                if(j % 3 == 0 && j % 5 == 0)
                    Console.WriteLine("FizzBuzz");
                else if(j % 3 == 0)
                    Console.WriteLine("Fizz");
                else if(j % 5 == 0)
                    Console.WriteLine("Buzz");
                else
                    Console.WriteLine(j);
            }
            
            //foreach loop
            var list = new int[3] {1,3,5};
            foreach(var item in list)
                Console.Write(item + " ");
            
            //random class
            var rand = new Random();
            for(var k = 0; k < 5; k++)
                Console.WriteLine(rand.Next(1,10));

            //arrays
            var numbers = new int[] {2,3,5,7,11,13};
            Console.WriteLine("Length of numbers: " + numbers.Length);
            Console.WriteLine("Index of 7: " + Array.IndexOf(numbers, 7));
            foreach(var num in numbers)
                Console.Write(num + " ");
            Console.WriteLine();
            //clear array
            Array.Clear(numbers, 0, numbers.Length);
            foreach(var num in numbers)
                Console.Write(num + " ");
            Console.WriteLine();
            
            //copy array
            var arr = new int[3]{3, 2, 1};
            var copyArr = new int[3];
            Array.Copy(arr, copyArr, 3);
            foreach(var num in copyArr)
                Console.Write(num + " ");
            Console.WriteLine();
            
            //sort array
            Array.Sort(copyArr);
            foreach(var num in copyArr)
                Console.Write(num + " ");
            Console.WriteLine();

            //lists
            var newList = new List<int>() {1,2,3,4};
            newList.Add(5);
            foreach(var item in newList)
                Console.Write(item + " ");
            Console.WriteLine();

            newList.AddRange(new int[3] {6,7,8});
            foreach(var item in newList)
                Console.Write(item + " ");
            Console.WriteLine();
            var index = newList.IndexOf(7);
            Console.WriteLine("Index of 7: " + index);
            Console.WriteLine("Count: " + newList.Count);
            newList.Remove(3);
            foreach(var item in newList)
                Console.Write(item + " ");
            Console.WriteLine();
            
        }//end of main
    }//end of class
}//end of namespace
