import os
from PyQt5 import QtWidgets, QtGui, QtCore

class RenomearArquivosApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configurações básicas da janela
        self.setWindowTitle("Renomeador")
        self.setGeometry(100, 100, 500, 250)
        self.setWindowIcon(QtGui.QIcon())
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QLabel {
                color: #333;
            }
            QLineEdit {
                border: 1px solid #ccc;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #004a84;
            }
        """)

        layout = QtWidgets.QVBoxLayout()

        self.label_titulo = QtWidgets.QLabel("Renomear Arquivos")
        self.label_titulo.setStyleSheet("font-size: 20px; font-weight: bold; text-align: center;")
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.label_titulo)

        self.label_subtitulo = QtWidgets.QLabel("Selecione um diretório para renomear os arquivos de forma sequencial.")
        self.label_subtitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitulo.setStyleSheet("margin-bottom: 10px;")
        layout.addWidget(self.label_subtitulo)

        self.input_diretorio = QtWidgets.QLineEdit()
        self.input_diretorio.setPlaceholderText("Caminho do diretório...")
        layout.addWidget(self.input_diretorio)

        self.botao_selecionar = QtWidgets.QPushButton("Selecionar Pasta")
        self.botao_selecionar.clicked.connect(self.selecionar_pasta)
        layout.addWidget(self.botao_selecionar)

        self.botao_renomear = QtWidgets.QPushButton("Renomear Arquivos")
        self.botao_renomear.clicked.connect(self.renomear_arquivos)
        layout.addWidget(self.botao_renomear)

        self.setLayout(layout)

    def selecionar_pasta(self):
        diretorio = QtWidgets.QFileDialog.getExistingDirectory(self, "Selecione a Pasta")
        if diretorio:
            self.input_diretorio.setText(diretorio)

    def renomear_arquivos(self):
        diretorio = self.input_diretorio.text().strip()
        if not diretorio or not os.path.isdir(diretorio):
            QtWidgets.QMessageBox.critical(self, "Erro", "Por favor, insira um diretório válido.")
            return

        try:
            arquivos = [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
            arquivos.sort()

            for indice, arquivo in enumerate(arquivos, start=1):
                extensao = os.path.splitext(arquivo)[1]
                novo_nome = f"{indice}{extensao}"
                os.rename(os.path.join(diretorio, arquivo), os.path.join(diretorio, novo_nome))

            QtWidgets.QMessageBox.information(self, "Sucesso", f"Renomeação concluída! {len(arquivos)} arquivos renomeados.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao renomear arquivos: {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janela = RenomearArquivosApp()
    janela.show()
    sys.exit(app.exec_())
