from PySide import QtGui, QtCore


class WCom (QtGui.QWidget):

    """ A communication (radio) widget """

    def __init__(self, parent, radio_number):
        super(WCom, self).__init__(parent)
        self.radio_number = radio_number
        self.radio_name = self.parent().parameters['radios']['own'][self.radio_number]['name'].replace('_','')
        radio_frequency = self.parent().parameters['radios']['own'][self.radio_number]['currentfreq']
        self.radio_index = self.parent().parameters['radios']['own'][self.radio_number]['index']
        self.is_selected = True if self.radio_index == 0 else False
        self.font = self.parent().font

        # Placement and sizes
        self.radio_select_ulx = 85 / 595. * self.parent().width()
        self.radio_name_ulx = 165 / 595. * self.parent().width()
        self.radio_frequency_ulx = 330 / 595. * self.parent().width()
        self.freq_select_ulx = 460 / 595. * self.parent().width()
        self.radio_select_width = self.radio_name_ulx - self.radio_select_ulx
        self.radio_name_width = self.radio_frequency_ulx - self.radio_name_ulx
        self.radio_frequency_width = self.freq_select_ulx - self.radio_frequency_ulx
        self.freq_select_width = 520 / 595. * self.parent().width() - self.freq_select_ulx
        self.radio_height = 40 / 665. * self.parent().height()
        self.uly = self.parent().height() / 2 - (len(self.parent().parameters['radios']['own']) / 2. * (1.5 * self.radio_height)) + (
            self.radio_index * (1.5 * self.radio_height)) + self.parent().upper_margin

        # Objects
        self.radio_select = QtGui.QLabel(self)
        self.radio_select.setFont(self.font)
        self.radio_name_ui = QtGui.QLabel(self)
        self.radio_name_ui.setText(self.radio_name)
        self.radio_name_ui.setFont(self.font)
        self.radio_frequency = QtGui.QLabel(self)
        self.radio_frequency.setText(str(radio_frequency))
        self.radio_frequency.setFont(self.font)
        self.freq_select = QtGui.QLabel(self)
        self.freq_select.setFont(self.font)

        self.radio_select.setGeometry(QtCore.QRect(self.radio_select_ulx, self.uly, self.radio_select_width, self.radio_height))
        self.radio_select.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        self.radio_name_ui.setGeometry(QtCore.QRect(self.radio_name_ulx, self.uly, self.radio_name_width, self.radio_height))
        self.radio_name_ui.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        self.radio_frequency.setGeometry(QtCore.QRect(self.radio_frequency_ulx, self.uly, self.radio_frequency_width, self.radio_height))
        self.radio_frequency.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        self.freq_select.setGeometry(QtCore.QRect(self.freq_select_ulx, self.uly, self.freq_select_width, self.radio_height))
        self.freq_select.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)

    def refreshValues(self):
        self.radio_frequency.setText(
            str(self.parent().parameters['radios']['own'][self.radio_number]['currentfreq']))
        if self.is_selected:
            self.radio_select.setText(u"\u25B2 \u25BC")
            self.freq_select.setText(u"\u25C0 \u25B6")
        else:
            self.radio_select.setText(u"")
            self.freq_select.setText(u"")

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRadio(qp)
        qp.end()

    def drawRadio(self, qp):
        self.radio_select.show()
        self.freq_select.show()
        self.radio_name_ui.show()
        self.radio_frequency.show()
