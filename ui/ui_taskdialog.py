# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskdialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TaskDialog(object):
    def setupUi(self, TaskDialog):
        TaskDialog.setObjectName(_fromUtf8("TaskDialog"))
        TaskDialog.resize(588, 222)
        TaskDialog.setAutoFillBackground(False)
        self.gridLayout_2 = QtGui.QGridLayout(TaskDialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(TaskDialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lstAvailableResources = QtGui.QListWidget(self.groupBox_2)
        self.lstAvailableResources.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lstAvailableResources.setObjectName(_fromUtf8("lstAvailableResources"))
        self.gridLayout_3.addWidget(self.lstAvailableResources, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.edtTaskName = QtGui.QLineEdit(self.groupBox)
        self.edtTaskName.setObjectName(_fromUtf8("edtTaskName"))
        self.gridLayout_5.addWidget(self.edtTaskName, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.cmbTaskPriority = QtGui.QComboBox(self.groupBox)
        self.cmbTaskPriority.setObjectName(_fromUtf8("cmbTaskPriority"))
        self.gridLayout_5.addWidget(self.cmbTaskPriority, 1, 1, 1, 1)
        self.spbTaskTime = QtGui.QSpinBox(self.groupBox)
        self.spbTaskTime.setAlignment(QtCore.Qt.AlignCenter)
        self.spbTaskTime.setMinimum(1)
        self.spbTaskTime.setMaximum(300)
        self.spbTaskTime.setProperty("value", 3)
        self.spbTaskTime.setObjectName(_fromUtf8("spbTaskTime"))
        self.gridLayout_5.addWidget(self.spbTaskTime, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 3, 1, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.btnAdd = QtGui.QPushButton(self.groupBox)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.gridLayout_6.addWidget(self.btnAdd, 0, 1, 1, 1)
        self.btnCancel = QtGui.QPushButton(self.groupBox)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.gridLayout_6.addWidget(self.btnCancel, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 8, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 5, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 2, 1, 1)

        self.retranslateUi(TaskDialog)
        QtCore.QObject.connect(self.btnAdd, QtCore.SIGNAL(_fromUtf8("clicked()")), TaskDialog.accept)
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), TaskDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TaskDialog)

    def retranslateUi(self, TaskDialog):
        TaskDialog.setWindowTitle(_translate("TaskDialog", "Добавить процесс", None))
        self.groupBox_2.setTitle(_translate("TaskDialog", "Ресурсы", None))
        self.lstAvailableResources.setSortingEnabled(False)
        self.label_2.setText(_translate("TaskDialog", "Приоритет:", None))
        self.label_3.setText(_translate("TaskDialog", "Время выполнения:", None))
        self.label.setText(_translate("TaskDialog", "Название:", None))
        self.btnAdd.setText(_translate("TaskDialog", "Добавить", None))
        self.btnCancel.setText(_translate("TaskDialog", "Отменить", None))

