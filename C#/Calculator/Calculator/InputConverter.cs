using System;
using System.Collections.Generic;
using System.Text;

namespace Calculator
{
    class InputConverter
    {
        public double ConvertInputToNum(string argTextInput)
        {
            double convertedNum;
            if (!double.TryParse(argTextInput, out convertedNum))
                throw new ArgumentException("Expected a numeric value");
            return convertedNum;

        }
    }
}
