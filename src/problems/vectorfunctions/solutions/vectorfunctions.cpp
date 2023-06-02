#include "vectorfunctions.h"
#include <vector>
using namespace std;
void backwards(std::vector<int> &vec)
{
    vector<int> v;
    v.reserve(vec.size());
    for(int i = vec.size() - 1; i > -1; i--){
        v.push_back(vec[i]);
    }
    vec.clear();
    for(int i = 0; i < v.size(); i++){
        vec.push_back(v[i]);
    }
}

std::vector<int> everyOther(const std::vector<int> &vec)
{
    vector<int> v;
    for(int i = 0; i < vec.size(); i++){
        if(i % 2 == 0) v.push_back(vec[i]);
    }
    return v;
}

int smallest(const std::vector<int> &vec)
{
    int smallest = vec[0];
    for(auto i : vec){
        if(i < smallest){
            smallest = i;
        }
    }
    return smallest;
}

int sum(const std::vector<int> &vec)
{
    int sum = 0;
    for(auto i : vec){
        sum += i;
    }
    return sum;
}

int veryOdd(const std::vector<int> &suchVector)
{
    int count = 0;
    for(int i = 0; i < suchVector.size(); i++){
        if (i % 2 == 1 && suchVector[i] % 2 == 1) count ++;
    }
    return count;
}