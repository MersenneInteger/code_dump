using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace oddsNEnds
{
    class program
    {
        static void Main(string[] args)
        {
            //date and time
            //var dateTime = new DateTime(2015, 1, 1);
            var now = DateTime.Now;
            var today = DateTime.Today;

            Console.WriteLine("hour: " + now.Hour);
            Console.WriteLine("minute: " + now.Minute);

            //var tomorrow = now.AddDays(1);
            //var yesterday = now.AddDays(-1);

            Console.WriteLine(now.ToLongDateString());
            Console.WriteLine(now.ToShortDateString());
            Console.WriteLine(now.ToLongTimeString());
            Console.WriteLine(now.ToShortTimeString());
            Console.WriteLine(now.ToString("yyyy-MM-dd hh"));

            var timeSpan = new TimeSpan(1,2,3);
            var timeSpan1 = new TimeSpan(1,0,0);
            var timeSpan2 = TimeSpan.FromHours(1);
            Console.WriteLine(timeSpan + "\n" + timeSpan1 + "\n" + timeSpan2);

            var start = DateTime.Now;
            var end = DateTime.Now.AddMinutes(2);
            var duration = end - start;
            Console.WriteLine("Duration: " + duration);
            Console.WriteLine(timeSpan.Minutes);
            Console.WriteLine(timeSpan.TotalMinutes);
            Console.WriteLine(timeSpan.Add(TimeSpan.FromMinutes(8)));

            var timeStr = timeSpan.ToString();
            Console.WriteLine(timeStr);

            //strings

            var fullName = "Mosh Hamedani";
            Console.WriteLine("Trim: {0}", fullName.Trim());
            Console.WriteLine(fullName.ToUpper());
            Console.WriteLine(fullName.ToLower());
            var index = fullName.IndexOf(' ');
            var firstName = fullName.Substring(0, index);
            var lastName = fullName.Substring(index + 1);
            Console.WriteLine("First Name: " + firstName);
            Console.WriteLine("Last Name: " + lastName); 
            var names = fullName.Split(' ');
            Console.WriteLine(names[1]); //lastName
            Console.WriteLine(fullName.Replace("o", "O"));
            
            if(String.IsNullOrEmpty(null))
                Console.WriteLine("Invalid String");
            if(String.IsNullOrEmpty(""))
                Console.WriteLine("Invalid String");

            var str = "25";
            Convert.ToInt32(str);
            var age = "24";
            Convert.ToByte(age);
            float price = 29.95f;
            price.ToString("C1"); //to format with currency

            //stringbuilder class
            var strBuilder = new StringBuilder();
            strBuilder.Append('-', 10);
            strBuilder.AppendLine();
            strBuilder.Append("Header");
            strBuilder.AppendLine();
            strBuilder.Replace('-', '+');
            strBuilder.Remove(0, 10);
            strBuilder.Insert(0, new string('-', 10));
            Console.WriteLine(strBuilder);

            //files and directories
            /*
            var path = @"/home/carlyle/copy.txt";
            File.Create("test.txt");          
            File.Create(path);
            File.WriteAllText("test.txt", "string");
            File.Copy("test.txt", "testCopy.txt"); 
            var path = @"/home/carlyle/copy.txt";
            File.Copy("test.txt", path, true);
            File.Delete(path);
            if(File.Exists(path))
            {
                Console.WriteLine(path + " exists");
            }
            var content = File.ReadAllText(path);
            var fileInfo = new FileInfo(path);
            fileInfo.CopyTo("...");
            fileInfo.Delete();
            var fileStr = fileInfo.OpenRead();
            */
            Directory.CreateDirectory(@"/home/carlyle/testDir");
            var files = Directory.GetFiles(@"/home/carlyle/Pictures","*.", SearchOption.AllDirectories);
            foreach(var file in files)
                Console.WriteLine(file);
            var directories = Directory.GetDirectories(@"/home/carlyle/",".", SearchOption.AllDirectories);
            foreach(var directory in directories)
                Console.WriteLine(directory);


        }//end of main
    }//end of class
}//end of namespace
