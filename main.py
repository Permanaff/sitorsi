# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Nama    : Fajar Permana Putra
# NPM     : 5220511385
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk
from SDP_BST import *

class Sitorsi : 
    def __init__(self, window): 
        self.window = window
        self.window.title('Sistem Informasi Stok dan Transaksi')
        self.window.geometry('1366x768')
        self.window.state('zoomed')
        self.window.iconbitmap('images\\icon.ico')
        self.homePage()
        self.dataBarang = None
        self.dataTransaksi = None
        self.labelDatamasuk = None
        self.labelDatakeluar = None
        self.label_total_data = None
        self.label_data_transaksi= None
        self.label_penghasilan = None

# -=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-  Header -=-=-=-=-=-=-=-=-=-=-=-=- 
# -=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-

        self.header = Frame(self.window, bg='#25316D' )
        self.header.place(x=300, y=0, width=1240, height=60)

        self.title = Label(self.header, text='SISTEM INFORMASI STOK DAN TRANSAKSI',bg='#25316D',font=("Tahoma",14,"bold",), bd=0,cursor='hand2',  activebackground= '#25316D', fg='white')
        self.title.place(x=20, y=20)

        self.keluar_text = Button(self.window, text='Keluar', bg='#D00000', font=("",13,"bold"), bd=0, fg='white', cursor='hand2', activebackground='#AD0000', command=lambda: self.keluar())
        self.keluar_text.place(x=1400, y=15)

# -=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=- SIDEBAR -=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-

        self.sidebar = Frame(self.window, bg='#F3F3F3')
        self.sidebar.place(x=0, y=0, width=300, height=800)

        self.logoImage= Image.open('images\\logo.png')
        self.logoImage = self.logoImage.resize((300, 300))
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo,  bg='#F3F3F3')
        self.logo.image = photo
        self.logo.place(x=-10, y=-50)

        # Menampilkan Jam 
        self.clockImage= Image.open('images\\time.png')
        self.clockImageSize = self.clockImage.resize((20, 20))
        photo = ImageTk.PhotoImage(self.clockImageSize)
        self.timeLabel = Label(self.sidebar, image=photo, bg='#F3F3F3')
        self.timeLabel.image = photo
        self.timeLabel.place(x=87, y=172)
        # ---
        self.lblClock = Label(self.sidebar,font=("tahoma",12))
        self.lblClock.place(x=110, y=172)

        # Menampilkan Tanggal
        self.dateImage= Image.open('images\\date.png')
        self.dateImageSize = self.dateImage.resize((20, 20))
        photo = ImageTk.PhotoImage(self.dateImageSize)
        self.dateLabel = Label(self.sidebar, image=photo)
        self.dateLabel.image = photo
        self.dateLabel.place(x=75, y=197)
        
        self.lblDate = Label(self.sidebar, font=("tahoma", 12), bg='#F3F3F3')
        self.lblDate.place(x=100, y=195)

        # Menampilkan Menu Home
        self.homeInd = Label(self.sidebar, text='',bg='#F3F3F3')
        self.homeInd.place(x=0, y=232, width=300, height=34)
        self.home = Button(self.sidebar, text='Home', bg='#F3F3F3',font=("tahoma",13,"bold"), bd=0,  activebackground= '#F3F3F3', command=lambda: self.indikator(self.homeInd, self.home,self.homePage, self.home_page_data))
        self.home.place(x=60, y=232)        

        # Menampilkan Menu Kelola Barang
        self.kelolaBarang = Label(self.sidebar, text='Kelola Barang', bg='#F3F3F3',font=("tahoma",13,"bold"), bd=0,  activebackground= '#F3F3F3')
        self.kelolaBarang.place(x=60, y=267)

        # Kelola Barang
            # Indikator Input Barang
        self.inputBarangInd = Label(self.sidebar, text='',bg='#F3F3F3')
        self.inputBarangInd.place(x=0, y=297, width=300, height=30)
            #  Menu Kelola Barang
        self.inputBarang = Button(self.sidebar,text='Input Barang', bg='#F3F3F3',font=("tahoma",13), bd=0, cursor='hand2', activebackground= '#E6E6E6', command=lambda:self.indikator(self.inputBarangInd,self.inputBarang, self.inputBarangPage,  self.tabelBarang))
        self.inputBarang.place(x=80, y=297)

        # Menu Restok Barang
            # Indikator Restok Barang
        self.restokBarangInd = Label(self.sidebar, text='',bg='#F3F3F3')
        self.restokBarangInd.place(x=0, y=327, width=300, height=32)
            # Menu Restok
        self.restokBarang = Button(self.sidebar,text='Restok Barang', bg='#F3F3F3',font=("tahoma",13), bd=0, cursor='hand2', activebackground= '#E6E6E6', command=lambda: self.indikator(self.restokBarangInd, self.restokBarang, self.restokPage, self.tabelBarang))
        self.restokBarang.place(x=80, y=327)
        
        # Label Kelola Transaksi
        self.kelolaTransaksi = Label(self.sidebar, text='Kelola Transaksi', bg='#F3F3F3',font=("tahoma",13,"bold"), bd=0,  activebackground= '#F3F3F3')
        self.kelolaTransaksi.place(x=60, y=370)

        # Input Transaksi
            # Indikator Input Transaksi
        self.inputTransaksiInd = Label(self.sidebar, text='',bg='#F3F3F3')
        self.inputTransaksiInd.place(x=0, y=400, width=300, height=30)
            # Menu Input Transaksi
        self.inputTransaksi = Button(self.sidebar,text='Input Transaksi Baru', bg='#F3F3F3',font=("tahoma",13), bd=0, cursor='hand2', activebackground= '#E6E6E6', command=lambda: self.indikator(self.inputTransaksiInd, self.inputTransaksi, self.transaksiPage, self.tabelBarang))
        self.inputTransaksi.place(x=80, y=400)

        # Tampil Data
            # Indikator Tampil Data
        self.tampilDataInd = Label(self.sidebar, text='',bg='#F3F3F3')
        self.tampilDataInd.place(x=0, y=430, width=300, height=32)
            # Menu Tampil Data
        self.tampilData = Button(self.sidebar,text='Data Transaksi', bg='#F3F3F3',font=("tahoma",13), bd=0, cursor='hand2', activebackground= '#E6E6E6',command=lambda: self.indikator(self.tampilDataInd, self.tampilData, self.tampilDataPage, self.tabelTransaksi ))
        self.tampilData.place(x=80, y=430)
        

