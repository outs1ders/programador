#include <iostream>
using namespace std;

int multiplos (int num1, int num2){
	if ( num1 % num2 == 0) {
		return num2;
	}
	else if (num2 % num1 == 0) {
		return num1;
	}
	else {
		return 0;
	}
}

int main (){
	int num1, num2;
	
	cout << "Ingrese el primer numero: "; cin >> num1;
	cout << "Ingrese el primer numero: "; cin >> num2;

	int resultado = multiplos(num1, num2);
	
	if (resultado != 0) {
		cout << "El numero " << resultado << " si es multiplo "; 	
	}else {
		cout << "No hay multiplos";
	}

}
