
#include <bits/stdc++.h>
using namespace std;

struct Point {
	int x, y;
};

int overlappingArea(Point l1, Point r1, Point l2, Point r2)
{

	int area1 = abs(l1.x - r1.x) * abs(l1.y - r1.y);
	int area2 = abs(l2.x - r2.x) * abs(l2.y - r2.y);
	int areaI = (min(r1.x, r2.x) - max(l1.x, l2.x)) * (min(r1.y, r2.y) - max(l1.y, l2.y));

	return (area1 + area2 - areaI);
}

int main()
{
	int n;
	cin>>n;
	int temp=n-1;
	while(temp--){
		Point l1,r1,l2,r2;
		cin>>l1.x>>l1.y>>r1.x>>r1.y;
		cin>>l2.x>>l2.y>>r2.x>>r2.y;	

		cout << overlappingArea(l1, r1, l2, r2);
	}
	return 0;
}

