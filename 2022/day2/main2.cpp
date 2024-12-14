#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>

enum Action{rock,paper,scissors};

Action getAction(std::string aMove);
int getResult(std::string aResult);

int main()
{

    std::string line;
    int totalScore = 0;
    std::ifstream ifs("data.txt");

    std::map<Action,int> moveScore = {{Action::rock,1},{Action::paper,2},{Action::scissors,3}};
    std::vector<std::vector<int>> score = {{3,6,0},{0,3,6},{6,0,3}};
    std::vector<std::vector<Action>> movesToResult = {{scissors,rock,paper},{rock,paper,scissors},{paper,scissors,rock}};

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
            int result = getResult(line.substr(line.find(delimiter)+1,line.find(delimiter)+2));
            Action myMove = movesToResult[opponentMove][result];
            totalScore += score[opponentMove][myMove] + moveScore[myMove];
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

int getResult(std::string aResult)
{
    int result;

    if(aResult == "X")
        result = Action::rock;
    if(aResult == "Y")
        result = Action::paper;
    if(aResult == "Z")
        result = Action::scissors;

    return result;
}
