#include<iostream>
#include<iomanip>
using namespace std;
class student
{
	public: char name[10],prn[10];
	        int roll;
	
	public:void get();   
	       void display();
	               
};

void student::get()
{
	

		cout<<"enter name"<<endl;
		cin>>name;
		cout<<"enter prn"<<endl;
		cin>>prn;
		cout<<"enter roll num"<<endl;
		cin>>roll;
	

}
int main()
{
	student s[10];
	int i,n;
	cout<<"enter num of student"<<endl;
	cin>>n;
	
	for(i=0;i<n;i++)
	{
		s[i].get();
	}
    for(i=0;i<n;i++)
    {
    	s[i].display();
	}
	
}

void student::display()
{   
    
	cout<<"____________________________"<<endl;
	cout<<"name\t prn\t roll number"<<endl;
	cout<<name<<setw(10)<<prn<<setw(10)<<roll<<endl;
	
}