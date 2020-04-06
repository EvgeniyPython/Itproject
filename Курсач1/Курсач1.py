
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Buy:
    def buy(self):
        self.buy = 2
        
while True:
 

 class HideorShow:     
    def hide_log(self): #hide_log_el
        self.ui.Pass.hide()
        self.ui.User.hide()
        self.ui.Sign.hide()       

    def show_log(self): #show_log_el
        self.ui.Pass.show()
        self.ui.User.show()
        self.ui.Sign.show()

    def hide_2(self): #hide lineedit
        self.ui.User_2.hide()
        self.ui.Pass_2.hide()
        self.ui.Number.hide()
        
    def show_2(self): #show lineedit
        self.ui.User_2.show()
        self.ui.Pass_2.show()
        self.ui.Number.show()

    def showHead(self): #showCarDelivery
        self.ui.car.setPixmap(QtGui.QPixmap('Group 85.png'))
        self.ui.delivery.setPixmap(QtGui.QPixmap('Delivery.png'))
        self.ui.shop.setPixmap(QtGui.QPixmap('ant-design_shopping-outlined.png'))
        self.ui.delivery.mousePressEvent = self.delivery
        self.ui.car.mousePressEvent = self.catalog
        self.ui.car.show()
        self.ui.delivery.show()
        self.ui.shop.show()

    def hideHead(self): #hideCarDelivery
        self.ui.car.hide()
        self.ui.delivery.hide()
        self.ui.shop.hide()

    def car_hide(self): #hideCar el.
        self.ui.character.hide()
        self.ui.Appearance.hide()
        self.ui.back.hide()
        self.ui.carEdit.hide()

    def rims_hide(self): #hideRims        
        self.ui.stock.hide()
        self.ui.rims2.hide()
        self.ui.rims3.hide()

    def rims_show(self): #ShowRims
        self.ui.carEdit.show()
        self.ui.stock.show()
        self.ui.rims2.show()
        self.ui.rims3.show()        

    def carChar_Show(self): #show char car(stage)
        self.ui.stockCh.show()
        self.ui.stage1.show()
        self.ui.stage2.show()
    
    def carChar_Hide(self): #hide char car(stage)
        self.ui.stockCh.hide()
        self.ui.stage1.hide()
        self.ui.stage2.hide()

    def hideBuy(self): #hide buy el.
        self.ui.price.hide()
        self.ui.total.hide()
        self.ui.accept.hide()

 """ Class for buying a car """
 class Cart(Buy): 
     """ Func for basket """  
     def cart(self, event):
         self.ui.x5.hide()
         self.ui.main.setPixmap(QtGui.QPixmap('Frame 57.png'))
         self.ui.shop.setPixmap(QtGui.QPixmap('shopClick.png'))
         self.ui.delivery.setPixmap(QtGui.QPixmap('Delivery.png'))
         self.ui.car.setPixmap(QtGui.QPixmap('CarsNO.png'))
         self.ui.carEdit.hide()
         self.ui.buy.hide()
         self.carChar_Hide()
         self.rims_hide()
         self.car_hide()
         if self.buy == 1:
             self.ui.accept.show()    
             self.ui.price.show()
             self.ui.price.setText(self.price)
             self.ui.total.show()
             self.ui.total.setText(self.total)
             self.ui.accept.setPixmap(QtGui.QPixmap('bmwbuy.png')) 
             self.rims_hide()
             self.car_hide()
             self.ui.x5.hide()
             self.carChar_Hide()
             self.ui.buy.hide()        
         else:
             pass
     def showForBuy(self, event):
         self.buy = 1

 """ Class for delivery """
 class Delivery:
     """ Func for delivery """  
     def delivery(self, event):
         self.hideBuy()
         self.ui.buy.hide()
         self.carChar_Hide()
         self.ui.exit.show()
         self.ui.exit.mousePressEvent = self.login
         self.ui.exit.setPixmap(QtGui.QPixmap('exit.png'))
         self.rims_hide()
         self.car_hide()
         self.ui.x5.hide()
         self.ui.carEdit.hide()
         self.ui.main.setPixmap(QtGui.QPixmap('Frame 58.png'))
         self.ui.shop.setPixmap(QtGui.QPixmap('ant-design_shopping-outlined.png'))
         self.ui.delivery.setPixmap(QtGui.QPixmap('DeliveryYES.png'))
         self.ui.car.setPixmap(QtGui.QPixmap('CarsNO.png'))
 """ Class for car """
 class Car:
     """ Func for car """  
     def car(self, event):
         self.ui.stock.setPixmap(QtGui.QPixmap('stockYES.png'))
         self.ui.rims3.setPixmap(QtGui.QPixmap('3NO.png'))
         self.ui.rims2.setPixmap(QtGui.QPixmap('2NO.png'))
         self.ui.back.setPixmap(QtGui.QPixmap('butt.png'))
         self.price = '      $0'
         self.total = '$130 000'
         self.hideBuy()
         self.ui.buy.show()
         self.carChar_Hide()
         self.ui.exit.hide()
         self.showHead()
         self.ui.carEdit.show()
         self.ui.carEdit.setPixmap(QtGui.QPixmap('stock.png'))
         self.rims_show()
         self.ui.back.show()
         self.ui.back.mousePressEvent = self.catalog
         self.ui.x5.hide()
         self.ui.character.show()         
         self.ui.character.setPixmap(QtGui.QPixmap('Characteristics.png'))
         self.ui.main.setPixmap(QtGui.QPixmap('car.png'))
         self.ui.Appearance.hide()
         self.ui.character.mousePressEvent = self.car_characher         
         self.ui.stock.mousePressEvent = self.stock
         self.ui.rims2.mousePressEvent = self.rims2
         self.ui.rims3.mousePressEvent = self.rims3
         self.ui.buy.mousePressEvent = self.showForBuy        

     """ Func rims2 for car. """  
     def rims2(self, event):
         self.ui.carEdit.setPixmap(QtGui.QPixmap('2 bmw.png'))
         self.ui.stock.setPixmap(QtGui.QPixmap('stockNO.png'))
         self.ui.rims2.setPixmap(QtGui.QPixmap('2YES.png'))
         self.ui.rims3.setPixmap(QtGui.QPixmap('3NO.png'))
         self.ui.stock.mousePressEvent = self.stock
         self.ui.rims3.mousePressEvent = self.rims3

     """ Func stock rims for car. """  
     def stock(self, event):
         self.ui.carEdit.setPixmap(QtGui.QPixmap('stock.png'))
         self.ui.stock.setPixmap(QtGui.QPixmap('stockYES.png'))
         self.ui.rims2.setPixmap(QtGui.QPixmap('2NO.png'))
         self.ui.rims3.setPixmap(QtGui.QPixmap('3NO.png'))
         self.ui.rims2.mousePressEvent = self.rims2
         self.ui.rims3.mousePressEvent = self.rims3
 
     """ Func rims3 for car. """  
     def rims3(self, event):
         self.ui.carEdit.setPixmap(QtGui.QPixmap('dark.png'))
         self.ui.stock.setPixmap(QtGui.QPixmap('stockNO.png'))
         self.ui.rims2.setPixmap(QtGui.QPixmap('2NO.png'))
         self.ui.rims3.setPixmap(QtGui.QPixmap('3YES.png'))
         self.ui.rims2.mousePressEvent = self.rims2
         self.ui.stock.mousePressEvent = self.stock

     """ Func for car character. """         
     def car_characher(self, event):
         self.ui.stockCh.setPixmap(QtGui.QPixmap('stockCharYES.png'))
         self.ui.stage1.setPixmap(QtGui.QPixmap('Stage1NO.png'))
         self.ui.stage2.setPixmap(QtGui.QPixmap('Stage2NO.png'))
         self.ui.exit.hide()
         self.carChar_Show()
         self.rims_hide()         
         self.ui.back.mousePressEvent = self.catalog
         self.ui.character.setPixmap(QtGui.QPixmap('char.png'))
         self.ui.Appearance.show()
         self.ui.main.setPixmap(QtGui.QPixmap('car char.png'))
         self.ui.Appearance.mousePressEvent = self.car
         self.ui.stockCh.mousePressEvent = self.stock1
         self.ui.stage1.mousePressEvent = self.stage1
         self.ui.stage2.mousePressEvent = self.stage2

     """ Func for stock in car character. """  
     def stock1(self, event):
         self.ui.stockCh.setPixmap(QtGui.QPixmap('stockCharYES.png'))
         self.ui.stage1.setPixmap(QtGui.QPixmap('Stage1NO.png'))
         self.ui.stage2.setPixmap(QtGui.QPixmap('Stage2NO.png'))
         self.ui.stage1.mousePressEvent = self.stage1
         self.ui.stage2.mousePressEvent = self.stage2
         self.price = '0'
         self.total = '$130 000'

     """ Func for STAGE1 in car character. """         
     def stage1(self, event):
         self.ui.stockCh.setPixmap(QtGui.QPixmap('stockCharNO.png'))
         self.ui.stage1.setPixmap(QtGui.QPixmap('Stage1YES.png'))
         self.ui.stage2.setPixmap(QtGui.QPixmap('Stage2NO.png'))
         self.ui.stockCh.mousePressEvent = self.stock1
         self.ui.stage2.mousePressEvent = self.stage2
         self.price = '$1000'
         self.total = '$131 000'
     """ Func for STAGE2 in car character. """       
     def stage2(self, event):
         self.ui.stage2.setPixmap(QtGui.QPixmap('Stage2YES.png'))
         self.ui.stage1.setPixmap(QtGui.QPixmap('Stage1NO.png'))
         self.ui.stockCh.setPixmap(QtGui.QPixmap('stockCharNO.png'))
         self.ui.stockCh.mousePressEvent = self.stock1
         self.ui.stage1.mousePressEvent = self.stage1
         self.price = '$1500'
         self.total = '$131 500'

 """ Class for catalog """
 class Catalog(Car, Delivery, Cart):
     def catalog(self, event):
         self.ui.error.hide()
         self.hideBuy()
         self.ui.accept.hide()
         self.ui.buy.hide()
         self.carChar_Hide()
         self.ui.shop.mousePressEvent =  self.cart
         self.ui.exit.hide()
         self.rims_hide()
         self.ui.main.setPixmap(QtGui.QPixmap('cat.png'))
         self.car_hide()
         self.hide_log()
         self.showHead()
         self.ui.carEdit.hide()
         self.ui.x5.setPixmap(QtGui.QPixmap('bmw.png'))
         self.ui.x5.show()
         self.ui.error.hide()
         self.ui.StartButton.hide()
         self.ui.x5.mousePressEvent = self.car
        
 """ Main class """
 class Sign_in(Catalog, HideorShow):
    def __init__(self):
        self.ui = uic.loadUi('qt.ui')
        self.ui.main.setPixmap(QtGui.QPixmap('First.png'))
        self.ui.StartButton.clicked.connect(self.login)    
        self.hide_log()
        self.ui.show()
        self.hide_2()
        self.hideHead()
        self.ui.error.hide()
        self.ui.x5.hide()
        self.car_hide()        
        self.rims_hide()
        self.ui.exit.hide()
        self.ui.buy.hide()
        self.carChar_Hide()
        self.ui.accept.hide()
        self.ui.price.hide()
        self.ui.total.hide()
    """ Funf for check username and password  """
    def admin(self):
        self.text1 = self.ui.User.text()
        self.text2 = self.ui.Pass.text()
        self.text3 = self.ui.User_2.text()
        self.text4 = self.ui.Pass_2.text()
        if self.text1 and self.text2 == 'admin':
            self.ui.Sign.clicked.connect(self.catalog)
        else:
            self.ui.error.show()
        if self.text1 in self.log:
            if self.text2 in self.passw:
             self.ui.Sign.clicked.connect(self.catalog)

    """Func for login"""
    def login(self, event):
        self.hideHead()
        self.ui.x5.hide()
        self.ui.exit.hide()
        self.ui.User.show()
        self.ui.Pass.show()
        self.show_log()
        self.hide_2()
        self.new_user = self.ui.User_2.text()
        self.new_pass = self.ui.Pass_2.text()
        self.passw = []
        self.log = []
        self.passw.append(self.new_pass)
        self.log.append(self.new_user)
        self.ui.Sign.setGeometry(QtCore.QRect(773, 550, 330, 50))
        self.ui.main.setPixmap(QtGui.QPixmap('sign.png'))
        self.ui.StartButton.setGeometry(QtCore.QRect(180, 428, 150, 40))
        self.ui.StartButton.clicked.connect(self.register)
        self.ui.Sign.clicked.connect(self.admin) #TYT

    """Func for register"""
    def register(self):
        self.ui.exit.hide()
        self.ui.error.hide()
        self.show_2()
        self.ui.User.hide()
        self.ui.Pass.hide()
        self.ui.Number.show()
        self.ui.Sign.setGeometry(QtCore.QRect(262, 587, 330, 50))
        self.ui.main.setPixmap(QtGui.QPixmap('reg.png'))
        self.ui.StartButton.setGeometry(QtCore.QRect(1036, 428, 150, 40))
        self.ui.StartButton.clicked.connect(self.login)
        self.ui.Sign.clicked.connect(self.login) 



 if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Sign_in()
    sys.exit(app.exec_())  
