using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Intro
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            int num = 4;
            const double PI = 3.14;
            string str = "Hello World";
            Console.WriteLine("Num: {0}, PI: {1}, str: {2}",num, PI, str);
            bool isFalse = true;
            if (isFalse)
                Console.WriteLine("isFalse is {0}", isFalse);
            else
                Console.WriteLine("jfdklfjdsl");
            byte smallInt = 255;
            Console.WriteLine(smallInt);
            char ch = 'A';
            Console.WriteLine(ch + 1);

            //intentionally causing an overflow
            smallInt++; //will be 0
            Console.WriteLine(smallInt);

            //use checked to prevent overflows
            /*
            smallInt = 255;
            checked {
                smallInt++;
                Console.WriteLine(smallInt);
            }//will throw exception
            */

            byte number = 2;
            Console.WriteLine(number);

            var d = 3;
            var s = "string";
            Console.WriteLine(d);
            Console.WriteLine(s);

            Console.WriteLine("{0}-{1}", byte.MinValue, byte.MaxValue);
            Console.WriteLine("{0}-{1}", int.MinValue, int.MaxValue);
            Console.WriteLine("{0}-{1}", float.MinValue, float.MaxValue);

            float pi = 3.14f;
            Console.WriteLine(pi);

            //type conversion
            //implicity conversion
            byte b = 1;
            int i = b;
            float f = i;

            //this will work because each conversion is a successively bigger data type
            //this wont compile
            //int i = 3;
            //byte b = i; //wont compile

            //explicit conversion
            int j = 1;
            byte c = (byte)j;

            float ff = 1.2f;
            int ii = (int)ff; //causes data lose, explicity casting required

            //some types are just incompatable
            s = "1";
            i = Convert.ToInt32(s);
            j = int.Parse(s);

            s = "1234";
            i = Convert.ToInt32(s);
            Console.WriteLine(i);

            try
            {
                b = Convert.ToByte(s); //will cause overflow
            }
            catch(Exception)
            {
                Console.WriteLine("number cannot be converted to byte");
            }
        }//end main
    }//end class
}//end namespace
