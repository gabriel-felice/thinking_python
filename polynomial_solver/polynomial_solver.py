# This program is intended to calculate roots of a polynomial equation. In actual stage, this program do not
# consider complex roots or derivatives that tends to zero.

while True:
    try:
        coefficients_number = int(input('What degree is the polynomial? '))
        break
    except ValueError:
        print("Type only positive intergers.")

coefficients_list = []
while len(coefficients_list) <= coefficients_number:
    while True:
        try:
            coefficients_list.append(float(input('Type coefficiets, starting by bigger degree: ')))
            break
        except ValueError:
            print('Type only numbers.')
coefficients_list = coefficients_list[::-1]

while True:
    try:
        iterations_number = int(input('How much iterations? '))
        break
    except ValueError:
        print("Type only positive intergers.")

while True:
        try:
            aprox= float(input('Type the start aproximation: '))
            break
        except ValueError:
            print('Type only numbers.')

derivative_list = []
for i, coef in enumerate(coefficients_list):
    derivative_list.append((coefficients_list[i])*i)

del derivative_list[0] #remove first zero from derivative list and align index and degrees.

print(f'Coefficients: {coefficients_list}')
print(f'Derivatives: {derivative_list}')

non_derivative = 0
derivative = 0

for _ in range(iterations_number):
    for i, name in enumerate(coefficients_list):
        if coefficients_list[0] == coefficients_list[i]: #coefficients_list = [minor degree, ... , bigger degree]
            non_derivative += coefficients_list[i]
        else:
            non_derivative += (aprox**i)*coefficients_list[i]
    for i, name in enumerate(derivative_list):
        derivative += (aprox**i)*derivative_list[i] #derivative_list = [minor degree, ... , bigger degree]
    aprox = aprox - (non_derivative/derivative)
    non_derivative = 0
    derivative = 0


print(f'If the polynomial has real root, this is the aproximation: {round(aprox, 6)}')







