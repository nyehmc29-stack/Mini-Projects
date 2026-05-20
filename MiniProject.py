while True:
    print("=" * 30)
    print("Selamat datang di PPLG Topup")
    print("=" * 30)

    print("\nPilihan game :")
    print("1. Mobile Legends: Bang Bang")
    print("2. Free Fire")
    print("3. Roblox")
    pilihan_game = input("Pilih yang mana (1/2/3)? ").strip()

    if pilihan_game == '1':
        print("\nData Akun Mobile Legends: Bang Bang")
        id_akun = input("ID: ")
        server = input("Server: ")
    elif pilihan_game == '2':
        print("\nData Akun Free Fire")
        id_akun = input("ID: ")
    elif pilihan_game == '3':
        print("\nData Akun Roblox")
        username = input("Username: ")
    else:
        print("Pilihan tidak valid.")
        continue

    if pilihan_game == '3':  
        nominal_options = {
            '1': ("80 Robux", 15000),
            '2': ("400 Robux", 50000),
            '3': ("800 Robux", 80000),
            '4': ("1700 Robux", 150000),
            '5': ("4500 Robux", 350000),
            '6': ("10000 Robux", 700000),
        }
        mata_uang = "Robux"
    else:  
        nominal_options = {
            '1': ("20 Diamond", 15000),
            '2': ("80 Diamond", 50000),
            '3': ("100 Diamond", 80000),
            '4': ("250 Diamond", 100000),
            '5': ("500 Diamond", 200000),
            '6': ("750 Diamond", 350000),
            '7': ("900 Diamond", 600000),
            '8': ("1200 Diamond", 800000),
            '9': ("1500 Diamond", 950000),
            '10': ("2000 Diamond", 1000000)
        }
        mata_uang = "Diamond"

    print("\n==============================")
    print(f"         PILIH NOMINAL ({mata_uang})")
    print("==============================")
    for key in sorted(nominal_options.keys(), key=int):
        desc, price = nominal_options[key]
        print(f"{key}. {desc:<15} - Rp{price:,}")
    print("==============================")
    pilihan_nominal = input("Pilih nominal :").strip()
    if pilihan_nominal not in nominal_options:
        print("Pilihan nominal tidak valid.")
        continue

    desc, harga = nominal_options[pilihan_nominal]

    print("\nMetode Pembayaran:")
    print("1. Debit")
    print("2. E-Wallet")
    metode = input("Pilih metode (1/2): ").strip()

    if metode == '1':
        print("\n--- Debit ---")
        id_debit = input("ID Debit: ")
        pin_debit = input("PIN Debit: ")
        kode_promo = input("Kode promo (jika tidak ada ketik 'tidak'): ").strip()
    elif metode == '2':
        print("\nPilih E-Wallet:")
        print("1. Dana")
        print("2. ShopeePay")
        print("3. GoPay")
        pilih_wallet = input("Pilih E-Wallet yang mana (1/2/3)? ").strip()
        if pilih_wallet == '1':
            id_wallet = input("ID Dana: ")
            PIN_wallet = input("PIN Dana: ")
        elif pilih_wallet == '2':
            id_wallet = input("ID ShopeePay: ")
            PIN_wallet = input("PIN ShopeePay")
        elif pilih_wallet == '3':
            id_wallet = input("ID GoPay: ")
            PIN_wallet = input ("PIN GoPay: ")
        else:
            print("Pilihan tidak valid.")
            continue
        kode_promo = input("Kode promo (jika tidak ada ketik 'tidak'): ").strip()
    else:
        print("Metode tidak valid.")
        continue

    diskon = 0
    if kode_promo.upper() == "PPLG123":
        diskon = 0.10  
        potongan = int(harga * diskon)
        harga_diskon = harga - potongan
        print(f"\nKode promo 'PPLG123' berhasil digunakan! Diskon 10% (Rp{potongan:,})")
    else:
        harga_diskon = harga
        if kode_promo.lower() != 'tidak':
            print("\nKode promo tidak valid. Tidak ada diskon yang diterapkan.")

    print("\nKonfirmasi apakah data dan nominal sudah benar?")
    print("=====================================")
    if pilihan_game == '1':
        print("Game     : Mobile Legends: Bang Bang")
        print(f"ID       : {id_akun}")
        print(f"Server   : {server}")
    elif pilihan_game == '2':
        print("Game     : Free Fire")
        print(f"ID       : {id_akun}")
    elif pilihan_game == '3':
        print("Game     : Roblox")
        print(f"Username : {username}")
    print(f"Nominal  : {desc} (Rp{harga:,})")
    if diskon > 0:
        print(f"Diskon   : 10% (-Rp{potongan:,})")
    print(f"Total    : Rp{harga_diskon:,}")
    print("=====================================")

    konfirmasi = input("Ketik 'ya' untuk lanjut atau 'tidak' untuk batal: ").strip().lower()
    if konfirmasi == 'ya':
        print("\n======================")
        print(" PEMBAYARAN BERHASIL ")
        print("======================")
        print(f"Total dibayar: Rp{harga_diskon:,}")
    else:
        print("\nTransaksi dibatalkan.")

    ulang = input("\nApakah ingin kembali ke menu utama? (ya/tidak): ").strip().lower()
    if ulang != 'ya':
        print("\nTerima kasih telah menggunakan PPLG Topup!")
        break
