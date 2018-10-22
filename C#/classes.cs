using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Classes
{
    public class Person
    {
        public string Name;
        private DateTime _birthDate;
        
        public Person()
        {
            Console.WriteLine("Initializing new Person");
        }

        public Person(string name)
        {
            Console.WriteLine("Initializing new Person");
            this.Name = name;
        }

        public void SetBirthDate(DateTime bday)
        {
            this._birthDate = bday;
        }

        public DateTime GetBirthDate()
        {
            return this._birthDate;
        }

        public void Introduce()
        {
            Console.WriteLine("Hi {0}", this.Name);
        }

        public static Person Parse(string name)
        {
            var person = new Person();
            person.Name = name;
            return person;
        }
    }

    public class Customer
    {
        public int id
        {
            get; set;
        }

        public string name
        {
            get; set;
        }

        public Customer(int id)
        {
            this.id = id;
        }

        public Customer(int id, string name)
        {
            this.id = id;
            this.name = name;
        }

        public static int refExample(ref int n)
        {
            return ++n;
        }
        
        public static void outExample(out int n)
        {
            n = 10;
        }
    }

    public class Point
    {
        public int X;
        public int Y;

        public Point(int x, int y)
        {
            this.X = x;
            this.Y = y;
        }

        public void Move(int x, int y)
        {
            this.X = x;
            this.Y = y;
        }

        public void Move(Point newLocation)
        {
            if(newLocation == null)
                throw new ArgumentNullException("new location");
            Move(newLocation.X, newLocation.Y);
        }
    }

    class HttpCookie
    {
        private readonly Dictionary<string, string> _dict;

        public HttpCookie()
        {
            _dict = new Dictionary<string, string>();
        }
        
        public string this[string key]
        {
            get { return _dict[key]; }
            set { _dict[key] = value; }
        }
    }
    
    public class PresentationObject
    {
        public int Width { get; set; }
        public int Heigth { get; set; }

        public void Copy()
        {
            Console.WriteLine("Object copied to clipboard");
        }

        public void Duplicate()
        {
            Console.WriteLine("Object was duplicated");
        }
    }

    public class Text : PresentationObject
    {
        public int FontSize { get; set; }
        public string FontName { get; set; }

        public void AddHyperLink(string url)
        {
            Console.WriteLine("Link: " + url + " added");
        }
    }

    public class Logger
    {
        public void Log(string msg)
        {
            Console.WriteLine(msg);
        }
    }

    public class DBMigrator
    {
        private readonly Logger _logger;

        public DBMigrator(Logger logger)
        {
            this._logger = logger;
        }

        public void Migrate()
        {
            this._logger.Log("Migration complete");
        }
    }

    public class Installer
    {
        private readonly Logger _logger;

        public Installer(Logger logger)
        {
            this._logger = logger;
        }

        public void Install()
        {
            this._logger.Log("Installing application");
        }
    }

    public class Animal
    {
        private int numOfLegs;
        private bool hasTail;

        public Animal()
        {

        }

        public Animal(int numOfLegs, bool hasTail)
        {
            this.numOfLegs = numOfLegs;
            this.hasTail = hasTail;
        }

        public void setNumOfLegs(int n)
        {
            this.numOfLegs = n;
        }

        public int getNumOfLegs()
        {
            return this.numOfLegs;
        }

        public void setHasTail(bool hasTail)
        {
            this.hasTail = hasTail;
        }

        public bool getHasTail()
        {
            return this.hasTail;
        }
    }

    public class Dog : Animal
    {
        private bool hasSpots;

        public Dog()
        {

        }

        public Dog(int numOfLegs, bool hasTail, bool hasSpots)
            : base(numOfLegs, hasTail)
        {
            this.hasSpots = hasSpots;
        }

        public bool getHasSpots()
        {
            return this.hasSpots;
        }
    }

    //method overriding example
/*
    public class Shape
    {
        public int Width { get; set; }
        public int Height { get; set; }

        public virtual void Draw();
    }
*/
    //abstract version of Shape
    public abstract class Shape
    {
        public int Width { get; set; }
        public int Height { get; set; }

        public abstract void Draw();
    }

    public class Circle : Shape
    {
        public override void Draw()
        {
            Console.WriteLine("Drawing a circle");
            //base.Draw()
        }
    }

    public class Rectangle : Shape
    {
        public override void Draw()
        {
            Console.WriteLine("Drawing a rectangle");
        }
    }

    public class Canvas
    {
        public void DrawShapes(List<Shape> shapes)
        {
            foreach(var shape in shapes)
            {
                shape.Draw();
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var person = new Person();
            person.Name = "John";
            person.Introduce();

            var newPerson = Person.Parse("Allen");
            newPerson.Introduce();

            var customer = new Customer(4, "John");
            Console.WriteLine(customer.id);

            int num = 6;
            int number = 1;
            Customer.refExample(ref num);
            Console.WriteLine(num);
            Customer.outExample(out number);
            Console.WriteLine(number);

            var p2 = new Person();
            p2.SetBirthDate(new DateTime(1888, 1, 1));
            Console.WriteLine(p2.GetBirthDate());

            //dictionary
            var map = new Dictionary<string, string>();
            map["name"] = "John";
            map["age"] = "24";
            Console.WriteLine("Name: {0}, Age: {1}", map["name"], map["age"]);

            var cookie = new HttpCookie();
            cookie["name"] = "Mosh";
            Console.WriteLine(cookie["name"]);

            //inheritance
            var text = new Text();
            text.FontSize = 3;
            text.FontName = "Comic Sans";
            text.Copy(); //calling base classes method
            
            //composition
            var dbm = new DBMigrator(new Logger());
            var logger = new Logger();
            var installer = new Installer(logger);
            dbm.Migrate();
            installer.Install();

            Dog spot = new Dog(4, true, false);
            Console.WriteLine(spot.getNumOfLegs());
            Console.WriteLine(spot.getHasTail());
            Console.WriteLine(spot.getHasSpots());
            
            Dog fifi = new Dog();
            Animal newDog = fifi;

            Dog fifiClone = (Dog)newDog;
            fifiClone.setNumOfLegs(3);
            if (fifiClone is Dog)
                Console.WriteLine("fifi # of legs: " + fifiClone.getNumOfLegs());
            //as keyword
            Dog harv = newDog as Dog;
            if (harv != null)
                Console.WriteLine("successful cast");
            
            //boxing unboxing
            var list = new ArrayList();
            list.Add(1);
            list.Add("Mosh");
            list.Add(DateTime.Today);
            
           // var genList = new List<int>();
           // genList.Add("Mosh");
           // Console.WriteLine(genList[0]);

            //method overriding
            var shapes = new List<Shape>();
            shapes.Add(new Circle());
            shapes.Add(new Rectangle());

            var canvas = new Canvas();
            canvas.DrawShapes(shapes);

        }//end of main
    }//end of class
}//end of namespace
