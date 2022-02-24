#include<stdio.h>
#include <stdlib.h>
#include <time.h>

int i, rn_ton , ton, rn_demand, demand, revenue;
float lp, salvage, dp, purchase_value_of_70_np = .33 * 70;

void rn_for_ton(int k){
    for(i = 0; i < k; i++){
        
        rn_ton = rand()%100;
        type_of_news_day();
    }
}

void type_of_news_day(){
    if(rn_ton < 36){
        ton = "good";
    }
    else if(rn_ton < 81){
        ton = "fair";
    }
    else if(rn_ton < 101){
        ton = "poor";
    }
    rn_for_demand();
}

void rn_for_demand(){
    rn_demand = rand()%100;
    _demand();
}

void _demand(){
    if(ton == "poor" & rn_demand < 45){
        demand = 40;
    }
    else if(ton == "poor" & rn_demand < 67){
        demand = 50;
    }
    else if(ton == "poor" & rn_demand < 83){
        demand = 60;
    }
    else if(ton == "poor" & rn_demand < 95){
        demand = 70;
    }
    else if(ton == "poor" & rn_demand < 101){
        demand = 80;
    }
    else if(ton == "fair" & rn_demand < 11){
        demand = 40;
    }
    else if(ton == "fair" & rn_demand < 29){
        demand = 50;
    }
    else if(ton == "fair" & rn_demand < 69){
        demand = 60;
    }
    else if(ton == "fair" & rn_demand < 89){
        demand = 70;
    }
    else if(ton == "fair" & rn_demand < 97){
        demand = 80;
    }
    else if(ton == "fair" & rn_demand < 101){
        demand = 90;
    }
    else if(ton == "good" & rn_demand < 4){
        demand = 40;
    }
    else if(ton == "good" & rn_demand < 9){
        demand = 50;
    }
    else if(ton == "good" & rn_demand < 24){
        demand = 60;
    }
    else if(ton == "good" & rn_demand < 44){
        demand = 70;
    }
    else if(ton == "good" & rn_demand < 79){
        demand = 80;
    }
    else if(ton == "good" & rn_demand < 94){
        demand = 90;
    }
    else if(ton == "good" & rn_demand < 101){
        demand = 100;
    }
    _revenue();
}

void _revenue(){
    revenue = demand * .5;
    _lost_profit();
}

void _lost_profit(){
    if(demand > 70){
        lp = (demand - 70) * .17;
    }
    else{
        lp = 0;
    }
    _salvage();
}

void _salvage(){
    if(demand < 70){
        salvage = (70 - demand) * .05;
    }
    else{
        salvage = 0;
    }
    _daily_profit();
}

void _daily_profit(){
    dp = revenue - purchase_value_of_70_np - lp + salvage;
    printf("%d\t   %d\t   %s\t    %d\t\t   %d\t   %d\t\t %.1f\t   %.1f\t\t       %.1f\t      %.1f\t\n", i+1, rn_ton, ton, rn_demand, demand, revenue, lp, salvage, dp, purchase_value_of_70_np);
}

int main(){
    printf("DAY\t Rn_TON\t   TON\t RN_DEMAND\t DEMAND\t REVENUE    LOST PROFIT\t SALVAGE\t DAILY PROFIT\t  Purchase Value of 70\t\n");
    srand(time(0));
    rn_for_ton(30);
    return 0;
}