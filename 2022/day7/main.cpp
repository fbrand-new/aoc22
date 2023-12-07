#include <iostream>
#include <fstream>
#include <string>
#include <memory>
#include <map>
#include <vector>
#include <numeric>
#include <functional>

class Tree;
void cd(std::shared_ptr<Tree>& fileSystem, std::string dir);
void ls(std::shared_ptr<Tree>& fileSystem, std::string elemInDir);
int sumDir(int a, std::pair<std::string,std::shared_ptr<Tree>> b);
void computeDim(std::shared_ptr<Tree>& fileSystem);
int baseComputeDim(std::shared_ptr<Tree>& fileSystem);
std::map<std::shared_ptr<Tree>,int> bfsSmall(std::shared_ptr<Tree>& fileSystem);
void baseBfsSmall(std::shared_ptr<Tree>& fileSystem, std::map<std::shared_ptr<Tree>,int>& smallEnough);
void printTree(std::shared_ptr<Tree>& fileSystem);

class Tree{

    public:     
        int _val;
        // std::shared_ptr<std::vector<Tree>> sons;
        std::map<std::string,std::shared_ptr<Tree>> sons;
        std::weak_ptr<Tree> parent;

        Tree() = default;
        Tree(int val) :
            _val{val}
            {}
};

int main(){

    std::ifstream ifs("test.txt");
    std::string line;
    std::string command;
    std::string dir;

    std::shared_ptr<Tree> fileSystem = std::make_shared<Tree>();
    std::shared_ptr<Tree> root = fileSystem;

    if(ifs)
    {
        while(!ifs.eof())
        {
            std::getline(ifs,line);

            // cd moves between tree levels
            // ls shows level
            if(line[0] == '$') //It's a command
            {
                size_t start = 2; //Hardcoded: a command always starts with $ cmd
                const size_t npos = line.find(" ",start);
                std::cout << "npos: " << npos << std::endl;
                command = line.substr(start,npos-start);
                std::cout << command << std::endl;
                if(command == "cd")
                {
                    start = npos+1;
                    std::cout << start << std::endl;
                    dir = line.substr(start,line.find(" ",start)-start);
                    std::cout << dir << std::endl;
                    cd(fileSystem,dir);
                }
            }
            else 
            {
                ls(fileSystem,line);
            }
        }
    }
    
    // printTree(fileSystem);

    // computeDim(fileSystem);
    // auto result = bfsSmall(fileSystem);

    // for(const auto& r: result)
    // {
    //     std::cout << r.second << " ";
    // }

    // std::cout << std::endl;

}

void cd(std::shared_ptr<Tree>& fileSystem, std::string dir)
{
    if(dir == "/")
    {
        fileSystem.get()->parent.lock() = nullptr;
    }
    else if(dir == "..") //Assuming we are not going to see cd /; cd ..
    {
        fileSystem = fileSystem.get()->parent.lock();
    }
    else
    {
        fileSystem = fileSystem.get()->sons[dir];
    }
}

void ls(std::shared_ptr<Tree>& fileSystem, std::string elemInDir)
{
    size_t start = 0;
    size_t npos = elemInDir.find(" ",start);
    std::string firstElem = elemInDir.substr(start,npos-start);
    start = npos+1;
    std::string secondElem = elemInDir.substr(start,elemInDir.find(" ",start)-start);

    if(firstElem == "dir")
    { 
        std::cout << "1: " << secondElem << std::endl;
        fileSystem.get()->sons.insert({secondElem,std::make_shared<Tree>()});
    }
    else // file dimension
    {
        std::cout << secondElem << std::endl;
        fileSystem.get()->sons.insert({secondElem,std::make_shared<Tree>(std::stoi(firstElem))});
    }
}

void computeDim(std::shared_ptr<Tree>& fileSystem)
{

    std::shared_ptr<Tree> dirPointer = fileSystem;

    baseComputeDim(dirPointer);

}

int baseComputeDim(std::shared_ptr<Tree>& fileSystem)
{

    if(fileSystem.get()->sons.empty())
    {
        return fileSystem.get()->_val;
    }

    for(auto& d: fileSystem.get()->sons)
    {
        if(d.second.get()->_val == 0) //If it still does not have a value sum its components
        {
            baseComputeDim(d.second);
        }
    }

    fileSystem.get()->_val = std::accumulate(fileSystem.get()->sons.begin(),
                                                fileSystem.get()->sons.end(),
                                                0,sumDir);

    return fileSystem.get()->_val;

}

int sumDir(int a, std::pair<std::string,std::shared_ptr<Tree>> b)
{
    return a + b.second.get()->_val;
};

std::map<std::shared_ptr<Tree>,int> bfsSmall(std::shared_ptr<Tree>& fileSystem)
{

    std::map<std::shared_ptr<Tree>,int> smallEnough;

    baseBfsSmall(fileSystem,smallEnough);

    return smallEnough;

}

void baseBfsSmall(std::shared_ptr<Tree>& fileSystem, std::map<std::shared_ptr<Tree>,int>& smallEnough)
{
    if(fileSystem.get()->sons.empty())
    {
        return;
    }
    if(fileSystem.get()->_val < 100000)
    {
        smallEnough.insert({fileSystem,fileSystem.get()->_val});
    }
    for(auto& d: fileSystem.get()->sons)
    {
        baseBfsSmall(d.second,smallEnough);
    }
}

void printTree(std::shared_ptr<Tree>& fileSystem)
{
    for(auto& d: fileSystem.get()->sons)
    {
        std::cout << 1 << d.first << std::endl;
        printTree(d.second);
    }
}