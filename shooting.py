def bang_cuu_chuong():
    print("Bảng cửu chương:\n")
    for i in range(1, 10):  # Từ 1 đến 9
        print(f"Bảng nhân {i}:")
        for j in range(1, 11):  # Nhân từ 1 đến 10
            print(f"{i} x {j} = {i * j}")
        print()  # Dòng trống giữa các bảng

bang_cuu_chuong()