#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>

std::vector<std::string> split(std::string& aString);

auto main() -> int
{
    std::ifstream ifs("test.dat");
    std::string line;

    std::set<std::pair<int,int>> tailPositions;
    std::pair<int,int> position{0,0};

    if(ifs)
    {
        while(!ifs.eof())
        {
            std::getline(ifs,line);

            //Read the line
            //std::string direction = line.substr(0,line.find(" "));
            //std::string steps = line.substr
            std::vector<std::string> aParsedLine = split(line);

            for(auto s: aParsedLine)
                std::cout << s << std::endl; //It freaking works!
            
        }
    }
}

std::vector<std::string> split(std::string& aString)
{
    std::vector<std::string> aParsedString;
    
    size_t start = 0;
    size_t pos = 0;
    //size_t pos = aString.find(" ",start);
    while((pos = aString.find(" ",start)) != std::string::npos)
    {
        aParsedString.push_back(aString.substr(start,pos));
        start = pos+1;
    }

    aParsedString.push_back(aString.substr(start,aString.size()));

    return aParsedString;
}