#include <iostream>
using namespace std;

int menu() {
	
	int seleccion;
	
	cout << "Seleccione: \n 1. Miles a Kilometers \n 2. Kilometers a Miles\n";
	cin >> seleccion;

	return seleccion;
}

int main(){
	
	int seleccion = menu();

	switch(seleccion){
		case 1 :
			cout << "Miles  Kilometers" << endl;

			for (int i = 1; i < 11; i++){
				float kilometers = i / 1.609;
				cout <<"  " << i << "   " << kilometers << endl;
			}
			break;
		case 2: 
			cout << "Kilometers  Miles" << endl;
			for (int i = 20; i < 65; i++){
				float Miles = i * 1.609;
				cout << "      " << i << "   " << Miles << endl;
			}
			break;
	}
}
