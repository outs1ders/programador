#include <iostream>
using namespace std;

int main(){
	float mount, rate, months, interest;
	cout << "Ingrese la cantidad que desea: " << endl;
	cin >> mount;

	cout << "Ingrese el porcentaje de interes: " << endl;
	cin >> rate;

	cout << "Ingrese el numero de meses: " << endl;
	cin >> months;
	
	rate = rate / 100;

	interest = rate / months;

	for ( int i = 1 ; i <= months ; i++ ){
		
		float value;
		
		if ( i == 1){
			value = mount * (1 + interest);
		}
		else {
			value = (mount + value) * (1 + interest); 
		}

		cout << "En el mes " << i << " el interes el valor es de: " << value << endl;

	}
}


