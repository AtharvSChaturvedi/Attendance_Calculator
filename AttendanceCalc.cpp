#include<iostream>

using namespace std;

int main(){
    int days, present, days_required=0;
    float percentage_wanted, current_percentage;
    cout<<"Enter No. of Days: ";
    cin>>days;
    cout<<"Enter No. of Present: ";
    cin>>present;

    current_percentage=present/days;

    cout<<"Percentage wanted: ";
    cin>>percentage_wanted;

    if (percentage_wanted>=100){
        cout<<"INVALID!";
    }
    if (percentage_wanted<=current_percentage){
        cout<<"Already achieved";
    }
    else {
        while((present/(float)days)*100 < percentage_wanted){
            present++;
            days++;
            days_required++;
        }
    }

    cout<<"Number of classes required: "<<days_required;
}
