using System;

namespace Calculator
{
    class Calculator
    {
        public double Calculate(double op1, double op2, string operation)
        {
            switch (operation)
            {
                case ("+"):
                    return op1 + op2;
                case ("-"):
                    return op1 - op2;
                case ("*"):
                    return op1 * op2;
                case ("/"):
                    try
                    {
                        return op1 / op2;
                    }
                    catch
                    {
                        throw new DivideByZeroException();
                    }
                case ("^"):
                    checked
                    {
                        return Math.Pow(op1, op2);
                    }
                default:
                    throw new InvalidOperationException("Operation is invalid");
            }
        }
    }
}
