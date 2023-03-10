#include <iostream>
using namespace std;

void kilogramsPounds(int kilogram){
	float pounds = kilogram/ 0.45359237;
	if (kilogram < 10){
		cout << endl << "    " << kilogram << "       " << pounds << endl ;
	}
	else if (kilogram >= 10 && kilogram < 100) {
		cout << endl << "    " << kilogram << "      " << pounds << endl ;
	}
	else if (kilogram >= 100) {
		cout << endl << "    " << kilogram << "     " << pounds << endl ;
	}
}




void PoundsKilograms(int pound){
	float kilogram = pound * 0.45359237;
	if (kilogram < 20){
		cout << endl << "    " << pound << "       " << kilogram << endl ;
	}
	else if (kilogram >= 20 && kilogram < 100) {
		cout << endl << "    " << pound << "      " << kilogram << endl ;
	}
	else if (kilogram >= 100) {
		cout << endl << "    " << pound << "     " << kilogram << endl ;
	}
}

int menu() {
	
	int seleccion;
	
	cout << "Seleccione: \n 1. kg a L \n 2. L a K \n";
	cin >> seleccion;

	return seleccion;
}

int main(){
	
	int seleccion = menu();

	switch(seleccion){
		case 1 :
			cout << "Kilograms  Pounds";

			for (int i = 1; i < 200; i++){
				kilogramsPounds(i);
			}
			break;
		case 2: 
			cout << "Pounds  Kilograms";

			for (int i = 20; i < 516; i++){
				PoundsKilograms(i);
			}
			break;
	}
}
