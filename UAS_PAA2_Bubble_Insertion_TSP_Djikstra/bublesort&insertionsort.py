import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.perf_counter()
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end_time = time.perf_counter()
    return arr, end_time - start_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.perf_counter()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.perf_counter()
    return arr, end_time - start_time

def print_iterations(arr, sort_name):
    print(f"Iterasi {sort_name} Sort:")
    print("--------------------------")
    print("\t V Iterasi Pertama:")
    for i in range(min(5, len(arr))):
        print(arr[i])
    print("--------------------------")
    print("\t V Iterasi Terakhir:")
    for i in range(max(len(arr) - 5, 0), len(arr)):
        print(arr[i])
    print()

def print_computation_time(time):
    print("--------------------------")
    print(f"Waktu Komputasi: {time:.6f} detik")

def print_before_after(arr, sorted_arr, sort_name):
    print(f"\t Sebelum {sort_name} Sort: {arr}")
    print(f"\t Sesudah {sort_name} Sort: {sorted_arr}")
    print()

def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    print("==============================================")
    print("JENIS ALGORITMA YANG DIGUNAKAN")
    print("\t 1. Bubble Sort")
    print("\t 2. Insertion Sort")
    choice = input("Pilih algoritma pengurutan (1 atau 2): ")

    if choice == "1":
        sorted_arr, time_taken = bubble_sort(arr.copy())
        print_iterations(sorted_arr, "Bubble")
        print_computation_time(time_taken)
        print_before_after(arr, sorted_arr, "Bubble")
    elif choice == "2":
        sorted_arr, time_taken = insertion_sort(arr.copy())
        print_iterations(sorted_arr, "Insertion")
        print_computation_time(time_taken)
        print_before_after(arr, sorted_arr, "Insertion")
    else:
        print("Pilihan tidak valid.")

    continue_choice = input("Apakah Anda ingin melanjutkan? (ya/tidak): ")
    if continue_choice.lower() == "ya":
        main()
    else:
        print("Program selesai.")

if __name__ == '__main__':
    main()
