import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Parameter batas integral dan langkah interval
x_start = 0  # Batas awal
x_stop = -2  # Batas akhir
x_steps_interval = 0.01  # Langkah interval

# Membuat array data x dan menghitung nilai y
x_values = np.arange(x_start, x_stop, -x_steps_interval)  # Arah negatif
y_values = x_values**2 * np.cos(x_values) + 3 * np.sin(2 * x_values)

# Plot kurva fungsi
plt.plot(x_values, y_values, label=r'$e^{-x^2}$', color='blue')  # Memperbaiki label dengan LaTeX-style

# Isi area di bawah kurva sebagai hasil integral
plt.fill_between(x_values, y_values, color='skyblue', alpha=0.4)

# Mendefinisikan fungsi lambda untuk integrasi
integration_function = lambda x: x**2 * np.cos(x) + 3 * np.sin(2 * x)

# Menghitung integral menggunakan quad() (tanpa menampilkan error)
integral, _ = integrate.quad(integration_function, x_start, x_stop)

# Menampilkan hasil integrasi
print("Nilai Integral:", integral)

# Menambahkan label dan judul pada grafik
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'Plot of f(x) = x^2 * cos(x) + 3 * sin(2x)')
plt.legend()

# Menampilkan grafik
plt.show()
