import csv
from datetime import datetime

class Node:
    def __init__(self, sku, nama_barang, harga_satuan, jumlah_stok):
        self.sku = sku
        self.nama_barang = nama_barang
        self.harga_satuan = harga_satuan
        self.jumlah_stok = jumlah_stok
        self.left = None
        self.right = None

# Class BST untuk menyimpan data barang
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Fungsi Insert Data Barang Ke Binary Search Tree
    def insert(self,  sku, nama_barang, harga_satuan, jumlah_stok):
        new_node = Node(sku, nama_barang, harga_satuan, jumlah_stok)
        temp = self.root

        if self.root is None:
            self.root = new_node
            self.simpanKeCsv('database_barang.csv')
            return True 

        while True:
            if bst.contains(sku):
                return False 

            elif sku < temp.sku:
                if temp.left is None:
                    temp.left = new_node
                    break

                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    break

                else:
                    temp = temp.right

        self.simpanKeCsv('database_barang.csv')
        return True

    # Fungsi untuk Mengecek Data di BST
    def contains(self, sku):
        temp = self.root
        while temp is not None:
            if sku < temp.sku:
                temp = temp.left
            elif sku > temp.sku:
                temp = temp.right
            else:
                return temp  
        return None    

    # Fungsi untuk mengupdar stok barang di BST   
    def restock(self, sku, jumlah_stok):
        temp = self.root
        while True :
            temp = self.root              
            if self.contains(sku) is not None :
                while temp is not None:
                    if sku == temp.sku:
                        temp.jumlah_stok += jumlah_stok
                        self.simpanKeCsv('database_barang.csv')
                        return 
                    
                    if sku < temp.sku:
                        if temp.left is None:
                            temp.left = jumlah_stok
                            return 
                        else:
                            temp = temp.left

                    else:
                        if temp.right is None:
                            temp.right = jumlah_stok
                            return 
                        else:
                            temp = temp.right
# Permanaff
    # Menampilkan Data 
    def tampil(self):
        data = []
        self.tampil_inorder(self.root, data)
        return data 

    def tampil_inorder(self, node,data):
        if node is not None:
            self.tampil_inorder(node.left, data)
            data.append([node.sku, node.nama_barang, node.harga_satuan, node.jumlah_stok])
            self.tampil_inorder(node.right, data)

    # Menghitung Total Stok Tersimpan
    def total_stok(self):
        if self.root is None:
            return 0
        stok = []
        current = self.root
        total_stok = 0
        while True:
            if current is not None:
                stok.append(current)
                current = current.left
            elif stok:
                current = stok.pop()
                total_stok += current.jumlah_stok
                current = current.right
            else:
                break
        return total_stok
    
    # Menghitung Stok Menipis 
    def tampil_stok_menipis(self):
        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            if node is not None:
                if node.jumlah_stok <= 5:
                    result.append(node)
                stack.append(node.left)
                stack.append(node.right)

        return result


    # Menyimpan Data Barang Ke CSv
    def simpanKeCsv(self, filename):
        data = []
        stack = []
        current = self.root

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                data.append([current.sku, current.nama_barang, current.harga_satuan, current.jumlah_stok])
                current = current.right
            else:
                break

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['no. sku', 'Nama Barang', 'Harga Satuan', 'Jumlah Stok'])
            writer.writerows(data)


    # Memuat Data dari CSV
    def muatDariCsv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Lewati baris header
            for row in reader:
                sku, nama_barang, harga_satuan, jumlah_stok = row
                self.insert(int(sku), str(nama_barang), int(harga_satuan), int(jumlah_stok))

# Class Transaksi untuk Menyimpan Data Transaksi 
class Transaksi:
    def __init__(self) :
        self.transaksi = []
        self.baca_dari_csv('data_transaksi.csv')

    # Fungsi Input Transaksi
    def input_transaksi(self, bst, nama_konsumen, sku, jumlah_beli):
        if not bst.contains(sku):
            return False
        else:
            barang = bst.contains(sku)
            subtotal = barang.harga_satuan * jumlah_beli
            if barang.jumlah_stok >= jumlah_beli:
                barang.jumlah_stok -= jumlah_beli
                waktu_transaksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.transaksi.append({
                    'nama konsumen': nama_konsumen,
                    'no. sku': sku,
                    'jumlah beli': jumlah_beli,
                    'subtotal': subtotal,
                    'waktu transaksi': waktu_transaksi
                })
                bst.simpanKeCsv('database_barang.csv')
                self.simpan_ke_csv('data_transaksi.csv')
                return True
            else:
                return False


    # Menghitung Stok Keluar
    def hitung_stok_keluar(self) :
        stok = 0
        for data in self.transaksi:
            stok += int(data['jumlah beli'])
        return stok
    
    # Menyimpan Data Transaksi Ke CSV
    def simpan_ke_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ['waktu transaksi','nama konsumen', 'no. sku', 'jumlah beli', 'subtotal']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerows(self.transaksi)
# Permanaff
    # Memuat Data Dari CSV
    def baca_dari_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.transaksi.append({
                    'waktu transaksi' : row['waktu transaksi'],
                    'nama konsumen': row['nama konsumen'],
                    'no. sku':int(row['no. sku']),
                    'jumlah beli': int(row['jumlah beli']),
                    'subtotal': int(row['subtotal'])
                })

    # Lihat Semua Data Transaksi
    def lihat_transaksi(self):
        return self.transaksi

    # Lihat Data Berdasarkan Subtotal
    def lihat_by_subtotal(self):
        data_urut = self.bubble_sort(self.transaksi)
        return data_urut
    
    # Melihat Data Berdasarkan Jumlah Beli
    def lihat_by_jmlBeli(self):
        data_urut = self.quicksort(self.transaksi, 'jumlah beli')
        return data_urut

    # Bubble Sort untuk mengurtukan data transaksi berdasarkan subtotal
    def bubble_sort(self, data):
        transaksi = data.copy()
        x = len(transaksi)
        for i in range (x-1):
            for j in range(0,x - i - 1):
                if transaksi[j]['subtotal'] < transaksi[j+1]['subtotal'] :
                    transaksi[j], transaksi[j+1] = transaksi[j+1], transaksi[j]
        return transaksi
    
    # Quicksort untuk mengurtukan data transaksi berdasarkan jumlah beli
    def quicksort(self, data, index):
        if len(data) <= 1:
            return data

        pivot = data[-1].get(index)
        smaller = []
        larger = []

        for i in range(len(data) - 1):
            if data[i][index] >= pivot:
                larger.append(data[i])
            else:
                smaller.append(data[i])

        return self.quicksort(larger, index) + [data[-1]] + self.quicksort(smaller, index)
                                                                          


# Create Objek 
bst = BinarySearchTree()
transaksi = Transaksi()
