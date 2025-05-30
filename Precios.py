from decimal import Decimal, ROUND_HALF_UP
import tkinter as tk
from tkinter import ttk, messagebox

def calcular_volumen(ancho, largo, alto):
    return Decimal(ancho * largo * alto).quantize(Decimal('0.000'))

def calcular_precio_por_pieza(precio_mil, volumen):
    return (Decimal(precio_mil) * volumen / Decimal(1000)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

def calcular_precio_mil(precio_pieza, volumen):
    return (Decimal(precio_pieza) * Decimal(1000) / volumen).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

class ConvertidorPreciosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertidor de Precios Salamanca XR")

        self.crear_interfaz()

    def crear_interfaz(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack()

        tk.Label(frame, text="Paso 1: Dimensiones (pulgadas)").grid(row=0, column=0, columnspan=6, sticky="w")

        tk.Label(frame, text="Ancho:").grid(row=1, column=0)
        self.ancho_var = tk.DoubleVar(value=1)
        tk.Entry(frame, textvariable=self.ancho_var, width=5).grid(row=1, column=1)

        tk.Label(frame, text="Largo:").grid(row=1, column=2)
        self.largo_var = tk.DoubleVar(value=1)
        tk.Entry(frame, textvariable=self.largo_var, width=5).grid(row=1, column=3)

        tk.Label(frame, text="Alto:").grid(row=1, column=4)
        self.alto_var = tk.DoubleVar(value=1)
        tk.Entry(frame, textvariable=self.alto_var, width=5).grid(row=1, column=5)

        tk.Label(frame, text="Paso 2: Ingresar Precio").grid(row=2, column=0, columnspan=6, sticky="w")

        self.precio_tipo = tk.StringVar(value="mil")
        tk.Radiobutton(frame, text="$ por Mil > Pieza", variable=self.precio_tipo, value="mil").grid(row=3, column=0, columnspan=2, sticky="w")
        tk.Radiobutton(frame, text="$ por Pieza > Mil", variable=self.precio_tipo, value="pieza").grid(row=3, column=2, columnspan=2, sticky="w")

        tk.Label(frame, text="Precio:").grid(row=3, column=4)
        self.precio_var = tk.StringVar(value="0.00")
        tk.Entry(frame, textvariable=self.precio_var, width=10).grid(row=3, column=5)

        tk.Button(frame, text="Calcular", command=self.calcular).grid(row=4, column=0, columnspan=6, pady=10)

        self.resultado_label = tk.Label(frame, text="Resultado: ")
        self.resultado_label.grid(row=5, column=0, columnspan=6, sticky="w")

    def calcular(self):
        try:
            ancho = Decimal(self.ancho_var.get())
            largo = Decimal(self.largo_var.get())
            alto = Decimal(self.alto_var.get())
            volumen = calcular_volumen(ancho, largo, alto)

            precio = Decimal(self.precio_var.get())

            if self.precio_tipo.get() == "mil":
                precio_pieza = calcular_precio_por_pieza(precio, volumen)
                resultado_texto = f"Precio por pieza = ${precio_pieza}  | Volumen: {volumen} po³"
            else:
                precio_mil = calcular_precio_mil(precio, volumen)
                resultado_texto = f"Precio por mil = ${precio_mil}  | Volumen: {volumen} po³"

            self.resultado_label.config(text="Resultado: " + resultado_texto)

        except Exception as e:
            messagebox.showerror("Error", f"Error en los cálculos: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConvertidorPreciosApp(root)
    root.mainloop()
