import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from skimage import io

image = io.imread(r"image.png")
gray_image = np.mean(image, axis=-1)

# dyskretna transformata Fouriera dla obrazu 2D
image_fft = fftpack.fft2(gray_image)

# Ustaw progi dla częstotliwości, które chcesz usunąć
cutoff_freq = 0.1  # Przykładowy próg, dostosuj go do własnych potrzeb
rows, cols = gray_image.shape
cutoff_row = int(rows * cutoff_freq)
cutoff_col = int(cols * cutoff_freq)

# Usuń wysokie częstotliwości, ustawiając je na zero
image_fft[:cutoff_row, :] = 0
image_fft[:, :cutoff_col] = 0
image_fft[-cutoff_row:, :] = 0
image_fft[:, -cutoff_col:] = 0

# Przeprowadź odwrotną transformatę Fouriera
denoised_image = np.abs(fftpack.ifft2(image_fft))

# Wyświetl oryginalny obraz i odszumiony obraz
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Oryginalny obraz szary')

plt.subplot(1, 2, 2)
plt.imshow(denoised_image, cmap='gray')
plt.title('Odszumiony obraz')

plt.show()