#include <iostream>
#include <fstream>
#include <time.h>
using namespace std;

int main()
{
    int iSecret;
    srand(time(NULL));

    ofstream myfile;
    myfile.open("written.txt");
    int n = 1000000;
    for (int i = 1; i <= n; i++)
    {
        iSecret = rand() % n + 1;
        myfile << iSecret << " ";
    }
    myfile.close();
    return 0;
}