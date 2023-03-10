#include <iostream>
using namespace std;

int menor(int num1, int num2, int num3 ){
	if ( num2 > num1 & num3 > num1) {
		return num1;
	}
	if ( num1 > num2 & num3 > num2) {
		return num2;
	}
	else {
		return num3;
	}
}

int main(){
	int num1, num2, num3;

	cout << "Ingrese el numero 1: "; cin >> num1; 
	cout << "Ingrese el numero 2: "; cin >> num2; 
	cout << "Ingrese el numero 3: "; cin >> num3;

	cout << "El numero menor es: " << menor(num1, num2, num3);
}
