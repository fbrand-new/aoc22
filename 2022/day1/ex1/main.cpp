#include <iostream>
#include <fstream>
#include <string>

int main()
{

    std::string tmp;
    int elf = 0;
    int max = 0;

    std::ifstream ifs("data.txt");

    if(ifs)
    {
        while(!ifs.eof())
        {
            std::getline(ifs,tmp);
            if(tmp == "")
            {
                if(max < elf)
                {
                    max = elf;
                }
                elf = 0;
            }
            else
            {
                elf += std::stoi(tmp);
            }
        }
    }

    std::cout << "The result you are looking for is: " << max << std::endl;

}