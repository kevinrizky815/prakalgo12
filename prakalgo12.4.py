# -*- coding: utf-8 -*-
"""prakalgo12.4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rdUXADJ0NuPo_vRkqyQ17Eyfd2lpMScE
"""

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    jumlah_angka = int(input("Masukkan jumlah angka pada List: "))
    angka_list = []

    for i in range(1, jumlah_angka + 1):
        angka = int(input(f"Angka ke-{i}: "))
        angka_list.append(angka)

    print("List angka > ", angka_list)

    selection_sort(angka_list)

    print("Hasil Selection Sort >", angka_list)

if __name__ == "__main__":
    main()