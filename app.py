import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

def larange_basis(x_values, i, x):
    n = len(x_values)
    basis = 1.0
    for j in range(n):
        if j != i:
            basis *= (x - x_values[j]) / (x_values[i] - x_values[j])
    return basis

def interpolasi_larange(x_values, y_values, x):
    n = len(x_values)
    y = 0
    langkah_perhitungan = []  # Menyimpan langkah-langkah perhitungan
    for i in range(n):
        basis = larange_basis(x_values, i, x)
        langkah_perhitungan.append(f"L_{i}({x}) = {basis:.4f}")  # Menyimpan langkah
        y += y_values[i] * basis
    return y, langkah_perhitungan

# Judul aplikasi
st.markdown("<h1>Interpolasi Langrange</h1>", unsafe_allow_html=True)

st.write("Interpolasi merupakan metode untuk menemukan titik data dalam rentang kumpulan titik data yang diketahui. Nah kalau di Matematika Interpolasi merupakan, teknik untuk memperkirakan nilai fungsi untuk setiap nilai antara dari variabel independen")
st.write("Berikut merupakan rumus Interpolasi Langrange")
url_gambar = "https://raw.githubusercontent.com/ain3ko/imgall/refs/heads/main/img-rumus-langrange.jpg"  # Contoh URL gambar
st.image(url_gambar, caption=" ", use_container_width=True)

st.markdown("<h3 style='color:orange;'>Simulasi</h3>", unsafe_allow_html=True)

# Input titik data
x_values = st.text_input('Masukkan nilai x (pisahkan dengan koma):', '0, 1, 2, 3')
y_values = st.text_input('Masukkan nilai y (pisahkan dengan koma):', '1, 2, 0, 5')

# Input nilai x yang ingin diperkirakan
x_target = st.number_input('Masukkan nilai x yang ingin diperkirakan:', min_value=-1e10, max_value=1e10, value=1.0)

# Mengonversi input menjadi array
try:
    x_values = np.array([float(x) for x in x_values.split(',')])
    y_values = np.array([float(y) for y in y_values.split(',')])

    if len(x_values) != len(y_values):
        st.error("Jumlah nilai x dan y harus sama.")
    else:
        # Rentang nilai x untuk interpolasi
        x_range = np.linspace(min(x_values), max(x_values), 100)
        y_interpolated = [interpolasi_larange(x_values, y_values, x)[0] for x in x_range]

        # Menghitung nilai y untuk x_target dan langkah-langkah perhitungan
        y_target, langkah_perhitungan = interpolasi_larange(x_values, y_values, x_target)

        # Visualisasi
        plt.figure(figsize=(10, 6))
        plt.plot(x_range, y_interpolated, label='Interpolasi Lagrange', color='blue')
        plt.scatter(x_values, y_values, color='red', label='Titik Data Asli')
        plt.scatter(x_target, y_target, color='green', label=f'Nilai Diperkirakan: ({x_target}, {y_target:.2f})', s=100)
        plt.title('Visualisasi Interpolasi Lagrange')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid()

        # Menampilkan grafik di Streamlit
        st.pyplot(plt)

        # Menampilkan langkah-langkah perhitungan
        st.write("**Langkah-langkah Perhitungan:**")
        for langkah in langkah_perhitungan:
            st.write(langkah)

        # Menampilkan hasil perkiraan
        st.write(f"Hasil interpolasi Lagrange untuk x = {x_target} adalah: {y_target:.4f}")

except ValueError:
    st.error("Masukkan nilai yang valid untuk x dan y.")