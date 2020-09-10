from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal
import folium
import webbrowser
from geopy.geocoders import Nominatim
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from helium import *
import os
import Design
import time
import glob
import shutil

class Ui_MainWindow(QDialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self)


    def setupUi(self, MainWindow):
        MAXx = 400
        MAXy = 600
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('C:/Projct/Logo/logo.png'))
        MainWindow.resize(MAXx, MAXy)
        MainWindow.setFixedSize(MAXx, MAXy)

        #------------------------------------------ Janela Principal--------------------------------------------------
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowIcon(QtGui.QIcon('C:/Projct/Logo/logo.png'))
        self.centralwidget.setStyleSheet(Design.stylesheet)

        #---------------------------------------------Janela de Escolha de Download------------------------------------
        self.download = QFrame(self.centralwidget)
        self.download.setStyleSheet(Design.stylesheet)
        self.download.setObjectName("frame1")
        self.download.move(50, 100)
        self.download.mousePressEvent = self.download_clicked
        self.download_texto = QLabel(self.download)
        self.download_texto.setText("Download de dados \n Clique aqui caso queira baixar dados da nuvem")
        self.download_texto.setWordWrap(True)
        self.download_texto.setObjectName("downloadTexto")
        self.download_texto.setAlignment(Qt.AlignCenter)
        self.download_texto.setStyleSheet(Design.stylesheet)
        #---------------------------------------------Janela de Escolha de Manipulação---------------------------------
        self.man = QFrame(self.centralwidget)
        self.man.setStyleSheet(Design.stylesheet)
        self.man.setObjectName("frame2")
        self.man.move(50, 275)
        self.man.mousePressEvent = self.man_clicked
        self.man_texto = QLabel(self.man)
        self.man_texto.setText("Manipulação de dados \n Clique aqui caso queira manipular dados")
        self.man_texto.setWordWrap(True)
        self.man_texto.setObjectName("manTexto")
        self.man_texto.setAlignment(Qt.AlignCenter)
        self.man_texto.setStyleSheet(Design.stylesheet)
        #---------------------------------------------Janela de Download----------------------------------------------
        self.download_grande = QFrame(self.centralwidget)
        self.download_grande.setObjectName("download_grande")
        self.download_grande.move(50, 100)
        self.download_grande.setStyleSheet(Design.stylesheet)
        self.download_grande.setVisible(False)
        self.flexa_dowload = QLabel(self.download_grande)
        self.flexa_dowload.setTextFormat(Qt.RichText)
        self.flexa_dowload.setText("&#8592;")
        self.flexa_dowload.setAlignment(Qt.AlignLeft)
        self.flexa_dowload.move(10, 10)
        self.flexa_dowload.setObjectName("flexa_download")
        self.flexa_dowload.setStyleSheet(Design.stylesheet)
        self.flexa_dowload.mousePressEvent = self.flexa_clicked
        self.download_texto_dentro = QLabel(self.download_grande)
        self.download_texto_dentro.setText("Download de dados")
        self.download_texto_dentro.setObjectName("downloadTextoDentro")
        self.download_texto_dentro.setAlignment(Qt.AlignCenter)
        self.download_texto_dentro.setStyleSheet(Design.stylesheet)
        self.hora_inicio = QLabel(self.download_grande)
        self.hora_inicio.setObjectName("hora_inicio")
        self.hora_inicio.setText("Hora de Início: ")
        self.hora_inicio.move(30, 50)

        self.hora_fim = QLabel(self.download_grande)
        self.hora_fim.setObjectName("hora_fim")
        self.hora_fim.setText("Hora fim: ")
        self.hora_fim.move(30, 90)

        self.ano = QLabel(self.download_grande)
        self.ano.setObjectName("ano")
        self.ano.setText("Ano: ")
        self.ano.move(30, 130)

        self.mes = QLabel(self.download_grande)
        self.mes.setObjectName("mes")
        self.mes.setText("Mês: ")
        self.mes.move(30, 170)

        self.dia = QLabel(self.download_grande)
        self.dia.setObjectName("dia")
        self.dia.setText("Dia: ")
        self.dia.move(30, 210)

        self.partition = QLabel(self.download_grande)
        self.partition.setObjectName("partition")
        self.partition.setText("Partição: ")
        self.partition.move(30, 250)

        self.hora_inicio_path = QLineEdit(self.download_grande)
        self.hora_inicio_path.setObjectName("horaIniciopath")
        self.hora_inicio_path.move(100, 45)

        self.hora_fim_path = QLineEdit(self.download_grande)
        self.hora_fim_path.setObjectName("horaFimpath")
        self.hora_fim_path.move(100, 85)

        self.ano_path = QLineEdit(self.download_grande)
        self.ano_path.setObjectName("Anopath")
        self.ano_path.move(100, 125)

        self.mes_path = QLineEdit(self.download_grande)
        self.mes_path.setObjectName("mespath")
        self.mes_path.move(100, 165)

        self.dia_path = QLineEdit(self.download_grande)
        self.dia_path.setObjectName("diapath")
        self.dia_path.move(100, 205)

        self.partition_path = QLineEdit(self.download_grande)
        self.partition_path.setObjectName("partitionPath")
        self.partition_path.move(100, 245)


        self.downloadOk = QPushButton(self.download_grande)
        self.downloadOk.setText("Ok")
        self.downloadOk.setObjectName("downloadOk")
        self.downloadOk.move(100, 275)
        self.downloadOk.clicked.connect(self.telaDownload)

        self.downloadProgress = QProgressBar(self.download_grande)
        self.downloadProgress.setObjectName("downloadProgress")
        self.downloadProgress.setGeometry(30, 315, 275, 20)
        self.downloadProgress.setMaximum(100)
        self.downloadProgress.hide()

        #--------------------------------------------Janela de Manipulação--------------------------------------------
        self.man_grande = QFrame(self.centralwidget)
        self.man_grande.setObjectName("man_grande")
        self.man_grande.move(50, 100)
        self.man_grande.setStyleSheet(Design.stylesheet)
        self.man_grande.setVisible(False)
        self.flexa = QLabel(self.man_grande)
        self.flexa.setTextFormat(Qt.RichText)
        self.flexa.setText("&#8592;")
        self.flexa.setAlignment(Qt.AlignLeft)
        self.flexa.move(10, 10)
        self.flexa.setObjectName("flexa")
        self.flexa.setStyleSheet(Design.stylesheet)
        self.flexa.mousePressEvent = self.flexa_clicked

        self.man_texto_dentro = QLabel(self.man_grande)
        self.man_texto_dentro.setText("Manipulação de dados")
        self.man_texto_dentro.setObjectName("manTextoDentro")
        self.man_texto_dentro.setAlignment(Qt.AlignCenter)
        self.man_texto_dentro.setStyleSheet(Design.stylesheet)

        self.local = QLabel(self.man_grande)
        self.local.setObjectName("local")
        self.local.setText("Localidade a ser buscada: ")
        self.local.move(30, 50)

        self.partitionMan = QLabel(self.man_grande)
        self.partitionMan.setObjectName("partitionMan")
        self.partitionMan.setText("Selecione o diretório")
        self.partitionMan.move(30, 125)

        self.localEdit = QLineEdit(self.man_grande)
        self.localEdit.setObjectName("localEdit")
        self.localEdit.move(30, 75)
        self.localEdit.hide()

        self.directory = QLineEdit(self.man_grande)
        self.directory.setObjectName("directory")
        self.directory.move(30, 150)
        self.directory.hide()

        self.buttonDirectory = QPushButton(self.man_grande)
        self.buttonDirectory.setObjectName("buttonDirectory")
        self.buttonDirectory.setText("...")
        self.buttonDirectory.clicked.connect(self.selecionaPasta)
        self.buttonDirectory.move(190, 150)
        self.buttonDirectory.hide()


        self.progressMan = QProgressBar(self.man_grande)
        self.progressMan.setObjectName("progressMan")
        self.progressMan.setMaximum(100)
        self.progressMan.setGeometry(30, 315, 275, 20)
        self.progressMan.hide()

        self.manIniciar = QPushButton(self.man_grande)
        self.manIniciar.setObjectName("manIniciar")
        self.manIniciar.setText("Iniciar")
        self.manIniciar.move(50, 305)
        self.manIniciar.clicked.connect(self.takeinputs)

        self.output_rd = QtWidgets.QTextBrowser(self.man_grande)
        self.output_rd.setGeometry(QtCore.QRect(40, 190, 200, 145))
        self.output_rd.setObjectName("output_rd")
        self.output_rd.hide()

        self.progress = QProgressBar(self.centralwidget)
        self.progress.setGeometry(75, 500, 300, 25)
        self.progress.setMaximum(100)
        self.progress.hide()

        self.buttonOk = QtWidgets.QPushButton(self.centralwidget)
        self.buttonOk.setGeometry(QtCore.QRect(90, 450, 80, 40))
        self.buttonOk.setObjectName("buttonOk")
        self.buttonOk.setStyleSheet(
            "background-color:#4e4e4e; color:#ffffff; font-size: 15px; padding-left:10px; padding: 4px;")
        self.buttonOk.hide()

        self.buttonCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCancelar.setGeometry(QtCore.QRect(250, 450, 80, 40))
        self.buttonCancelar.setObjectName("buttonCancelar")
        self.buttonCancelar.setStyleSheet(
            "background-color:#4e4e4e; color:#ffffff; font-size: 15px; padding-left:10px; padding: 4px;")
        self.buttonCancelar.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonOk.setText(_translate("MainWindow", "Abrir"))
        self.buttonOk.clicked.connect(self.takeinputs)
        self.buttonCancelar.setText(_translate("MainWindow", "Fechar"))
        self.buttonCancelar.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def selecionaPasta(self):
        self.file = QFileDialog.getExistingDirectory(self, "Selecione o diretório")
        if self.file:
            self.directory.setText(self.file)
            self.lang = str(self.file)[0:1]
            self.roll = str(self.file)[10:34]

    def selecionaArquivo(self):
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo", "",
                                                  "All Files (*);; CSV Files (*.csv);; NC Files (*.nc)")
        if self.fileName:
            print(self.fileName, _)
            self.directory.setText(self.fileName)

    def flexa_clicked(self, event):
        self.download.setVisible(True)
        self.man.setVisible(True)
        self.download_grande.setVisible(False)
        self.man_grande.setVisible(False)
        self.hora_inicio_path.setText("")
        self.hora_fim_path.setText("")
        self.ano_path.setText("")
        self.mes_path.setText("")
        self.dia_path.setText("")
        self.partition_path.setText("")
        self.directory.setText("")
        self.localEdit.setText("")


    def man_clicked(self, event):
        print("Simples")
        self.download.setVisible(False)
        self.man.setVisible(False)
        self.download_grande.setVisible(False)
        self.man_grande.setVisible(True)

    def download_clicked(self, event):
        print("Complexo")
        self.download.setVisible(False)
        self.man.setVisible(False)
        self.download_grande.setVisible(True)
        self.man_grande.setVisible(False)

    def takeinputs(self):
        QtCore.QTimer.singleShot(0, self.after_show)
        self.name, self.done1 = QtWidgets.QInputDialog.getText(
            self, 'Input Dialog', 'Nome da localidade:')

        # cgpa, done3 = QtWidgets.QInputDialog.getDouble(
        #      self, 'Input Dialog', 'Enter your CGPA:')
        # QtCore.QTimer.singleShot(0, self.after_show)

        if self.done1 and len(self.name) != 0:
            # Showing confirmation message along
            # with information provided by user.

            self.localEdit.setText(self.name)
            #self.manIniciar.hide()
            geolocator = Nominatim(user_agent="ver0z")
            self.location = geolocator.geocode(f"{self.name}")

            try:
                if self.location != None:
                    self.localEdit.show()
                    print(self.location.address)
                    print((self.location.latitude, self.location.longitude))
                    print(self.location.raw)
                    # m = folium.Map(location=[location.latitude, location.longitude], zoom_start=4)
                    # folium.Marker(location=[location.latitude, location.longitude], popup=f"<strong>{location.address}</strong>", tooltip="Click for more information").add_to(m)
                    # m = folium.Map(location=[location.latitude, location.longitude],tiles="Stamen Terrain", zoom_start=12)
                    m = folium.Map(location=[self.location.latitude, self.location.longitude], zoom_start=12)
                    folium.Marker(location=[self.location.latitude, self.location.longitude],
                                  popup=f"<strong>{self.location.address}</strong>", tooltip="Click for more information").add_to(m)

                    filepath = 'C:/Projct/Report/map.html'

                    m.save(filepath)
                    webbrowser.open('file://' + filepath)

                    # Hide the pushbutton after inputs provided by the use.
                    #self.pseudo.hide()
                    self.buttonOk.hide()

                    buttonResposta = QMessageBox.question(self, '', "A localização está correta ?",
                                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    self.buttonMapa = QMessageBox.question(self, '', "Utilizar o mapa ?",
                                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if buttonResposta == QMessageBox.Yes:
                        print('Yes clicked.')
                        self.manIniciar.hide()
                        self.directory.show()
                        self.buttonDirectory.show()
                        self.filtro, self.done1_1_1 = QtWidgets.QInputDialog.getInt(
                            self, 'Input Dialog', 'Tamanho do filtro:')
                        self.user, self.done3 = QtWidgets.QInputDialog.getText(
            self, 'Input Dialog', 'Nome do usuário:')


                        self.selecionaPasta()

                        #QtCore.QTimer.singleShot(0, self.after_show)
                        #self.roll, self.done1_1_2 = QtWidgets.QInputDialog.getText(
                        #    self, 'Input Dialog', 'Pasta para busca:')
                        #langs = ['C', 'D', 'E', 'F', 'G']
                        #self.lang, self.done1_1_3 = QtWidgets.QInputDialog.getItem(
                        #    self, 'Input Dialog', 'Partição em uso:', langs)
                        if self.done1_1_1 and len(self.roll) !=0  and len(self.lang) != 0:
                            self.manipula()


                    else:
                        print('No clicked.')
                else:
                    self.takeinputs()
            except ValueError:
                print("Lugar inexistente")




    def after_show(self):
        size = QtCore.QSize(400, 100)
        for d in self.findChildren(QtWidgets.QInputDialog):
            if d.isVisible():
                d.resize(size)

    def manipula(self):


        print(self.location.latitude, self.location.longitude)

        import matplotlib.pyplot as plt
        from netCDF4 import Dataset
        import numpy as np
        import math
        import pandas as pd
        import os
        import datetime
        from datetime import date
        from matplotlib.patches import Circle
        import csv

        os.environ["PROJ_LIB"] = f"C:\\Users\\{self.user}\\anaconda3\\Library\\share"
        from mpl_toolkits.basemap import Basemap
        csfont = {'fontname': 'Arial'}
        # today = str(date.today())
        # today_datentime = datetime.datetime.today()
        # now = datetime.datetime.now()
        # year = now.year

        tic = time.perf_counter()
        # Get the data from today
        # time_finish = today_datentime.hour
        # fmt = '%Y-%m-%d'
        # dt = datetime.datetime.strptime(today, fmt)
        # tt = dt.timetuple()
        # day_in_year = str(tt.tm_yday)
        # hour = range(0, 0)
        # Get the data from a specific year, day and time.
        # year = 2020
        # day_in_year = 189

        # fs = s3fs.S3FileSystem(anon=True)
        # fs.ls('s3://noaa-goes/')
        # files = np.array(fs.ls('noaa-goes17/ABI-L2-MCMIPC/2019/240/00/'))
        # print(type(files))

        # fs.get(files[0], files[0].split('/')[-1])
        # Local de instalaçao do sistema de alarme
        # Lat_sensor = -1.473777
        # Long_sensor = -48.452123

        Lat_sensor = self.location.latitude
        Long_sensor = self.location.longitude
        Lat_Cast = -1.287709
        Long_Cast = -47.989619
        Lat1 = Lat_sensor * np.pi / 180
        Lon1 = Long_sensor * np.pi / 180
        Lat2 = Lat_Cast * np.pi / 180
        Lon2 = Long_Cast * np.pi / 180

        D = 6378137.00 * math.acos(
            math.cos(Lat1) * math.cos(Lat2) * math.cos(Lon2 - Lon1) + math.sin(Lat1) * math.sin(Lat2))
        print("Distancia do sensor para Marituba {0:0.2f} metros".format(D))
        self.contador_belem = 0
        contador_aleatorio = 0
        flashes = []
        dia_formatado_i = ''
        dia_formatado_f = ''
        temp = ''
        tempo_exato = ''
        hora_i = ''
        hora_f = ''
        self.max_l = 0
        self.min_l = 50
        self.aver = 0
        correction = 1.8
        # filtro = float(input('Qual o tamanho do filtro ? \n'))
        # pasta = input('Qual pasta percorrer ? \n')

        lng = 0.1444681 * ((self.filtro / 10) + 2)
        ltd = 0.0899321 * ((self.filtro / 10) + 2)
        DPI = 150
        ax = plt.figure(figsize=(2000 / float(DPI), 2000 / float(DPI)), frameon=True, dpi=DPI)
        ax
        self.progress.show()
        self.tamanho()
        title = os.listdir(f'{self.lang}:/Projct/{self.roll}')[0][
                20:27]  # Pega o título do primeiro arquivo e extrai a posição entre 20:27

        print(self.roll)

        for self.i in range(1, self.counternc + 1):
            QtCore.QCoreApplication.processEvents()  # Evitar travamentos e deixar a interface responsiva
            self.prog()
            contador_aleatorio += 1
            print('Sou o numero de arquivo ################################## {0}'.format(self.i))
            path = ('{3}:/Projct/{1}/OR_GLM-L2-LCFA_G16_s{2} ({0}).nc'.format(self.i, self.roll, title, self.lang))
            g16glm = Dataset(path)
            # Pegando o tempo do arquivo
            tempo_inicio = g16glm.getncattr('time_coverage_start')
            tempo_final = g16glm.getncattr('time_coverage_end')
            temp = g16glm.variables['flash_time_offset_of_first_event'][:]
            dia_formatado = tempo_inicio[0:4] + ',' + tempo_inicio[5:7] + ',' + tempo_inicio[8:10]
            tempo_inicio_formatado = tempo_inicio[11:13] + ',' + tempo_inicio[14:16] + ',' + tempo_inicio[17:21]
            tempo_final_formatado = tempo_final[11:13] + ',' + tempo_final[14:16] + ',' + tempo_final[17:21]

            print(dia_formatado)
            print(tempo_inicio_formatado)
            print(tempo_final_formatado)

            event_lat = g16glm.variables['event_lat'][:]
            event_lon = g16glm.variables['event_lon'][:]

            group_lat = g16glm.variables['group_lat'][:]
            group_lon = g16glm.variables['group_lon'][:]

            flash_lat = g16glm.variables['flash_lat'][:]
            flash_lon = g16glm.variables['flash_lon'][:]
            id_flash = g16glm.variables['flash_id'][:]

            tme = len(event_lat)
            tmg = len(group_lat)
            tma = len(flash_lat)
            print('Tamanho de eventos {0}'.format(tme))
            print('Tamanho de grupos {0}'.format(tmg))
            print('Tamanho de flashes {0}'.format(tma))

            if contador_aleatorio == 1:
                dia_formatado_i = dia_formatado
                hora_i = tempo_inicio_formatado
            else:
                dia_formatado_f = dia_formatado
                hora_f = tempo_final_formatado

            for cnt in range(1, tma):
                print('Fora do if {0}'.format(cnt))
                Lat_sensor = self.location.latitude
                Long_sensor = self.location.longitude
                Lat_Raio = flash_lat[cnt]
                Long_Raio = flash_lon[cnt]
                Lat1 = Lat_sensor * np.pi / 180
                Lon1 = Long_sensor * np.pi / 180
                Lat2 = Lat_Raio * np.pi / 180
                Lon2 = Long_Raio * np.pi / 180
                Dr = (6378137.00 * math.acos(
                    math.cos(Lat1) * math.cos(Lat2) * math.cos(Lon2 - Lon1) + math.sin(Lat1) * math.sin(
                        Lat2))) / 1000  # Calcula a distância que o raio aconteceu
                Dis_raio = float('{:.3f}'.format(Dr))  # Calcula a distância que o raio aconteceu

                if bool(Dis_raio <= self.filtro):
                    var = str(int(tempo_inicio[17:19]) + float(temp[cnt]))

                    tempo_exato = tempo_inicio[11:13] + ',' + tempo_inicio[14:16] + ',' + var[0:6]

                    # if bool(-49 <= flash_lon[cnt] <= -47) and bool(-1.67 <= flash_lat[cnt] <= -0.94):
                    # if bool(-47.871 <= flash_lon[cnt] <= -47.771) and bool(-2.991 <= flash_lat[cnt] <= -2.910):

                    if Dis_raio > self.max_l:
                        self.max_l = Dis_raio
                    if Dis_raio < self.min_l:
                        self.min_l = Dis_raio
                    self.aver += Dis_raio
                    print('Latitude: {0}'.format(flash_lat[cnt]))
                    print('Longitude: {0}'.format(flash_lon[cnt]))
                    self.contador_belem += 1

                    print('O raio ocorreu a {0:0.2f} Km do sensor'.format(Dis_raio))
                    # print('Horário: {0}'.format(hora))
                    print('Caíram {0} raios em Belém'.format(self.contador_belem))
                    # fig = plt.figure(figsize=(6, 6), dpi=200)
                    # Localização de Belém #
                    if self.buttonMapa == QMessageBox.Yes:
                        self.map = Basemap(llcrnrlon=Long_sensor - lng, llcrnrlat=Lat_sensor - ltd, urcrnrlon=Long_sensor + lng,
                                      urcrnrlat=Lat_sensor + ltd, resolution='h',
                                      epsg=3857)
                    # Localização de Canaã #
                    # map = Basemap(llcrnrlon=-48.027496, llcrnrlat=-3.018657, urcrnrlon=-47.630615, urcrnrlat=-2.845163, resolution='h',
                    #              epsg=3857)

                    # Localização de toda américa #
                    # map = Basemap(projection='merc', lat_0=0, lon_0=-70.0,
                    #             resolution='l', area_thresh=1000.0,
                    #              llcrnrlon=-135.0,
                    # 	          llcrnrlat=-65.0, #lower left corner latitude
                    #              urcrnrlon=0.0,
                    # 	          urcrnrlat=65.0) #upper right lat
                    if self.contador_belem == 1:
                        print('Dentro do if {0}'.format(cnt))

                        flashes = pd.DataFrame({'flash_id': g16glm.variables['flash_id'][::cnt],
                                                'Data': dia_formatado,
                                                'Tempo_inicio': tempo_inicio_formatado,
                                                'Tempo_final': tempo_final_formatado,
                                                'Tempo_exato': tempo_exato,
                                                'Distância': Dis_raio,
                                                'flash_time_offset_of_first_event': g16glm.variables[
                                                                                        'flash_time_offset_of_first_event'][
                                                                                    ::cnt],
                                                'flash_time_offset_of_last_event': g16glm.variables[
                                                                                       'flash_time_offset_of_last_event'][
                                                                                   ::cnt],
                                                'flash_frame_time_offset_of_first_event': g16glm.variables[
                                                                                              'flash_frame_time_offset_of_first_event'][
                                                                                          ::cnt],
                                                'flash_frame_time_offset_of_last_event': g16glm.variables[
                                                                                             'flash_frame_time_offset_of_last_event'][
                                                                                         ::cnt],
                                                'flash_lat': g16glm.variables['flash_lat'][::cnt],
                                                'flash_lon': g16glm.variables['flash_lon'][::cnt],
                                                'flash_area': g16glm.variables['flash_area'][::cnt],
                                                'flash_energy': g16glm.variables['flash_energy'][::cnt],
                                                'flash_quality_flag': g16glm.variables['flash_quality_flag'][::cnt],
                                                'product_time': g16glm.variables['product_time'][::cnt]
                                                })
                        flashes_p = flashes[flashes.flash_id == id_flash[cnt]]
                        saveCsv = 'C:/Projct/Report/'
                        flashes_p.to_csv(saveCsv+'{0}.csv'.format(self.roll), index=False)
                    else:
                        print('Dentro do if {0}'.format(cnt))
                        print(id_flash[cnt])
                        flashes2 = pd.DataFrame({'flash_id': g16glm.variables['flash_id'][::cnt],
                                                 'Data': dia_formatado,
                                                 'Tempo_inicio': tempo_inicio_formatado,
                                                 'Tempo_final': tempo_final_formatado,
                                                 'Tempo_exato': tempo_exato,
                                                 'Distância': Dis_raio,
                                                 'flash_time_offset_of_first_event': g16glm.variables[
                                                                                         'flash_time_offset_of_first_event'][
                                                                                     ::cnt],
                                                 'flash_time_offset_of_last_event': g16glm.variables[
                                                                                        'flash_time_offset_of_last_event'][
                                                                                    ::cnt],
                                                 'flash_frame_time_offset_of_first_event': g16glm.variables[
                                                                                               'flash_frame_time_offset_of_first_event'][
                                                                                           ::cnt],
                                                 'flash_frame_time_offset_of_last_event': g16glm.variables[
                                                                                              'flash_frame_time_offset_of_last_event'][
                                                                                          ::cnt],
                                                 'flash_lat': g16glm.variables['flash_lat'][::cnt],
                                                 'flash_lon': g16glm.variables['flash_lon'][::cnt],
                                                 'flash_area': g16glm.variables['flash_area'][::cnt],
                                                 'flash_energy': g16glm.variables['flash_energy'][::cnt],
                                                 'flash_quality_flag': g16glm.variables['flash_quality_flag'][::cnt],
                                                 'product_time': g16glm.variables['product_time'][::cnt]
                                                 })
                        # print(flashes)

                        flashes_s = flashes.append(flashes2)
                        flashes_s = flashes2[flashes2.flash_id == id_flash[cnt]]
                        saveCsv = 'C:/Projct/Report/'
                        flashes_s.to_csv(saveCsv+'{0}.csv'.format(self.roll), mode='a', header=False, index=False)
                    if self.buttonMapa == QMessageBox.Yes:
                        self.map.drawcoastlines()
                        self.map.drawcountries()
                        self.map.fillcontinents(color='#bbdaa4', lake_color='#a7cdf2')
                        self.map.drawmapboundary(fill_color='#a7cdf2')

                        # map.drawmapscale(Long_sensor-0.33, Lat_sensor-0.23, Long_sensor-0.33, Lat_sensor-0.23, filtro*2, barstyle='fancy')

                        # Plot events as large blue dots
                        # event_x, event_y = map(event_lon[cnt], event_lat[cnt])
                        # map.plot(event_x, event_y, 'bo', markersize=7)
                        # Plot groups as medium green dots
                        # group_x, group_y = map(group_lon[cnt], group_lat[cnt])
                        # map.plot(group_x, group_y, 'go', markersize=3)
                        # Plot flashes as small red dots

                        x, y = self.map(Long_sensor, Lat_sensor)
                        self.map.plot(x, y, 'bo', markersize=4, label='LPDA')
                        circle = Circle((x, y), radius=self.filtro * 1010, fill=False)
                        plt.gca().add_patch(circle)
                        print('Raio {0}'.format(self.map.ymax - self.map.ymin))
                        flash_x, flash_y = self.map(flash_lon[cnt], flash_lat[cnt])
                        self.map.plot(flash_x, flash_y, 'ro', markersize=3, label='Raios')
                        az = plt.gca()
                        handles, labels = az.get_legend_handles_labels()
                        legend = plt.legend([labels[0], labels[1]])
                        # Add logos / images to the plot
                        logo_LPDA = plt.imread('C:\\Projct\\Logo\\lpda.png')
                        logo_UFPA = plt.imread('C:\\Projct\\Logo\\ufpa.png')
                        ax.figimage(logo_LPDA, 1020, 79, zorder=3, alpha=1, origin='upper')
                        ax.figimage(logo_UFPA, 950, 75, zorder=3, alpha=1, origin='upper')
                        if self.filtro == 10:
                            ad = 1.8
                        else:
                            ad = correction + self.filtro/1000
                        x2, y2 = self.map(Long_sensor + ((0.1444681 * (self.filtro / 10)) / ad),
                                     Lat_sensor + ((0.0899321 * (self.filtro / 10))) / ad)
                        plt.annotate(f'{self.filtro:0.0f} Km', xy=(x, y), xycoords='data',
                                     xytext=(x2, y2),
                                     textcoords='data',
                                     arrowprops=dict(facecolor='black', lw=0.3, arrowstyle="<->"),
                                     # arrowprops={"arrowstyle": "-", "linestyle": "--", "linewidth": 3, "shrinkA": 0, "shrinkB": 0})
                                     )


        print('Caíram {0} raios em Belém'.format(self.contador_belem))

        plt.title(
            "GOES-16 GLM - Monitoramento de raios" "\n Escaneamento do dia " + dia_formatado_i[
                                                                               8:10] + "/" + dia_formatado_i[
                                                                                             5:7] + "/" + dia_formatado_i[
                                                                                                          0:4]
            + " - " + hora_i[0:2] + ":" + hora_i[3:5] + ":" + hora_i[6:8] + " UTC até " + dia_formatado_f[
                                                                                          8:10] + "/" + dia_formatado_f[
                                                                                                        5:7] + "/" + dia_formatado_f[
                                                                                                                     0:4]
            + " - " + hora_f[0:2] + ":" + hora_f[3:5] + ":" + hora_f[6:8], **csfont)
        toc = time.perf_counter()
        print(f'Tempo decorrido  ', toc - tic)
        print(f'Distância máxima ', self.max_l)
        print(f'Distância mínima ', self.min_l)
        print(f'Distância média  ', self.aver / self.contador_belem)

        plt.show()

        # DPI = 150
        # plt.savefig('C:\goes16\GOES-16_Ch13.png', dpi=DPI, bbox_inches='tight', pad_inches=0)

        # eventos = pd.DataFrame({'event_id': g16glm.variables['event_id'][:],
        #                        'event_time_offset': g16glm.variables['event_time_offset'][:],
        #                        'event_lat': g16glm.variables['event_lat'][:],
        #                        'event_lon': g16glm.variables['event_lon'][:],
        #                        'event_energy': g16glm.variables['event_energy'][:],
        #                        'event_parent_group_id': g16glm.variables['event_parent_group_id'][:]})

        # grupos = pd.DataFrame({'group_id': g16glm.variables['group_id'][:],
        #                      'group_time_offset': g16glm.variables['group_time_offset'][:],
        #                       'group_frame_time_offset': g16glm.variables['group_frame_time_offset'][:],
        #                       'group_lat': g16glm.variables['group_lat'][:],
        #                       'group_lon': g16glm.variables['group_lon'][:],
        #                       'group_area': g16glm.variables['group_area'][:],
        #                       'group_energy': g16glm.variables['group_energy'][:],
        #                       'group_parent_flash_id': g16glm.variables['group_parent_flash_id'][:],
        #                       'group_quality_flag': g16glm.variables['group_quality_flag'][:],
        #                       })

        # eventos.to_csv('eventos.csv', index=False)
        # grupos.to_csv('grupos.csv', index=False)

        # map = Basemap(llcrnrlon=3.75,llcrnrlat=39.75,urcrnrlon=4.35,urcrnrlat=40.15, epsg=5520)
        # http://server.arcgisonline.com/arcgis/rest/services

        # map.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 1500, verbose= True)
        # plt.show()
        self.flexa.hide()
        self.output_rd.show()
        if self.contador_belem > 0:
            self.output_rd.append(f'Filtro (Km): {self.filtro} \nLocal: {self.location.address} \nLatitude: {self.location.latitude} \nLongitude: {self.location.longitude} \nQuantidade de raios na região: {self.contador_belem} \nDistância máxima: {self.max_l} \nDistância mínima: {self.min_l} \nDistância média: {self.aver/self.contador_belem}')
            self.buttonCancelar.show()
            if self.buttonMapa == QMessageBox.Yes:
                self.getcsv()





    def getcsv(self):
        start_chrome('http://geojson.io/#map=2/20.0/0.0')
        time.sleep(5)
        self.selecionaArquivo()
        print(self.fileName)
        drag_file(f'{self.fileName}', to="Table")

    def prog(self):
        if self.i < self.counternc + 1:
            percent = self.i*(100/self.counternc)
            self.progress.setValue(percent)

    def progDownload(self):
        if self.i < self.length + 1:
            percent = self.i*(100/self.length)
            self.progress.setValue(percent)


    def tamanho(self):
        self.counternc = len(glob.glob1(f'{self.lang}:/Projct/{self.roll}', '*.nc'))

    def telaDownload(self):
        import s3fs
        import numpy as np
        import datetime
        self.hora_i_tela = int(self.hora_inicio_path.text())
        self.hora_f_tela = int(self.hora_fim_path.text())
        self.hour_tela = range(self.hora_i_tela, self.hora_f_tela, 1)
        self.ano_tela = int(self.ano_path.text())
        self.mes_tela = int(self.mes_path.text())
        self.dia_tela = int(self.dia_path.text())
        self.part_tela = self.partition_path.text()

        self.today = datetime.datetime(self.ano_tela, self.mes_tela, self.dia_tela, 00, 00)
        self.day_in_year = (self.today - datetime.datetime(self.ano_tela, 1, 1)).days + 1
        print(self.day_in_year)
        # hour = 00
        # Use the anonymous credentials to access public data
        fs = s3fs.S3FileSystem(anon=True)

        # # List contents of GOES-16 bucket.
        fs.ls('s3://noaa-goes16/')

        for t in self.hour_tela:
            QtCore.QCoreApplication.processEvents()  # Evitar travamentos e deixar a interface responsiva
            print(t)
            #if t < 10:
            files = np.array(fs.ls('noaa-goes16/GLM-L2-LCFA/{0}/{1:03d}/{2:02d}/'.format(self.ano_tela, self.day_in_year, t)))
            print(files)
            self.length = len(files)  # Getting the number of .nc files
            print(self.length)
            for self.i in range(0, self.length):
                QtCore.QCoreApplication.processEvents()  # Evitar travamentos e deixar a interface responsiva
                self.progress.show()
                self.progDownload()

                fs.get(files[self.i],
                       files[self.i].split('/')[-1])  # Writting all those .nc files in the directory of your script

                  #print('End of minus 10')
              #else:
                  #files = np.array(fs.ls('noaa-goes16/GLM-L2-LCFA/{0}/{1:03d}/{2:02d}/'.format(year, day_in_year, t)))
                  #print(files)
                  #length = len(files)  # Getting the number of .nc files
                  #print(length)
                  #for i in range(0, length):
                  #    fs.get(files[i],
                  #           files[i].split('/')[-1])  # Writting all those .nc files in the directory of your script
                  #print('End over 10')
        self.buttonCancelar.show()

        self.criarPasta('{5}:\\Projct\\{0:02d}-{1:02d}-{2}T{3}h00m#{4}h00m'.format(self.dia_tela, self.mes_tela, self.ano_tela, self.hora_i_tela, self.hora_f_tela, self.part_tela))
        self.mover('{5}:\\Projct\\{0:02d}-{1:02d}-{2}T{3}h00m#{4}h00m'.format(self.dia_tela, self.mes_tela, self.ano_tela, self.hora_i_tela, self.hora_f_tela, self.part_tela))
        self.renomear('{5}:\\Projct\\{0:02d}-{1:02d}-{2}T{3}h00m#{4}h00m'.format(self.dia_tela, self.mes_tela, self.ano_tela, self.hora_i_tela, self.hora_f_tela, self.part_tela))
        #  # self.size('C:\\goes16\\{0:02d}-{1:02d}-{2} T {3}h00m # {4}h00m'.format(self.values['dia'], self.values['mes'], self.values['ano'], self.values['horai'], self.values['horaf']))  # Duas barras fazem diferença


    #
    # Cria uma pasta com a data informada
    #
    def criarPasta(self, data):
        caminho_destino = data
        caminho_report = f'{self.partition}:/Projct/Report'
        try:
            if not os.path.exists(caminho_destino):
                os.makedirs(caminho_destino)
            if not os.path.exists(caminho_report):
                os.makedirs(caminho_report)

        except OSError:
            print("Erro ao criar o diretório, " + caminho_destino)

    #
    # Move os arquivos baixados para uma pasta
    #
    def mover(self, data):
        caminho_fonte = os.getcwd()
        caminho_destino = data
        lista_arquivos_fonte = os.listdir(caminho_fonte)

        for file in lista_arquivos_fonte:
            if file.endswith('.nc'):
                shutil.move(os.path.join(caminho_fonte, file), os.path.join(caminho_destino, file))

    #
    # Mostra o tamanho total do arquivo
    #

    # def size(self, data):
    # Inicializa a variável que vai armazenar o tamanho total da pasta
    #    tamanho_total = 0

    #    # Usando o método walk() para navegar entre os diretórios
    #    for dirpath, dirnames, filenames in os.walk(data):
    #        for i in filenames:
    #            # O .join é para concatenação de todos componentes da pasta
    #            f = os.path.join(dirpath, i)
    #            # Usar o getsize para pegar o tamanho em bytes e ir salvando o valor acumulado

    #           tamanho_total += os.path.getsize(f)
    #   return tamanho_total

    # print('{0:0.5f} GB'.format(size() / 1073741824))

    def renomear(self, data):
        caminho_destinho = data
        path = caminho_destinho
        file_num = 1
        doc = os.listdir(caminho_destinho)[0]
        # doc = os.listdir(path)[0]
        doc_part = caminho_destinho + '\\' + doc[:27]
        print(doc_part)

        for filename in glob.glob(os.path.join(path, '*.nc')):
            print(filename)
            os.rename(filename, doc_part + ' (' + str(file_num) + ')' + '.nc')
            file_num += 1






if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



