#include <iostream>
#include <fstream>
#include <string>
#include <vector>

void isTreeVisible(std::vector<std::vector<std::pair<int,bool>>>& trees, int& maxHeight, size_t i, size_t j);

auto main() -> int
{
    std::ifstream ifs("data.dat");
    std::string line;
    std::vector<std::vector<std::pair<int,bool>>> trees; //height, isVisible

    if(ifs)
    {
        while(!ifs.eof())
        {
            std::getline(ifs,line);

            std::vector<std::pair<int,bool>> treeInLine;
            for(const auto c: line)
            {
                treeInLine.push_back({c-'0',false});
            }

            trees.push_back(treeInLine);
        }
    }

    const size_t n = trees.size(); //Using standard matrix notation n=number of rows, m=number of columns
    const size_t m = trees[0].size();

    //Skipping first last row, first last column
    for(auto& tree: trees[0])
        tree.second = true;
    for(auto& tree: trees.back())
        tree.second = true;
    for(auto& tree: trees)
    {
        tree[0].second = true;
        tree.back().second = true;
    }
    
    for(size_t i=1; i<n-1; ++i) //We skip the first and the last row
    {

        int maxHeight = trees[i][0].first;

        //Scan left to right
        for(size_t j=1; j<m; ++j)
        {
            isTreeVisible(trees,maxHeight,i,j);
        }

        maxHeight = trees[i][m-1].first;

        for(size_t j=m-1; j>0; --j)
        {
            isTreeVisible(trees,maxHeight,i,j);
        }
    }

    for(size_t j=1; j<m-1; ++j)
    {
        int maxHeight = trees[0][j].first;

        for(size_t i=1; i<n-1; ++i)
        {
            isTreeVisible(trees,maxHeight,i,j);
        }

        maxHeight = trees[n-1][j].first;

        for(size_t i=n-1; i>0; --i)
        {
            isTreeVisible(trees,maxHeight,i,j);
        }
    }

    int result = 0;

    for(const auto& treesLine: trees)
        for(const auto& tree: treesLine)
        {
            //std::cout << tree.first << " " << tree.second << std::endl;
            if(tree.second)
                result += 1;
        }

    std::cout << "result is: " << result << std::endl;

}



void isTreeVisible(std::vector<std::vector<std::pair<int,bool>>>& trees, int& maxHeight, size_t i, size_t j)
{
    auto& tree = trees[i][j];
    if(tree.first > maxHeight)
    {
        //std::cout << i << " " << j << std::endl;
        tree.second = true;
        maxHeight = tree.first;
    }
}