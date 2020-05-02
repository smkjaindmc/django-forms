#include<iostream>
using namespace std;
class Float
{
    private:
    float a;
    public:
        void setdata(float b){
            a=b;
        }
    Float operator+ (Float c){
     Float temp;
     temp.a=a+c.a;
     return temp;
    }
    Float operator- (Float c){
     Float temp;
     temp.a=a-c.a;
     return temp;
    }
    Float operator* (Float c){
     Float temp;
     temp.a=a*c.a;
     return temp;
    }
    void print(){
        cout<<a<<endl;
    }
    };
    int main(){
      cout<<"enter two float number";
      float num1,num2;
      cin>>num1>>num2;
      Float c1,c3,c2;
      c1.setdata(num1);
      c2.setdata(num2);
      c3=c1+c2;
      c3.print();
      c3=c1-c2;
      c3.print();
      c3=c1*c2;
      c3.print();
      return 0;
    }
