using System;

namespace Calculator
{
    class Program
    {
        static void parseInput(ref double targetVar)
        {
            if (!double.TryParse(Console.ReadLine(), out targetVar))
                throw new ArgumentException("Expected a numeric value");
        }

        static void Main(string[] args)
        {
            try
            {
                while (true)
                {
                    Calculator calculator = new Calculator();

                    double operand1 = 0, operand2 = 0;
                    parseInput(ref operand1);
                    string operation = Console.ReadLine();
                    parseInput(ref operand2);
                    Console.WriteLine("= " + calculator.Calculate(operand1, operand2, operation) + "\n");
                }
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }
    }
}