# -=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=- BODY -=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-

    def homePage(self):

        # Background Halaman Home
        self.beranda = Frame(self.window, bg='white')
        self.beranda.place(x=300, y=60, width=1240, height=708)

        # Menampilkan Barang Masuk
        self.barangMasuk = Canvas(self.beranda, bg='#F8F4F4', bd=0, width=270, height=170)
        self.barangMasuk.grid(row=0, column=0, padx=15, pady=20)
        self.masukImage = Image.open('images\\in.png').resize((60, 60))
        photo = ImageTk.PhotoImage(self.masukImage)
        self.masukLabel = Label(self.barangMasuk, image=photo, bg='#F8F4F4')
        self.masukLabel.image = photo
        self.masukLabel.place(x=5, y=35)
        self.labelmasuk = Label(self.barangMasuk, text="Jumlah Barang Masuk", font=("tahoma",13, 'bold'), anchor=W, bg='#F8F4F4', fg='#25316D')
        self.labelmasuk.place(x=15, y=100)
        self.labelDatamasuk = Label(self.barangMasuk, text="0", font=("tahoma",14), anchor=W, bg='#F8F4F4')
        self.labelDatamasuk.place(x=15, y=125)
        self.labelDatamasuk = self.labelDatamasuk
        

        # Menampilkan Jumlah Barang Keluar
        self.barangKeluar = Canvas(self.beranda, bg='#F8F4F4', bd=0, width=270, height=170)
        self.barangKeluar.grid(row=0, column=1, padx=15)
        keluarImage = Image.open('images\\out.png').resize((60, 60))
        photo = ImageTk.PhotoImage(keluarImage)
        keluarLabel = Label(self.barangKeluar, image=photo, bg='#F8F4F4')
        keluarLabel.image = photo
        keluarLabel.place(x=5, y=35)
        labelkeluar = Label(self.barangKeluar, text="Jumlah Barang Keluar", font=("tahoma",13, 'bold'), anchor=W, bg='#F8F4F4', fg='#25316D')
        labelkeluar.place(x=15, y=100)
        self.labelDatakeluar = Label(self.barangKeluar, text="0", font=("tahoma",14), anchor=W, bg='#F8F4F4')
        self.labelDatakeluar.place(x=15, y=125)

        # Menampilkan Total Stok Barang
        self.totalBarang = Canvas(self.beranda, bg='#F8F4F4', bd=0, width=270, height=170)
        self.totalBarang.grid(row=0, column=2, padx=15)
        barang_image = Image.open('images\\gudang.png').resize((60, 60))
        photo = ImageTk.PhotoImage(barang_image)
        total_barang_label = Label(self.totalBarang, image=photo, bg='#F8F4F4')
        total_barang_label.image = photo
        total_barang_label.place(x=5, y=35)
        label_total_barang = Label(self.totalBarang, text="Total Stok Barang", font=("tahoma", 13, 'bold'), anchor=W, bg='#F8F4F4', fg='#25316D')
        label_total_barang.place(x=15, y=100)
        self.label_total_data = Label(self.totalBarang, text="0", font=("tahoma", 14), anchor=W, bg='#F8F4F4')
        self.label_total_data.place(x=15, y=125)

        # Menampilkan Jumlah Transaksi
        self.totalTransaksi = Canvas(self.beranda, bg='#F8F4F4', bd=0, width=270, height=170)
        self.totalTransaksi.grid(row=1, column=3, padx=15, pady=20)
        transaksi_image = Image.open('images\\transaksi.png').resize((60, 60))
        photo = ImageTk.PhotoImage(transaksi_image)
        transaksi_label = Label(self.totalTransaksi, image=photo, bg='#F8F4F4')
        transaksi_label.image = photo
        transaksi_label.place(x=5, y=35)
        label_transaksi = Label(self.totalTransaksi, text="Jumlah Transaksi", font=("tahoma", 13, 'bold'), anchor=W, bg='#F8F4F4', fg='#25316D')
        label_transaksi.place(x=15, y=100)
        self.label_data_transaksi = Label(self.totalTransaksi, text="0", font=("tahoma", 14), anchor=W, bg='#F8F4F4')
        self.label_data_transaksi.place(x=15, y=125)
        self.label_data_transaksi = self.label_data_transaksi
        
        # Menampilkan Total Keuntungan
        self.Penghasilan = Canvas(self.beranda, bg='#F8F4F4', bd=0, width=270, height=170)
        self.Penghasilan.grid(row=2, column=3, padx=15, pady=20)
        penghasilan_image = Image.open('images\\dollar.png').resize((60, 60))
        photo = ImageTk.PhotoImage(penghasilan_image)
        penghasilan = Label(self.Penghasilan, image=photo, bg='#F8F4F4')
        penghasilan.image = photo
        penghasilan.place(x=5, y=35)
        labelHasil = Label(self.Penghasilan, text="Total Keuntungan", font=("tahoma", 13, 'bold'), anchor=W, bg='#F8F4F4', fg='#25316D')
        labelHasil.place(x=15, y=100)
        self.label_penghasilan = Label(self.Penghasilan, text="0", font=("tahoma", 14), anchor=W, bg='#F8F4F4')
        self.label_penghasilan.place(x=15, y=125)
        self.label_penghasilan = self.label_penghasilan

        labelTabel = Label(self.beranda,text="Daftar Stok Menipis", font=("tahoma", 13, 'bold'), anchor=W, bg='#ffffff', fg='#25316D')
        labelTabel.place(x=30, y=210)

        # Menampilkan Data Barang Out Of Stock
        style = ttk.Style()
        style.theme_use('clam')
        self.tabelMenipis = ttk.Treeview(self.beranda,height=20)
        self.tabelMenipis['columns'] = ('sku', 'nama', 'harga', 'jumlah')
        self.tabelMenipis.column('#0', width=0, stretch=NO)
        self.tabelMenipis.column('sku', anchor=CENTER, width=100)
        self.tabelMenipis.column('nama', anchor=W, width=300)
        self.tabelMenipis.column('harga', anchor=W, width=220)
        self.tabelMenipis.column('jumlah', anchor=W, width=220)
        #  Heading tabel
        self.tabelMenipis.heading('sku', text='No. SKU', anchor=CENTER)
        self.tabelMenipis.heading('nama', text='Nama Barang', anchor=W)
        self.tabelMenipis.heading('harga', text='Harga Satuan', anchor=W)
        self.tabelMenipis.heading('jumlah', text='Jumlah Stok', anchor=W)            
        self.tabelMenipis.place(x=30, y=240)

        self.home_page_data()


    def inputBarangPage(self):
        # Background Halamn Input Barang
        self.ibpFrame = Frame(self.window, bg='white')
        self.ibpFrame.place(x=300, y=60, width=1240, height=708)

        # Tulisan Input Barang
        self.title = Label(self.ibpFrame, text='INPUT DATA BARANG', fg='#0E0E0E',font=("tahoma",14, 'bold'), bg='#ffffff')
        self.title.place(x=20, y=20)
        self.labelTabel = Label(self.ibpFrame, text='Daftar Barang', fg='#0E0E0E',font=("tahoma",12, 'bold'), bg='#ffffff' )
        self.labelTabel.place(x=700, y=70)        

        # Entry No. SKU
        self.labelSKU = Label(self.ibpFrame, text='No. SKU', fg='#0E0E0E',font=("tahoma",10), bg='#ffffff' )
        self.labelSKU.place(x=20, y=100)
        self.sku = Entry(self.ibpFrame,font=("tahoma",14) )
        self.sku.place(x=20, y=125) 
        
        # Entry Nama Barang
        self.labelNama = Label(self.ibpFrame, text='Nama Barang', fg='#0E0E0E',font=("tahoma",10), bg='#ffffff' )
        self.labelNama.place(x=300, y=100)
        self.namaBarang = Entry(self.ibpFrame, font=("tahoma",14) )
        self.namaBarang.place(x=300, y=125)

        # Entry Harga Satuan
        self.labelHarga= Label(self.ibpFrame, text='Harga Satuan', fg='#0E0E0E',font=("tahoma",10), bg='#ffffff' )
        self.labelHarga.place(x=20, y=200)
        self.hargaSatuan = Entry(self.ibpFrame, font=("tahoma",14) )
        self.hargaSatuan.place(x=20, y=225)

        # Entry Stok
        self.labelStok = Label(self.ibpFrame, text='Jumlah Stok', fg='#0E0E0E',font=("tahoma",10), bg='#ffffff' )
        self.labelStok.place(x=300, y=200)
        self.stokBarang = Entry(self.ibpFrame, font=("tahoma",14) )
        self.stokBarang.place(x=300, y=225)

        self.simpan = Button(self.ibpFrame,text='Simpan' ,font=("tahoma",14), bg='#25316D', activebackground='#0B1339',fg='white',command= self.getInputBarang)
        self.simpan.place(x=225, y=300) 

        # Menampilkan Tabel Data Barang 
        self.tabel = ttk.Treeview(self.ibpFrame, height=25)
        self.tabel['columns'] = ('sku', 'nama', 'harga', 'jumlah')
        self.tabel.column('#0', width=0, stretch=NO)
        self.tabel.column('sku', anchor=CENTER, width=100)
        self.tabel.column('nama', anchor=W, width=140)
        self.tabel.column('harga', anchor=CENTER, width=120)
        self.tabel.column('jumlah', anchor=CENTER, width=100)
        #  Heading tabel
        self.tabel.heading('sku', text='No. SKU', anchor=CENTER)
        self.tabel.heading('nama', text='Nama Barang', anchor=W)
        self.tabel.heading('harga', text='Harga Satuan', anchor=CENTER)
        self.tabel.heading('jumlah', text='Jumlah Stok', anchor=CENTER)            
        self.tabel.place(x=700, y=100)



    def restokPage(self):
        # Background Halaman Restok
        self.restokFrame = Frame(self.window, bg='white')
        self.restokFrame.place(x=300, y=60, width=1240, height=708)

        # Tulisan Restok Barang
        self.title = Label(self.restokFrame, text='RESTOK BARANG', fg='#0E0E0E',font=("tahoma",14, 'bold'), bg='#ffffff')
        self.title.place(x=20, y=20)
        self.labelTabel = Label(self.restokFrame, text='Daftar Barang', fg='#0E0E0E',font=("tahoma",12, 'bold'), bg='#ffffff' )
        self.labelTabel.place(x=700, y=70)

        # Entry No. SKU
        self.labelSKU = Label(self.restokFrame, text='No. SKU', fg='#0E0E0E',font=("tahoma",10), bg='#ffffff' )
        self.labelSKU.place(x=20, y=100)
        self.sku = Entry(self.restokFrame,font=("tahoma",14) )
        self.sku.place(x=20, y=125) 
        
        # Entry Nama Barang
        self.labelStok = Label(self.restokFrame, text='Jumlah Stok', fg='#0E0E0E',font=("tahoma",10), bg='#ffffff' )
        self.labelStok.place(x=300, y=100)
        self.stokBarang = Entry(self.restokFrame, font=("tahoma",14) )
        self.stokBarang.place(x=300, y=125)

        # Tombol Simpan 
        self.simpan = Button(self.restokFrame,text='Simpan' ,font=("tahoma",14), bg='#25316D', activebackground='#0B1339',fg='white',command= self.getRestokBarang)
        self.simpan.place(x=225, y=200) 

        # Menampilkan Tabel Data Barang 
        self.tabel = ttk.Treeview(self.restokFrame, height=25)
        self.tabel['columns'] = ('sku', 'nama', 'harga', 'jumlah')
        self.tabel.column('#0', width=0, stretch=NO)
        self.tabel.column('sku', anchor=CENTER, width=100)
        self.tabel.column('nama', anchor=W, width=140)
        self.tabel.column('harga', anchor=CENTER, width=120)
        self.tabel.column('jumlah', anchor=CENTER, width=100)
        #  Heading tabel
        self.tabel.heading('sku', text='No. SKU', anchor=CENTER)
        self.tabel.heading('nama', text='Nama Barang', anchor=W)
        self.tabel.heading('harga', text='Harga Satuan', anchor=CENTER)
        self.tabel.heading('jumlah', text='Jumlah Stok', anchor=CENTER)            
        self.tabel.place(x=700, y=100)



    def transaksiPage(self):
        # Backgourund Halaman Transaksi
        self.transaksiFrame = Frame(self.window, bg='white')
        self.transaksiFrame.place(x=300, y=60, width=1240, height=708)

        # Teks Halaman Transaksi
        self.title = Label(self.transaksiFrame, text='INPUT TRANSAKSI', fg='#0E0E0E',font=("tahoma",14, 'bold'), bg='#ffffff')
        self.title.place(x=20, y=20)
        self.labelTabel = Label(self.transaksiFrame, text='Daftar Barang', fg='#0E0E0E',font=("tahoma",12, 'bold'), bg='#ffffff' )
        self.labelTabel.place(x=700, y=70)

        # Entry/Input Nama Barang
        self.nama = Label(self.transaksiFrame, text='Nama Konsumen', fg='#0E0E0E',font=("tahoma",10), bg='#ffffff' )
        self.nama.place(x=20, y=100)
        self.namaKonsumen = Entry(self.transaksiFrame, font=("tahoma",14) )
        self.namaKonsumen.place(x=20, y=125) 

        # Entry/Input No. SKU 
        self.labelSKU = Label(self.transaksiFrame, text='No. SKU', fg='#0E0E0E',font=("tahoma",10), bg='#ffffff' )
        self.labelSKU.place(x=300, y=100)
        self.sku = Entry(self.transaksiFrame,font=("tahoma",14) )
        self.sku.place(x=300, y=125)
        
        # Entry/Input Jumlah Beli
        self.labelJmlBeli = Label(self.transaksiFrame, text='Jumlah Beli', fg='#0E0E0E',font=("tahoma",10), bg='#ffffff' )
        self.labelJmlBeli.place(x=20, y=200)
        self.jmlBeli = Entry(self.transaksiFrame,font=("tahoma",14) )
        self.jmlBeli.place(x=20, y=225) 

        # Tombol Simpan
        self.simpan = Button(self.transaksiFrame,text='Simpan' ,font=("tahoma",14), bg='#25316D', activebackground='#0B1339',fg='white',command= self.getInputTransaksi)
        self.simpan.place(x=225, y=300) 

        # Menampilkan Tabel Data Barang
        self.tabel = ttk.Treeview(self.transaksiFrame, height=25)
        self.tabel['columns'] = ('sku', 'nama', 'harga', 'jumlah')
        self.tabel.column('#0', width=0, stretch=NO)
        self.tabel.column('sku', anchor=CENTER, width=100)
        self.tabel.column('nama', anchor=W, width=140)
        self.tabel.column('harga', anchor=CENTER, width=120)
        self.tabel.column('jumlah', anchor=CENTER, width=100)
        #  Heading tabel
        self.tabel.heading('sku', text='No. SKU', anchor=CENTER)
        self.tabel.heading('nama', text='Nama Barang', anchor=W)
        self.tabel.heading('harga', text='Harga Satuan', anchor=CENTER)
        self.tabel.heading('jumlah', text='Jumlah Stok', anchor=CENTER)            
        self.tabel.place(x=700, y=100)



    def tampilDataPage(self):
        # Backgourd Halaman Daftar Transaksi
        self.dataFrame = Frame(self.window, bg='white')
        self.dataFrame.place(x=300, y=60, width=1240, height=708)
        
        # Tulisan Daftar Transaksi
        self.title = Label(self.dataFrame, text='DAFTAR TRANSAKSI', fg='#0E0E0E',font=("tahoma",14, 'bold'), bg='#ffffff', bd=0)
        self.title.place(x=20, y=20)

        # Button Show All 
        self.all = Button(self.dataFrame, text='All',fg='white',font=("tahoma",10), bg='#25316D', bd=0, command= self.tabelTransaksi)
        self.all.place(x=20, y=60, width=90)

        # Button untuk menampilkan daftar transaksi berdasarkan subtotal
        self.bySubtotal = Button(self.dataFrame, text='By Subtotal',fg='white',font=("tahoma",10), bg='#25316D', bd=0, command= self.tabel_transaksi_by_subtotal)
        self.bySubtotal.place(x=120, y=60, width=90)

        # Button Untuk menampilkan daftar transaksi berdasarkan jumlah beli
        self.byjmlBeli = Button(self.dataFrame, text='By Jumlah Beli',fg='white',font=("tahoma",10), bg='#25316D', bd=0, command= self.tabel_transaksi_by_jmlBeli)
        self.byjmlBeli.place(x=220, y=60, width=90)

        # Menampilkan Tabel Daftar Transaksi
        self.tabel_transaksi = ttk.Treeview(self.dataFrame, height=25)
        self.tabel_transaksi['columns'] = ( 'tanggal', 'nama','sku', 'harga', 'jumlah')
        self.tabel_transaksi.column('#0', width=0, stretch=NO)
        self.tabel_transaksi.column('tanggal', anchor=CENTER, width=150)
        self.tabel_transaksi.column('nama', anchor=W, width=250)
        self.tabel_transaksi.column('sku', anchor=CENTER, width=100)
        self.tabel_transaksi.column('harga', anchor=CENTER, width=150)
        self.tabel_transaksi.column('jumlah', anchor=CENTER, width=150)
        #  Heading tabel
        self.tabel_transaksi.heading('tanggal', text='Tanggal', anchor=CENTER)
        self.tabel_transaksi.heading('nama', text='Nama Konsumen', anchor=W)
        self.tabel_transaksi.heading('sku', text='No. SKU Dibeli', anchor=CENTER)
        self.tabel_transaksi.heading('harga', text='Jumlah Beli', anchor=CENTER)
        self.tabel_transaksi.heading('jumlah', text='Subtotal', anchor=CENTER)            
        self.tabel_transaksi.place(x=20, y=100)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# -=-=-=-=-=-=-=-=-=-  FUNGSI-FUNGSI -=-=-=-=-=-=-=-=-=--=-=-
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    # Fungsi Untuk menampilkan data pada halaman home
    def home_page_data(self):
        # Menampilkan Jumlah Data Barang Masuk
        total_barang_masuk = int(bst.total_stok()+transaksi.hitung_stok_keluar())
        self.labelDatamasuk.config(text=str(total_barang_masuk))

        # Menampilkan Jumlah Total Barang/Stok 
        label_total_data = bst.total_stok()
        self.label_total_data.config(text=str(label_total_data))

        # Menampilkan Jumlah Data Barang Keluar 
        total_barang_keluar = transaksi.hitung_stok_keluar()
        self.labelDatakeluar.config(text=str(total_barang_keluar))

        # Menampilkan Jumlah Daftar Transaksi 
        jumlah_transaksi = len(transaksi.lihat_transaksi())
        self.label_data_transaksi.config(text=str(jumlah_transaksi))

        #  Menampilakn Jumlah Total Penghasilan 
        data = transaksi.lihat_transaksi()
        totalPenghasilan = 0 
        for hasil in data:
            totalPenghasilan += int(hasil['subtotal'])
        self.label_penghasilan.config(text=str(totalPenghasilan))

        # Menampilkan Tabel Daftar Barang stok menipis/habis
        self.stok_menipis()

    # Menampilkan Barang dengan Stok Menipis/Habis
    def stok_menipis(self):
        self.tabelMenipis.delete(*self.tabelMenipis.get_children())

        data_list = bst.tampil_stok_menipis()
        for data in data_list:
            self.tabelMenipis.insert(parent='', index='end', values=(data.sku, data.nama_barang, data.harga_satuan, data.jumlah_stok))

    # Fungsi Indikator Menu 
    def indikator(self,label, menu, page, tabelData) :
        self.hideIndikatorMenu()
        self.hideIndikator()
        menu.config(bg='#E6E6E6')
        label.config(bg='#E6E6E6')
        page()
        tabelData()
        
    # Fungsi Hide Indikator Halaman
    def hideIndikator(self):
        self.homeInd.config(bg='#F3F3F3')
        self.inputBarangInd.config(bg='#F3F3F3')
        self.restokBarangInd.config(bg='#F3F3F3')
        self.inputTransaksiInd.config(bg='#F3F3F3')
        self.tampilDataInd.config(bg='#F3F3F3')
    # Fungsi Hide Indikator Halaman
    def hideIndikatorMenu(self):
        self.home.config(bg='#F3F3F3')
        self.inputBarang.config(bg='#F3F3F3')
        self.restokBarang.config(bg='#F3F3F3')
        self.inputTransaksi.config(bg='#F3F3F3')
        self.tampilData.config(bg='#F3F3F3')
    

    # Fungsi Close 
    def keluar(self) :
        self.window.quit()

    # Fungsi Jam 
    def time(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        current_date = datetime.now().strftime('%d-%m-%Y')
        self.lblClock.config(text=current_time)
        self.lblDate.config(text=current_date)
        self.lblClock.after(1000, self.time)

    # -=-=-=-=-=-=-=-=-=-=-=-=-
    # -=-=-=- GET DATA -=-=-=- 
    # -=-=-=-=-=-=-=-=-=-=-=-=-

    # Fungsi Get Input Data Barang
    def getInputBarang(self):
        sku = self.sku.get()
        namaBarang = self.namaBarang.get()
        harga = self.hargaSatuan.get()
        stok = self.stokBarang.get()

        if sku == '' or namaBarang == '' or harga == '' or stok == '':
            return False

        try:
            sku = int(sku)
            harga = int(harga)
            stok = int(stok)

            if len(str(sku)) != 4:
                messagebox.showwarning(title="Peringatan!", message='No. SKU harus berupa 4 angka!')
            elif bst.contains(sku):
                messagebox.showwarning(title='Gagal', message=f'No. SKU {sku} sudah terdaftar. Masukkan yang lain!')
            else:
                bst.insert(sku, namaBarang, harga, stok)
                self.tabelBarang()
                messagebox.showinfo(title='Berhasil', message=f'Berhasil Menambahkan :\nNo. SKU : {sku}\nNama Barang : {namaBarang}\nHarga Satuan : {harga}\nJumlah Stok : {stok}')
                self.hapusEntry('inputBarang')
        except ValueError:
            messagebox.showwarning(title="Peringatan!", message="No. SKU, Harga Satuan, dan Jumlah Stok harus berupa angka!")
            self.hapusEntry('inputBarang')

    #  Fungsi Get Input Restok Barang 
    def getRestokBarang(self): 
        sku = int(self.sku.get() )
        if bst.contains(sku) is None : 
            pilih = messagebox.askyesno(title='Berhasil', message=f'No. SKU {sku} Tidak Ditemukan. Mohon Lakukan Input Barang Terlebih Dahulu!')
            if pilih : 
                self.indikator(self.inputBarangInd,self.inputBarang, self.inputBarangPage, self.tabelBarang)
            else : 
                self.restokPage()
                self.tabelBarang()
                self.hapusEntry('restok')
        else :
            stok = int(self.stokBarang.get())
            bst.restock(sku,stok)
            self.tabelBarang()
            messagebox.showinfo(title='Berhasil', message=f"Jumlah Stok No. SKU {sku} Berhasil ditambahkan. Stok Sekarang {bst.contains(sku).jumlah_stok}")
            self.sku.delete(0, END)
            self.stokBarang.delete(0, END)

    # Fungsi Untuk Get Input Transaksi
    def getInputTransaksi(self):
        nama = self.namaKonsumen.get()
        sku = self.sku.get()
        jmlBeli = self.jmlBeli.get()

        if nama == '' or sku == '' or jmlBeli == '':
            return False
        try:
            nama = nama
            sku = int(sku)
            jmlBeli = int(jmlBeli)

            if not bst.contains(sku):

                messagebox.showwarning(title="Peringatan!", message=f'No.SKU {sku} belum terdaftar')
                self.sku.delete(0, END)
            else:
                trnsksi = transaksi.input_transaksi(bst, nama, sku, jmlBeli)
 
                if trnsksi:
                    messagebox.showinfo(title='Berhasil', message=f'Data Transaksi Konsumen Berhasil Disimpan.')
                    self.hapusEntry('inputTransaksi')
                    self.tabelBarang()
                else:
                    messagebox.showwarning(title="Peringatan!", message=f"Jumlah Stok No.SKU {sku} tidak mencukupi")
                    self.hapusEntry('inputTransaksi')
                    
        except ValueError:
            messagebox.showwarning(title="Peringatan!", message="No. SKU dan Jumlah Beli harus berupa angka!")
            self.hapusEntry('inputTransaksi')


    # Fungsi Untuk Memasukkan Data Barang Ke Tabel Barang
    def tabelBarang(self):
        self.tabel.delete(*self.tabel.get_children())

        data_list = bst.tampil()
        self.dataBarang = data_list
        for data in data_list: 
            self.tabel.insert(parent='', index='end', values=(data[0], data[1], data[2], data[3]))
    
    # Fungsi Untuk Menghapus Data Barang
    def deleteDataTabel(self):
        self.tabel_transaksi.delete(*self.tabel_transaksi.get_children())

    # Fungsi Untuk Memasukkan Daftar Transaksi Ke Treevier/Tabel
    def tabelTransaksi(self): 
        self.deleteDataTabel()

        data_list = transaksi.lihat_transaksi()
        for data in data_list: 
            self.tabel_transaksi.insert(parent='', index='end', values=(data['waktu transaksi'], data['nama konsumen'], data['no. sku'], data['jumlah beli'], data['subtotal']))

    # Fungsi Untuk Menampilkan Daftra Transaksi Berdasrkan Subtotal 
    def tabel_transaksi_by_subtotal(self):
        self.deleteDataTabel()

        data_list = transaksi.lihat_by_subtotal()
        for data in data_list: 
            self.tabel_transaksi.insert(parent='', index='end', values=(data['waktu transaksi'], data['nama konsumen'], data['no. sku'], data['jumlah beli'], data['subtotal']))

    # Fungsi Untuk Menampilkan Daftar Transaksi Berdarakasn Jumlah Beli
    def tabel_transaksi_by_jmlBeli(self):
        self.deleteDataTabel()

        data_list = transaksi.lihat_by_jmlBeli()
        for data in data_list: 
            self.tabel_transaksi.insert(parent='', index='end', values=(data['waktu transaksi'], data['nama konsumen'], data['no. sku'], data['jumlah beli'], data['subtotal']))

    # Fungsi Untuk Menghapus Entry 
    def hapusEntry(self, page) :
        if page == 'inputBarang' :
            self.sku.delete(0, END)
            self.namaBarang.delete(0, END)
            self.hargaSatuan.delete(0, END)
            self.stokBarang.delete(0, END)
        elif page == 'restok' :
            self.sku.delete(0, END)
            self.stokBarang.delete(0, END)

        elif page == 'inputTransaksi' :
            self.namaKonsumen.delete(0, END)
            self.sku.delete(0, END)
            self.jmlBeli.delete(0, END)
 
# MAIN
def main():
    window = Tk()
    bst.muatDariCsv('database_barang.csv')
    Sitorsi(window)
    Sitorsi(window).time()
    window.mainloop()

if __name__ == '__main__' :
    main()