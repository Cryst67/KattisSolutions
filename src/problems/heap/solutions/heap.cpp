#include "heap.h"
#include <vector>
using namespace std;
vector<int> heap;

int parent(int i){
    return (i-1)/2;
}

int left(int i){
    return 2*i + 1;
}

int right(int i){
    return 2*i + 2;
}

int getMax(){
    return heap[0];
}

int getSize(){
    return heap.size();
}

void heapUp(int i){
    while(i > 0 and heap[parent(i)] < heap[i]){
        swap(heap[parent(i)], heap[i]);
        i = parent(i);
    }
}

void heapDown(int i){
    int max_index = i;
    int l = left(i);
    if (l < heap.size() && heap[l] > heap[max_index]){
        max_index = l;
    }
    int rite = right(i);
    if(rite < heap.size() && heap[rite] > heap[max_index]){
        max_index = rite;
    }
    if(i !=  max_index){
        swap(heap[i], heap[max_index]);
        heapDown(max_index);
    }
}

void insert(int element){
    heap.push_back(element);
    heapUp(heap.size() - 1);
}

void removeMax(){
    int max_value = heap[0];
    heap[0] = heap[heap.size() - 1];
    heap.pop_back();
    heapDown(0);
}
