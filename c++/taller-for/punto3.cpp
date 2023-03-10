#include <iostream>
using namespace std;

int menu() {
	
	int seleccion;
	
	cout << "Seleccione: \n 1. Divisible by 5 \n 2. Divisible by 6\n";
	cin >> seleccion;

	return seleccion;
}

int main(){	
	int seleccion = menu();

	switch(seleccion){
		case 1 :
			cout << "Divisible by 5" << endl;
			for (int i = 100; i < 1000; i++){
				if ( i % 5 == 0)
				cout << i << "  Is divisible by 5" << endl ;
			}
			break;
		case 2: 
			cout << "Divisible by 6" << endl;
			for (int i = 100; i < 1000; i++){
				if ( i % 6 == 0)
				cout << i << "  Is divisible by 5" << endl ;
			}
			break;
	}
}
