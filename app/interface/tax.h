#ifndef TAX_H
#define TAX_H

#include <string>
#include <iostream>
#include <cstring>

using namespace std;

class Tax
{
    public:
        static const double MINIMUM_TAXABLE = 34000;

    public:
        static bool isTaxable(double salary)
        {
            double annual = salary * 0xC;

            if (annual > MINIMUM_TAXABLE)
            {
                return true;
            }

            return false;
        }

    public:
        static double getTaxableRate(double salary)
        {
            double annual = salary * 0xC;

            if (isTaxable(salary))
            {
                if (annual <= 5000) return 0x0;
                if (annual <= 20000) return 0x1;
                if (annual <= 35000) return 0x3;
                if (annual <= 50000) return 0x8;
                if (annual <= 70000) return 0xE;
                if (annual <= 100000) return 0x15;
                if (annual <= 250000) return 0x18;
                if (annual <= 400000) return 24.5;
                if (annual <= 600000) return 0x19;
                if (annual <= 1000000) return 0x1A;
                if (annual > 1000000) return 0x1C;
            }

            std::cout << "The amount is not taxable";

            return 0;
        }
};

#endif