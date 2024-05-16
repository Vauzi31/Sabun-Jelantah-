import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDialog, QHBoxLayout, QInputDialog, QAction, QMenu, QMenuBar, QMainWindow
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtGui import QPixmap

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Login")
        self.setGeometry(700, 350, 500, 400)

        # Menambahkan gambar sabun di samping teks "Aplikasi Login"
        self.logo_label = QLabel(self)
        pixmap = QPixmap('sabun.png')  # Ganti 'sabun.png' dengan nama gambar sabun Anda
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setGeometry(-10, -40, 500, 400)  # Atur posisi dan ukuran gambar

        # Menambahkan menu bar
        menubar = self.menuBar()
        self.file_menu = menubar.addMenu('Fitur')

        # Membuat menu dropdown untuk tema
        self.theme_menu = QMenu('Tema', self)
        self.light_theme_action = QAction('Tema Terang', self)
        self.dark_theme_action = QAction('Tema Gelap', self)
        self.theme_menu.addAction(self.light_theme_action)
        self.theme_menu.addAction(self.dark_theme_action)
        self.file_menu.addMenu(self.theme_menu)

        # Membuat menu dropdown untuk fitur tambahan
        self.additional_menu = QMenu('Fitur Tambahan', self)
        self.profile_action = QAction('Profil Pengguna', self)
        self.download_action = QAction('Unduh Laporan', self)
        self.help_action = QAction('Bantuan', self)
        self.additional_menu.addAction(self.profile_action)
        self.additional_menu.addAction(self.download_action)
        self.additional_menu.addAction(self.help_action)
        self.file_menu.addMenu(self.additional_menu)

        # Menghubungkan aksi menu dengan metode
        self.light_theme_action.triggered.connect(self.set_light_theme)
        self.dark_theme_action.triggered.connect(self.set_dark_theme)
        self.profile_action.triggered.connect(self.show_profile)
        self.download_action.triggered.connect(self.download_report)
        self.help_action.triggered.connect(self.show_help)

        layout = QVBoxLayout()

        # Menambahkan label untuk menampilkan waktu
        self.time_label = QLabel()
        self.time_label.setStyleSheet("color: blue")  # Memberikan warna biru pada teks
        layout.addWidget(self.time_label)

        # Timer untuk mengupdate waktu setiap detik
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Set interval to 1000 milliseconds (1 second)

        self.username_label = QLabel("Username:")
        self.username_label.setStyleSheet("color: green")  # Memberikan warna hijau pada teks
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet("color: green")  # Memberikan warna hijau pada teks
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("background-color: orange")  # Memberikan warna oranye pada tombol
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_time(self):
        # Mendapatkan waktu dan tanggal saat ini
        current_datetime = QDateTime.currentDateTime()
        current_time = current_datetime.toString("hh:mm:ss")  # Format: Jam:Menit:Detik
        current_date = current_datetime.toString("dd MMMM yyyy")  # Format: Tanggal Bulan Tahun
        self.time_label.setText(f"Waktu: {current_time}, Tanggal: {current_date}")

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Menambahkan validasi untuk memastikan input tidak kosong
        if not username or not password:
            QMessageBox.warning(self, "Login Gagal", "Silakan isi username dan password.")
            return

        # Periksa jika username dan password benar
        if username == "admin" and password == "admin":
            confirmation = ConfirmationDialog().exec_()
            if confirmation == QDialog.Accepted:
                QMessageBox.information(self, "Login Berhasil", f"Selamat datang, {username}!")
                # Membuat dan menampilkan jendela menu
                self.menu_app = MenuApp()
                self.menu_app.show()
                self.hide()  # Menyembunyikan jendela login setelah login berhasil
        else:
            QMessageBox.warning(self, "Login Gagal", "Username atau password salah.")
            # Mengosongkan input setelah login gagal
            self.username_input.clear()
            self.password_input.clear()

    def set_light_theme(self):
        self.setStyleSheet("")
        self.statusBar().showMessage('Tema Terang Diterapkan')

    def set_dark_theme(self):
        self.setStyleSheet("background-color: #2b2b2b; color: white;")
        self.statusBar().showMessage('Tema Gelap Diterapkan')

    def show_profile(self):
        QMessageBox.information(self, "Profil Pengguna", "Ini adalah profil pengguna.")

    def download_report(self):
        QMessageBox.information(self, "Unduh Laporan", "Laporan telah berhasil diunduh.")

    def show_help(self):
        QMessageBox.information(self, "Bantuan", "Silakan hubungi admin untuk bantuan lebih lanjut.")

class ConfirmationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konfirmasi")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Apakah Anda ingin melanjutkan ke step berikutnya?"))
        self.yes_button = QPushButton("Ya")
        self.yes_button.setStyleSheet("background-color: lightgreen")  # Memberikan warna hijau muda pada tombol
        self.yes_button.clicked.connect(self.accept)
        self.no_button = QPushButton("Tidak")
        self.no_button.setStyleSheet("background-color: salmon")  # Memberikan warna salmon pada tombol
        self.no_button.clicked.connect(self.reject)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.yes_button)
        button_layout.addWidget(self.no_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)

class MenuApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Pilihan")
        self.setGeometry(700, 350, 500, 500)

        layout = QVBoxLayout()

        button1 = QPushButton("1. Sabun Jelantah")
        button1.setStyleSheet("background-color: lightyellow")  # Memberikan warna kuning muda pada tombol
        button1.clicked.connect(self.sabun_jelantah)
        layout.addWidget(button1)

        button2 = QPushButton("2. Bahan")
        button2.setStyleSheet("background-color: lightpink")  # Memberikan warna merah muda pada tombol
        button2.clicked.connect(self.show_bahan_dialog)
        layout.addWidget(button2)

        button3 = QPushButton("3. Cara Kerja")
        button3.setStyleSheet("background-color: lightcyan")  # Memberikan warna cyan muda pada tombol
        button3.clicked.connect(self.show_cara_kerja_dialog)
        layout.addWidget(button3)

        button4 = QPushButton("4. Penjualan")
        button4.setStyleSheet("background-color: lightgrey")  # Memberikan warna abu-abu muda pada tombol
        button4.clicked.connect(self.show_penjualan_dialog)
        layout.addWidget(button4)

        button5 = QPushButton("5. Keluar")
        button5.setStyleSheet("background-color: lightcoral")  # Memberikan warna coral muda pada tombol
        button5.clicked.connect(self.keluar)
        layout.addWidget(button5)

        self.setLayout(layout)

    def sabun_jelantah(self):
        QMessageBox.information(self, "Pengertian Sabun Jelantah", "Sabun Jelantah Itu Adalah Sabun olahan yang terbuat dari minyak jelantah Minyak jelantah merupakan minyak bekas hasil penggorengan rumah tangga, restaurant,atau pedagang kaki lima. Sabun jelantah ini merupakan produk yang dibuat untuk mengurangi limbah minyak jelantah yang biasanya langsung dibuang ke parit dan mencemari saluram drainase.")

    def show_bahan_dialog(self):
        confirmation = QMessageBox.question(self, "Konfirmasi",
                                            "Apakah Anda ingin mengetahui bahan-bahan yang akan digunakan?",
                                            QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            description = "Deskripsi Bahan\n\nBahan-bahan yang digunakan untuk membuat sabun jelantah antara lain:\n1. Minyak jelantah bekas penggorengan.\n2. Bahan pengemulsi seperti NaOH.\n3. Bahan pewangi dan pewarna."
            dialog = DescriptionDialog(description)
            if dialog.exec_() == QDialog.Accepted:
                QMessageBox.information(self, "Bahan",
                                        "Deskripsi Bahan\n\nBahan-bahan yang digunakan untuk membuat sabun jelantah antara lain:\n1. Minyak jelantah bekas penggorengan.\n2. Bahan pengemulsi seperti NaOH.\n3. Bahan pewangi dan pewarna.")

    def show_cara_kerja_dialog(self):
        confirmation = QMessageBox.question(self, "Konfirmasi", "Apakah Anda ingin mengetahui cara kerja?",
                                            QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            description = "Deskripsi Cara Kerja\n\nCara kerja pembuatan sabun jelantah adalah sebagai berikut:\n1. Pemanasan minyak jelantah bekas penggorengan hingga suhu tertentu.\n2. Campurkan minyak jelantah dengan bahan pengemulsi seperti NaOH dalam proporsi yang tepat.\n3. Tambahkan bahan pewangi dan pewarna sesuai selera.\n4. Aduk campuran secara merata hingga terbentuk adonan sabun.\n5. Tuangkan adonan ke dalam cetakan dan biarkan mengeras.\n6. Potong sabun menjadi bentuk yang diinginkan.\n7. Biarkan sabun mengering sebelum digunakan."
            dialog = DescriptionDialog(description)
            if dialog.exec_() == QDialog.Accepted:
                QMessageBox.information(self, "Cara Kerja",
                                        "Deskripsi Cara Kerja\n\nCara kerja pembuatan sabun jelantah adalah sebagai berikut:\n1. Pemanasan minyak jelantah bekas penggorengan hingga suhu tertentu.\n2. Campurkan minyak jelantah dengan bahan pengemulsi seperti NaOH dalam proporsi yang tepat.\n3. Tambahkan bahan pewangi dan pewarna sesuai selera.\n4. Aduk campuran secara merata hingga terbentuk adonan sabun.\n5. Tuangkan adonan ke dalam cetakan dan biarkan mengeras.\n6. Potong sabun menjadi bentuk yang diinginkan.\n7. Biarkan sabun mengering sebelum digunakan.")

    def show_penjualan_dialog(self):
        confirmation = ConfirmationDialog().exec_()
        if confirmation == QDialog.Accepted:
            product_interest, ok = QInputDialog.getItem(self, "Penjualan", "Apakah Anda Tertarik dengan produk kami?",
                                                        ["Ya", "Tidak"], 0, False)
            if ok:
                if product_interest == "Ya":
                    quantity, ok = QInputDialog.getInt(self, "Jumlah Pembelian",
                                                       "Berapakah Anda ingin Beli Jumlah Pembelian:", 1, 1, 100000, 1)
                    if ok:
                        total_price = 10500 * quantity

                        delivery_options = ["DiAmbil Sendiri", "DiAntar"]
                        delivery_option, ok = QInputDialog.getItem(self, "Pilihan Pengiriman",
                                                                   "Apakah Pesanan Anda Ingin DiAmbil Sendiri atau DiAntar Oleh Kami?",
                                                                   delivery_options, 0, False)
                        if ok:
                            if delivery_option == "DiAmbil Sendiri":
                                delivery_info = "Anda dapat mengambil pesanan Anda di alamat kami. Silahkan hubungi nomor telepon di bawah ini untuk mengatur waktu pengambilan."
                                contact_info = "Nomor Telepon: 085248106658"
                            else:
                                address, ok = QInputDialog.getText(self, "Alamat Pengiriman",
                                                                   "Masukkan Alamat Pengiriman:")
                                if ok and address.strip():  # Pastikan alamat tidak kosong
                                    delivery_info = f"Pesanan Anda akan diantar ke alamat:\n{address}"
                                    contact_info = "Nomor Telepon: 085248106658"
                                else:
                                    QMessageBox.warning(self, "Alamat Pengiriman",
                                                        "Alamat tidak boleh kosong. Silakan masukkan alamat yang valid.")
                                    return  # Kembali ke dialog pengiriman jika alamat kosong

                            QMessageBox.information(self, "Penjualan",
                                                    f"Anda telah membeli {quantity} unit dengan total harga Rp. {total_price}\n\n{delivery_info}\n{contact_info}")

    def keluar(self):
        QMessageBox.information(self, "Terima Kasih", "Terima kasih telah menggunakan aplikasi kami!")
        sys.exit()

class DescriptionDialog(QDialog):
    def __init__(self, description):
        super().__init__()
        self.setWindowTitle("Deskripsi")
        layout = QVBoxLayout()
        layout.addWidget(QLabel(description))
        self.ok_button = QPushButton("OK")
        self.ok_button.setStyleSheet("background-color: lightblue")  # Memberikan warna biru muda pada tombol
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()
    sys.exit(app.exec_())
