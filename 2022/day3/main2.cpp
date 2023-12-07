#include <iostream>
#include <fstream>
#include <string>
#include <set>

int priority(char c);

int main()
{
    std::ifstream ifs{"data.txt"};
    std::string sack1;
    std::string sack2;
    std::string sack3;
    int tmp = 0;

    if(ifs)
    {
        while(!ifs.eof())
        {
            std::getline(ifs,sack1);
            std::getline(ifs,sack2);
            std::getline(ifs,sack3);


            for(const char c: sack1)
            {
                if(sack2.find(c) != std::string::npos && sack3.find(c) != std::string::npos)
                {
                    tmp += priority(c);
                    break;
                }
            }
        }
    }

    std::cout << "Result is " << tmp << std::endl;

    return 0;

}

int priority(char c)
{
    return ((int)c - 33)%64;
}

//%64
//A=65 -> 1
//Z=90 -> 

//-33 % 58
//A=65 -> 32 -> 32 -> 27
//Z=90 -> 57 -> 57 -> 52
//a=97 -> 64 -> 6 -> 0
//z=122 -> 89 -> 31 -> 25