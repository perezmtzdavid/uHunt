#include <iostream>
using namespace std;

int main() {
    int s,b,l,r; cin >> s >> b;    
    while(s != 0 && b != 0){
        int soldiers[s] = {0};
        for(int i = 0; i < b; i++){
            cin >> l >> r;
            for(int j = l-1; j < r; j++ ){
                soldiers[j] = s+1;
            }            
            int temp_l = s+1;
            int temp_r = s+1;            
            for(int j = l-2; j >= 0; j--){
                if(soldiers[j] != s+1){temp_l = j+1; break;}
            }
            for(int j = l-1; j < s; j++){
                if(soldiers[j] != s+1){
                    temp_r = j+1;
                    break;
                }
            }
            if(temp_l == s+1 && temp_r == s+1){cout<<"* *"<<endl;}
            else{
                if(temp_l == s+1){cout<<"* "<<temp_r<<endl;}
                if(temp_r == s+1){cout<<temp_l<<" *"<<endl;}
                if(temp_r != s+1 && temp_l != s+1){cout<<temp_l<<" "<<temp_r<<endl;}
            }
        }        
        cin >> s >> b;
        cout<<"-"<<endl;
    }
    return 0;
}