#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{

    std::string tmp;
    int elf = 0;
    std::vector<int> max(3);

    std::ifstream ifs("data.txt");

    if(ifs)
    {
        while(!ifs.eof())
        {
            std::getline(ifs,tmp);
            if(tmp == "")
            {
                if(max[0] < elf)
                {
                    max[0] = elf;
                    std::sort(max.begin(),max.end());
                }
                elf = 0;
            }
            else
            {
                elf += std::stoi(tmp);
            }
        }
    }

    std::cout << "The result you are looking for is: " << max[0]+max[1]+max[2] << std::endl;

}