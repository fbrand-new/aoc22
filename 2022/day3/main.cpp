#include <iostream>
#include <fstream>
#include <string>
#include <set>

int priority(char c);

int main()
{
    std::ifstream ifs{"data.txt"};
    std::string line;
    int tmp = 0;

    if(ifs)
    {
        while(!ifs.eof())
        {
            std::getline(ifs,line);
            std::string firstCompartment = line.substr(0,line.size()/2);
            std::string secondCompartment = line.substr(line.size()/2,line.size());

            std::set<char> prioritySet(secondCompartment.begin(),secondCompartment.end());

            for(const char c: firstCompartment)
            {
                if(prioritySet.find(c) != prioritySet.end())
                {
                    std::cout << "found: " << c << " " << priority(c) << std::endl;
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
    return ((int)c - 33)%58-5;
}

//%64
//A=65 -> 1
//Z=90 -> 

//-33 % 58
//A=65 -> 32 -> 33 -> 27
//Z=90 -> 57 -> 58 -> 52
//a=97 -> 64 -> 6 -> 0
//z=122 -> 89 -> 31 -> 25