from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel
#Cadastro do numeração das regiões:
zonas = ('SJ01','SJ01','SJ01','SJ01','SJ01','SJ01','SJ01','SJ01','SJ01','SJ01','SJ01','SJ01','SJ01','SJ01','SJ02','SJ02','SJ02','SJ02','SJ02','SJ02','SJ02','SJ02','SJ02','SJ02'
,'SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ03','SJ04','SJ04','SJ04','SJ04','SJ04','SJ04','SJ04','SJ04','SJ05','SJ05','SJ05','SJ05','SJ05','SJ05','SJ05','SJ05','SJ05','SJ05','SJ05','SJ06','SJ06','SJ06','SJ06','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01','JC01',)
#Cadatro das regiões:
nome_região = ('ZUADOR','MACAIBA','PARNAMIRIM','CENTRO SJM','TANCREDO NEVES','PAU BRASIL','QUEBRA FUZIL','BAIRRO NOVO','VILA MARIA','KM 38','GOGO DA EMA','BRISA','CIDADE DE DEUS'
,'MAZAPA','MONTE ALEGRE','MENDES','VALE DO LIRIO', 'JAPECANGA','LARANJEIRAS COSME','JARDIM','MENDENZINHO','ARENAN','VERA CRUZ','COBE','LARANJEIRA ABDIAS','RIBEIRO','MANIMBU','CAJEIRA','SITIO SANTA LUZIA','SITIO BURACO','CURRAL NOVO','BOA VISTA','MUNDO NOVO CIMA','MUNDO NOVO BAIXO','URUCARA','RIO DO MEIO','NASCENCA','BREJINHO','SANTA ANTONIO','VARZEA','NOVA CRUZ','PATANE','GEOGINO AVELINO','ARES','GOLANDI','CURRAIS','GENIPAPEIRO','CARNAUBA','GEORGE AVELINO','PATANE','ARES','GOIANINHA','NISIA FLORESTA','TOROROMBA','MORRINHOS','OITIZEIRO','CAMPO SANTANA','CAMURUPOM','BARRETA','TABATINGA','TIMBO','PORTO','BUZIOS','MONTE ALEGRE','BREJINHO','SANTO ANTONIO','NOVA CRUZ','ASSUNÇÃO','RIACHO SECO','ZABELE','CAJA','BOA SORTE','BAIXA DO MACACO','LAGEADO','MORADA NOVA','PEDRA DAGUA','CENTRO','ASSENT SÃO LUIZ','MATÃO','ASSENT XOA','BREJINHO 1','BREJINHO 2','CORTE','JUA','AS 100','SERRA VERDE',' CHICO MENDES','ARRIBÃO','SANTO ANTONIO','ARACATI')
modelo = QStandardItemModel(len(zonas),2)
modelo.setHorizontalHeaderLabels(['Zonas','Áreas'])



for linha, zona in enumerate(zonas):   
    elemento = QStandardItem(zona)
    modelo.setItem(linha, 0, elemento)

filtro = QSortFilterProxyModel()
filtro.setSourceModel(modelo)
filtro.setFilterKeyColumn(0)
filtro.setFilterCaseSensitivity(Qt.CaseInsensitive)

for linha, região in enumerate(nome_região):   
    elemento = QStandardItem(região)
    modelo.setItem(linha, 1, elemento)

filtro = QSortFilterProxyModel()
filtro.setSourceModel(modelo)
filtro.setFilterKeyColumn(1)
filtro.setFilterCaseSensitivity(Qt.CaseInsensitive)

app=QtWidgets.QApplication([])
tela=uic.loadUi("layout.ui")
tela.tableView.setModel(filtro)
tela.tableView.horizontalHeader().setStyleSheet("font-size: 35px;color: rgb(50, 50, 255);")
tela.barra_pesquisa.textChanged.connect(filtro.setFilterRegExp)

tela.show()
app.exec()