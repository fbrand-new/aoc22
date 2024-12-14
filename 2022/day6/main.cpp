#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::ifstream ifs("data.txt");
    char c;
    std::string packet;
    bool duplicated = false;

    if(ifs)    
    {
        while(!ifs.eof())
        {
            ifs.get(c);
            packet.push_back(c);

            int n = packet.size();
            if(n>=14){
                for(int i=n-14; i<n ; ++i){
                    // std::string marker = packet.substr(i,n);
                    // marker.find
                    //if(packet[i] == packet[i-1])
                    for(int j=i+1;j<n;++j)
                    {
                        if(packet[i] == packet[j])
                            duplicated = true;
                    }
                }
            }
            else{
                duplicated = true;
            }

            if(!duplicated){
                std::cout << packet.size() << std::endl;
                return 0;
            }
            else{
                duplicated = false;
            }   


        }
    }
}