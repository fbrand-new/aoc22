#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>

enum Action{rock,paper,scissors};

Action getAction(std::string aMove);

int main()
{

    std::string line;
    int totalScore = 0;
    std::ifstream ifs("data.txt");

    std::map<Action,int> moveScore = {{Action::rock,1},{Action::paper,2},{Action::scissors,3}};
    std::vector<std::vector<int>> score = {{3,6,0},{0,3,6},{6,0,3}};

    if(ifs)
    {
        while(!ifs.eof())
        {
            std::getline(ifs,line);
            //1. split the line based on space
            //According to stack overflow we should do the following
            // std::string s = "scott>=tiger";
            // std::string delimiter = ">=";
            // std::string token = s.substr(0, s.find(delimiter)); // token is "scott"

            std::string delimiter = " ";
            Action opponentMove = getAction(line.substr(0,line.find(delimiter)));
            Action myMove = getAction(line.substr(line.find(delimiter)+1,line.find(delimiter)+2));

            // std::cout << "line: " << line << std::endl;
            // std::cout << "opponentMove: " << opponentMove << std::endl;
            // std::cout << "myMove: " << myMove << std::endl;
            // std::cout << "delimiter: " << line.find(delimiter) << std::endl;
            // std::cout << "myMove field: " << line.substr(line.find(delimiter),line.find(delimiter)+1) << std::endl;
            totalScore += score[opponentMove][myMove] + moveScore[myMove];
            //std:: cout << score[opponentMove][myMove] + moveScore[myMove] << std::endl;
        }
    }

    std::cout << "Total score:"  << totalScore << std::endl;
}

Action getAction(std::string aMove) 
{
    Action a;

    if(aMove == "A" || aMove == "X")
        a = Action::rock;
    if(aMove == "B" || aMove == "Y")
        a = Action::paper;
    if(aMove == "C" || aMove == "Z")
        a = Action::scissors;

    return a;
}

