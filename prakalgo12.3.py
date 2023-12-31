# -*- coding: utf-8 -*-
"""prakalgo12.3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rdUXADJ0NuPo_vRkqyQ17Eyfd2lpMScE
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    jumlah_angka = int(input("Masukkan jumlah angka pada List: "))
    angka_list = []

    for i in range(1, jumlah_angka + 1):
        angka = int(input(f"Angka ke-{i}: "))
        angka_list.append(angka)

    print("List angka ->", angka_list)

    bubble_sort(angka_list)

    print("Hasil Bubble Sort ->", angka_list)

if __name__ == "__main__":
    main()