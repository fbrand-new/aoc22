#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>

int main()
{
    std::ifstream ifs("data.txt");
    std::string line;
    std::list<std::list<char>> stacks;

    bool phase1 = true;

    if(ifs)
    {
        while(phase1)
        {
            std::getline(ifs,line);

            if(line == "")
            {
                phase1 = false;
                break;
            }

            int pos = 0;
            
            std::list<char> hStack;
            while(pos < line.size())
            {
                std::string elem = line.substr(pos,pos+4);
                char elemChar = elem.substr(1,1)[0];
                
                hStack.push_back(elemChar);
                pos += 4;
            }

            stacks.push_back(hStack);
        }

        std::vector<std::list<char>> vStacks(stacks.front().size());

        for(const auto& s: stacks)
        {
            int i = 0;
            for(const auto& c: s)
            {
                if(c != ' ')
                    vStacks[i].push_front(c);

                ++i;
            }
        }

        while(!ifs.eof())
        {
            //std::cout << std::endl;
            std::getline(ifs,line);

            std::string delimiter = " ";
            int pos = 0;
            int k = 0;
            int pos_end = 0;
            std::vector<int> moveFromTo(3);

            //std::cout << line.find(delimiter,pos) << std::endl;
            //std::cout << line << std::endl;
            
            while((pos_end = line.find(delimiter,pos)) != std::string::npos)
            {
                // std::cout << line << std::endl;
                //std::cout << line.substr(pos,pos_end-pos) << ",";
                //std::cout << k << std::endl;
                if(k%2)
                {
                    //std::cout << k/2 << std::endl;
                    moveFromTo[k/2] = std::stoi(line.substr(pos,pos_end));
                    //std::cout << std::stoi(line.substr(pos,pos_end));
                }
                pos = pos_end+1;
                k += 1;
            }
            moveFromTo[2] = std::stoi(line.substr(pos));
            
            // for(auto i: moveFromTo)
            //     std::cout << i << " ";

            auto it = vStacks[moveFromTo[1]-1].begin();
            std::advance(it, vStacks[moveFromTo[1]-1].size()-moveFromTo[0]);
            vStacks[moveFromTo[2]-1].splice(vStacks[moveFromTo[2]-1].end(),
                                            vStacks[moveFromTo[1]-1],it,vStacks[moveFromTo[1]-1].end());

            // for(int i=0; i<moveFromTo[0]; ++i) //Move
            // {
            //     //std::cout << vStacks[moveFromTo[1]-1].back() << std::endl;
            //     vStacks[moveFromTo[2]-1].push_back(vStacks[moveFromTo[1]-1].back()); //To - From
            //     vStacks[moveFromTo[1]-1].pop_back();
            // }
        }

        // for(auto s: vStacks)
        // {
        //     for(auto i: s)
        //         std::cout << i << " ";

        //     std::cout << std::endl;
        // }


        std::cout << "The message is: ";

        for(size_t i=0; i<vStacks.size(); ++i)
            std::cout << vStacks[i].back();

        std::cout << std::endl;
    }
}