# Программа по работе с GUI

# Импортируемые модули
import sys  
import os  
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTextEdit, QTableWidget, QTableWidgetItem, QMessageBox
from design import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """Главное окно"""
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # обработчики нажатий
        self.actionBrowse.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionClear.triggered.connect(self.clear_text)
        self.tableWidget.itemClicked.connect(self.click_discription)
        self.addOrder.clicked.connect(self.add_order)
        self.newOrder.clicked.connect(self.clear_text)
        self.saveOrder.clicked.connect(self.save_file)

    def open_file(self):
        """Метод для добавления списка товаров в из требуемого файла в таблицу"""
        global info
        info = {}
        directory = QFileDialog.getOpenFileName(self, "Выберите папку")[0]
        file = open(directory , 'r', encoding='utf-8')
        # чтение из файла
        with file as f:
            i = 0
            data = f.read()
            mystring = data.split("\n")
            self.tableWidget.setRowCount(len(mystring))
            for newstring in mystring:
                # введение данных из файла в таблицу
                name_price = newstring.split(":\t")
                name = str(name_price[0])
                price = str(name_price[1])
                disc = str(name_price[2])
                self.tableWidget.setItem(i, 0, QTableWidgetItem(name))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(price))
                # окрашивание ячеек таблицы
                if i % 2:
                    self.tableWidget.item(i, 0).setBackground(QtGui.QColor(125,125,125))
                    self.tableWidget.item(i, 1).setBackground(QtGui.QColor(125,125,125))
                info[name] = disc
                i += 1

    def click_discription(self):
        """Метод для выведения описания товара"""
        row = self.tableWidget.currentItem().row()
        column = self.tableWidget.currentItem().column()
        itemnew = self.tableWidget.item(row, column).text()
        if itemnew in info:
            self.textEditDiscrip.setText(info[itemnew])
        
    def add_order(self):
        """Метод для добавления товара в заказ и получения суммы заказа"""
        row = self.tableWidget.currentItem().row()
        column = self.tableWidget.currentItem().column()
        rowprice = self.tableWidget.currentItem().row()
        columnprice = self.tableWidget.currentItem().column() + 1
        
        itemnew = self.tableWidget.item(row, column).text()
        total = self.tableWidget.item(rowprice, columnprice).text()

        # выведения цены
        for pr in total.split():
            if pr.isdigit():
                totalprice = int(pr)

        if self.orderPrice.text() == "":
            price = 0
        else:
            price = int(self.orderPrice.text())
        totalprice += price

        # добавление товара в заказ и суммирование цены с имеющийся
        self.textEditNew.append(itemnew)
        self.orderPrice.setText(str(totalprice))
    
    def save_file(self):
        """Метод для сохранения заказа"""
        directory = QFileDialog.getSaveFileName(self, "Выберите папку")[0]
        file = open(directory , 'w', encoding='utf-8')
        # сохранение в файл
        with file as f:
            text = "Товары:\n" + self.textEditNew.toPlainText()
            textprice = "\n\nИтог:\n" + self.orderPrice.text() + " р."
            f.write(text)
            f.write(textprice)

        # вывод высплывающего окна
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Информация")
        msg.setText("Заказ оформлен успешно.")
        retButton = msg.addButton("Назад", QMessageBox.AcceptRole)

        msg.exec()

        if msg.clickedButton() == retButton:
            self.orderPrice.clear()
            self.textEditNew.clear()
            self.textEditDiscrip.clear()
            
    def clear_text(self):
        """Метод для очистки всех окон"""
        self.orderPrice.clear()
        self.textEditNew.clear()
        self.textEditDiscrip.clear()

        
def my_excepthook(type, value, tback):
    """Метод для перехвата ошибок"""
    QtWidgets.QMessageBox.critical(
        main, "CRITICAL ERROR", str(value),
        QtWidgets.QMessageBox.Cancel
    )
    sys.__excepthook__(type, value, tback)
 
sys.excepthook = my_excepthook

def main():
    """Метод для выполнения программы"""
    app = QApplication(sys.argv) 
    main = MainWindow()  
    main.show()  
    sys.exit(app.exec_()) 

if __name__ == '__main__':  
    main() 
