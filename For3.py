print("For 3")
 
MontoPrestamo = int(input("digita el monto del prestamo: "))
TasaInteres = float(input("digita la tasa del interes: "))
PlazoPrestamo = int(input("digita el plazo del prestamo: "))

TasaInteresMensual = TasaInteres / 12 / 100

CuotaMensual = (MontoPrestamo * TasaInteresMensual) / (1 - (1 + TasaInteresMensual) ** -PlazoPrestamo)

SaldoPendiente = MontoPrestamo

print(f"Mes   Cuota           	Interes           	Amortizacion")

for Mes in range(1, PlazoPrestamo + 1):
	IMensual = SaldoPendiente * TasaInteresMensual
	Amortizacion = CuotaMensual - IMensual
	SaldoPendiente -= Amortizacion

	print(f"{ Mes } 	{CuotaMensual}   {IMensual}	{Amortizacion}")



