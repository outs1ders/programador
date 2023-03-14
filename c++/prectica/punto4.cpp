#include <iostream>
using namespace std;

int divisor(int num, int i){
	if (num % i == 0) {
		return i;
	}else {
		return 0;	
	}
	return 0;
}

int main(){
	int num;
	
	cout << "Ingrese el numero: "; cin >> num;

	for (int i = 1 ; i < 100; i++) {
	
		int divisores = divisor(num, i);

		if (divisores != 0) {
			cout << i <<" es un divisor de " << divisores << endl;
		}

		
	}

}
