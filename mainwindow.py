from PySide2.QtWidgets import QMainWindow #referencia al path y la clase QMainWindow
from PySide2.QtCore import Slot #importación de Slot
from ui_mainwindow import Ui_MainWindow #archivos con minusculas y clases con mayusculas
from administrador import Administrador
from particula import Particula
#union de codigo de archivo a programa con >
#ejemplo: pyside2-uic mainwindow.ui > ui_mainwindow.py

class MainWindow(QMainWindow): #llamar al constructor
    def __init__(self): #funcion
        super(MainWindow, self).__init__() #metodo
        #self se usa para que nuestro objeto exista globalmente y no solo en el constructor.

        self.administrador = Administrador()
        self.ui = Ui_MainWindow() #objeto referenciado
        self.ui.setupUi(self) #metodo para enbeber la instruccion
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar) #conectar las instrucciones de abajo
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear() #limpiar pantalla de PlaintText
        self.ui.salida.insertPlainText(str(self.administrador)) #salida datos introducidos por pantalla

    @Slot() #funcion Slot para recibir eventos
    def click_agregar(self): #funcion de botones
        #obtener infornacion para las variables
        #.tex() estrae el texto ingresado
        #self. esta asociado a las variables globales de el programa
        identificador = self.ui.identificador_lineEdit.text()
        origenx = self.ui.origen_x_spinBox.value()
        origeny = self.ui.origen_y_spinBox.value()
        destinox = self.ui.destino_x_spinBox.value()
        destinoy = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        #.value() regresa un valor entero
        # elementos del libro
        particula = Particula(identificador, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        #asociar el apartado globalmente
        self.administrador.agregar_final(particula)
        # print(titulo, autor, publicado, editorial)
        # mostrar los datos en el recuadro PlainText
       # self.ui.salida.insertPlainText(titulo + autor + str(publicado) + editorial)

    @Slot() #funcion Slot para recibir eventos
    def click_agregar_inicio(self): #funcion de botones
        #obtener infornacion para las variables
        #.tex() estrae el texto ingresado
        #self. esta asociado a las variables globales de el programa
        identificador = self.ui.identificador_lineEdit.text()
        origenx = self.ui.origen_x_spinBox.value()
        origeny = self.ui.origen_y_spinBox.value()
        destinox = self.ui.destino_x_spinBox.value()
        destinoy = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        #.value() regresa un valor entero
        particula = Particula(identificador, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        self.administrador.agregar_inicio(particula)
