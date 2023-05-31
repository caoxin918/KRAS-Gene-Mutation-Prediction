from PyQt5 import QtWidgets, QtGui
import os
from gui.UI import Ui_Dialog
import sys
from decimal import *#为了避免浮点数精确度不够，必须用decimal
import numpy as np
from PyQt5.QtWidgets import QApplication
from radiomics import featureextractor
from rs import RS
from seg import Seg
import pandas as pd
from sklearn import preprocessing
class myMainWindow(QtWidgets.QMainWindow, Ui_Dialog):

    def __init__(self):
        super(myMainWindow, self).__init__()
        self.setupUi(self)

        self.CTImage = ''
        self.PETImage = ''
        self.maskImage = ''

        self.ct.clicked.connect(self.readCT)
        self.pet.clicked.connect(self.readPet)
        self.mask.clicked.connect(self.readMask)
        self.calculate.clicked.connect(self.run)


        self.show()

    def readCT(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(
            None, "选择CT文件",
            "F:/medicalImaging/FirstProject/", "*.nii;*.nrrd")
        self.CTImage = file_name[0]
        print(file_name)

    def readPet(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(
            None, "选择PET文件",
            "F:/medicalImaging/FirstProject/", "*.nii;*.nrrd")
        self.PETImage = file_name[0]
        print(file_name)

    def readMask(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(
            None, "选择MASK文件",
            "F:/medicalImaging/FirstProject/", "*.nii;*.nrrd")
        self.maskImage = file_name[0]
        print(file_name)



    def run(self):
        if self.CTImage=='' or self.PETImage=='' or self.maskImage=='':
            return

        cal = RS()
        SEG = Seg()

        mask = self.maskImage
        ct = self.CTImage
        pet = self.PETImage

        sl = SEG.getSegList(mask)
        maskImage = SEG.segMaskImage(mask, sl)
        ctImage = SEG.segImage(ct, sl)
        petImage = SEG.segImage(pet, sl)

        base = path = os.getcwd()
        yaml_pet = base + '/pet_parameters.yaml'
        yaml_ct = base + '/ct_parameters.yaml'

        extractor_pet = featureextractor.RadiomicsFeatureExtractor(yaml_pet)
        extractor_ct = featureextractor.RadiomicsFeatureExtractor(yaml_ct)

        extractor_pet.enableImageTypeByName('Wavelet')

        petresult = extractor_pet.execute(petImage, maskImage)
        result = extractor_ct.execute(ctImage, maskImage)
        print(type(result))
        # standard_scaler = preprocessing.StandardScaler()
        # result = standard_scaler.fit_transform(result)
        # petresult = standard_scaler.fit_transform(petresult)
        # RS_CT = cal.Cal_Rs_ct(result)
        # RS_PET = cal.Cal_Rs_pet(petresult)
        RS_CT_PET = cal.Cal_Rs_two(result, petresult)
        RS_CT_PET_fake = cal.Cal_Rs_two_fake(result, petresult)

        _age=int(self.age.value())
        #_diagnosis=int(self.diagnosis.currentText())
        _diagnosis=0
        _gender=int(self.gender.currentText())
        _manual=int(self.manual.currentText())
        # print(RS_CT_PET,_age,_diagnosis,_gender,_manual)
        hybridResult=sigmoidOfPCM(age=_age,manualDiagnosis=_manual,pathologyDiagnosis=_diagnosis,gender=_gender,petct_rs=RS_CT_PET)
        '''
        new
        '''
        hybridResult_=sigmoidOfPCM_EGFR(age=_age,manualDiagnosis=_manual,pathologyDiagnosis=_diagnosis,gender=_gender,petct_rs=RS_CT_PET)
        hybridResult_fake=sigmoidOfPCM_fake(age=_age,manualDiagnosis=_manual,pathologyDiagnosis=_diagnosis,gender=_gender,petct_rs=RS_CT_PET_fake)
        # print(hybridResult)
        '''
        new
        '''

        if float(hybridResult) > 0.4819828043880051:
            kras='kras未突变|'
        else:
            kras = 'kras突变|'
        if float(hybridResult_) > 0.4819828043880051:
            egfr='egfr未突变'
        else:
            egfr = 'egfr突变'

        self.result.setText('未突变' if float(hybridResult) > 0.4819828043880051 else '突变')
        self.result_2.setText( '未突变' if float(hybridResult_)>0.28292471450702744 else'突变')
        self.result.setText(kras+egfr)
        self.result_2.setText('良性' if float(hybridResult)<0.717926666666667 else'恶性')
    def closeEvent(self, a0: QtGui.QCloseEvent):
        reply = QtWidgets.QMessageBox.question(self,
                                               '终止程序',
                                               '退出？',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()

def sigmoidOfPCM(age,manualDiagnosis,pathologyDiagnosis,gender,petct_rs):#用于计算最终的混合指标=petct+人工判断结果
    y = Decimal(6.1937) * Decimal(petct_rs) +Decimal(0.0606)
    y_1 = 1 / (1 + np.exp(-y))
    y_2 = format(y_1, '.7f')  # 跟表格一样，保留7位小数
    return y_2

def sigmoidOfPCM_EGFR(age,manualDiagnosis,pathologyDiagnosis,gender,petct_rs):#用于计算最终的混合指标=petct+人工判断结果
    y = Decimal(-3.5369) * Decimal(petct_rs) +Decimal(-1.3767)
    y_1 = 1 / (1 + np.exp(-y))
    y_2 = format(y_1, '.7f')  # 跟表格一样，保留7位小数
    return y_2
def sigmoidOfPCM_fake(age,manualDiagnosis,pathologyDiagnosis,gender,petct_rs):#文献公式
    y = Decimal( 5.9589) * Decimal(petct_rs) + Decimal(3.1895) * Decimal(manualDiagnosis) + Decimal(-2.4097)
    y_1 = 1 / (1 + np.exp(-y))
    y_2 = format(y_1, '.7f')  # 跟表格一样，保留7位小数
    return y_2

'''
new
'''
# def mixedRsCalc(age,manualDiagnosis,pathologyDiagnosis,gender,petct_rs):
#     y = Decimal(6.3750) * Decimal(petct_rs)+Decimal(-0.3521)
#     y_1 = 1 / (1 + np.exp(-y))
#     y_2 = format(y_1, '.7f')  # 跟表格一样，保留7位小数
#     return y_2



if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = myMainWindow()
    sys.exit(app.exec_())