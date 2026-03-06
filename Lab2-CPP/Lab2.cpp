#include <iostream>
using namespace std;

void question1() {
    int num;
    cout << "Enter a positive integer greater than 9: ";
    cin >> num;

    int steps = 0;
    cout << num;

    while (num >= 10) {
        int sum = 0;
        int temp = num;

        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }

        cout << " → " << sum;
        num = sum;
        steps++;
    }

    cout << "\nFinal value: " << num << endl;
    cout << "Total steps: " << steps << endl;
}

void question2() {
    int n;
    cout << "Enter a number between 10 and 100: ";
    cin >> n;

    while (n < 10 || n > 100) {
        cout << "Invalid input. Enter a number between 10 and 100: ";
        cin >> n;
    }

    int fizz = 0, buzz = 0, fizzbuzz = 0;

    for (int i = 1; i <= n; i++) {

        if (i % 7 == 0) continue;

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz\n";
            fizzbuzz++;
        }
        else if (i % 3 == 0) {
            cout << "Fizz\n";
            fizz++;
        }
        else if (i % 5 == 0) {
            cout << "Buzz\n";
            buzz++;
        }
        else {
            cout << i << endl;
        }
    }

    cout << "--Summary--" << endl;
    cout << "Fizz count: " << fizz << endl;
    cout << "Buzz count: " << buzz << endl;
    cout << "FizzBuzz count: " << fizzbuzz << endl;
}

void question3() {
    int n;
    cout << "Enter a number between 3 and 9: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }

    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
}

int main() {

    question1();
    question2();
    question3();

    return 0;
}