#!/usr/bin/python
import psycopg2
import time
import datetime
from library.spse import spse


if __name__ == '__main__':

    # # Bentuk Usaha
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel bentuk_usaha")
    spse("bentuk_usaha")


    # # Ijin Usaha
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel ijin_usaha")
    spse("ijin_usaha")


    # # Kabupaten
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel kabupaten")
    spse("kabupaten")


    # # Kontrak
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel kontrak")
    spse("kontrak")


    # # Pemilik
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel pemilik")
    spse("pemilik")


    # # Pengalaman
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel pengalaman")
    spse("pengalaman")
    

    # # Pengurus
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel pengurus")
    spse("pengurus")


    # # Peralatan
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel peralatan")
    spse("peralatan")


    # # Propinsi
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel propinsi")
    spse("propinsi")


    # # Rekanan
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel rekanan")
    spse("rekanan")


    # # Satuan Kerja
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel satuan_kerja")
    spse("satuan_kerja")


    # # Staf Ahli
    current_time = time.strftime('%Y-%m-%d %H-%M-%S')
    print("["+current_time+"] : Mengambil Data Tabel staf_ahli")
    spse("staf_ahli")