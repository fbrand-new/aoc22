#include <iostream>
#include <fstream>
#include <string>

bool isFullyContained(std::pair<int,int> a, std::pair<int,int> b);
bool overlaps(std::pair<int,int> a, std::pair<int,int> b);
class Elf
{
    public:

        inline static const std::string _innerDelimiter = "-";
    
        static std::pair<int,int> elfAssignment(std::string assignment)
        {
            return {std::stoi(assignment.substr(0,assignment.find(_innerDelimiter))),
                        std::stoi(assignment.substr(assignment.find(_innerDelimiter)+1,assignment.size()))};
        }

};


int main()
{
    std::ifstream ifs("data.txt");
    std::string line;
    int result = 0;

    if(ifs)
    {
        while(!ifs.eof())
        {
            std::getline(ifs,line);
            std::string delimiter = ",";
            std::string innerDelimiter = "-";
            
            std::string assignment1 = line.substr(0,line.find(delimiter));
            std::pair<int,int> elf1 = Elf::elfAssignment(assignment1);

            std::string assignment2 = line.substr(line.find(delimiter)+1,line.size());
            std::pair<int,int> elf2 = Elf::elfAssignment(assignment2);

            if(overlaps(elf1,elf2))
                result += 1;
        }
    }

    std::cout << "Result: " << result << std::endl;

}

bool isFullyContained(std::pair<int,int> a, std::pair<int,int> b)
{
    // std::cout << "pair 1 " << a.first << "," << a.second << std::endl;
    // std::cout << "pair 2 " << b.first << "," << b.second << std::endl;

    return a.first <= b.first && a.second >= b.second
            || a.first >= b.first && a.second <= b.second;
}

bool overlaps(std::pair<int,int> a, std::pair<int,int> b)
{
    return (a.first <= b.first && a.second >= b.first
            || b.first <= a.first && b.second >= a.first);
}