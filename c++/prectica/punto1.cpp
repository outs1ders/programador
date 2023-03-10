#include <iostream>
using namespace std;

int valores(int num1, int num2){
	if (num1 > num2) {
		return num1;
	}else {
		return num2;
	}
}

int main(){
	int num1, num2;

	cout << "Ingrese el valor del numero 1: ";cin >> num1;
	cout << "Ingrese el valor del numero 2: ";cin >> num2;
	
	cout << "El mayor es: " << valores(num1, num2);
}
