#include "countingdays.h"
using namespace std;
int rHours = 0;
int rMinutes = 0;
int days = 1;
void lookAtClock(int hours, int minutes){
    if ((hours - rHours) < 0) days ++;
    if (hours - rHours == 0 && minutes - rMinutes < 0) days ++;
    rHours = hours;
    rMinutes = minutes;
}

int getDay(){
    return days;
}
