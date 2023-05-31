import numpy as np
import SimpleITK as sitk
# import os

class Seg(object):
    def getSegList(self, mask):
        """
        :param mask: A string to mask file.
        :return: segList
        """
        maskImage = sitk.ReadImage(mask)

        maskArray = sitk.Cast(maskImage, sitk.sitkInt8)
        maskArray = sitk.GetArrayFromImage(maskArray)

        judge = np.where(maskArray == 1)

        x1 = np.min(judge[0])
        x2 = np.max(judge[0])

        y1 = np.min(judge[1])
        y2 = np.max(judge[1])

        z1 = np.min(judge[2])
        z2 = np.max(judge[2])
        return x1, x2, y1, y2, z1, z2

    def segMaskImage(self, fileSrting, segList):
        maskdata = sitk.ReadImage(fileSrting)

        maskArray = sitk.GetArrayFromImage(maskdata)

        x1 = segList[0]
        x2 = segList[1]
        y1 = segList[2]
        y2 = segList[3]
        z1 = segList[4]
        z2 = segList[5]

        mask_array = maskArray[x1:x2 + 1, y1:y2 + 1, z1:z2 + 1]

        mask_array = sitk.GetImageFromArray(mask_array)
        mask_array.SetOrigin(maskdata.GetOrigin())
        mask_array.SetSpacing(maskdata.GetSpacing())
        mask_array.SetDirection(maskdata.GetDirection())

        return mask_array
        #For the need to save the file
        # path = os.getcwd()
        # sitk.WriteImage(mask_array, path + '/mask.nii')

    def segImage(self, fileSrting, segList):
        maskdata = sitk.ReadImage(fileSrting)

        maskArray = sitk.Cast(maskdata, sitk.sitkFloat32)
        maskArray = sitk.GetArrayFromImage(maskArray)

        x1 = segList[0]
        x2 = segList[1]
        y1 = segList[2]
        y2 = segList[3]
        z1 = segList[4]
        z2 = segList[5]

        mask_array = maskArray[x1:x2 + 1, y1:y2 + 1, z1:z2 + 1]

        mask_array = sitk.GetImageFromArray(mask_array)
        mask_array.SetOrigin(maskdata.GetOrigin())
        mask_array.SetSpacing(maskdata.GetSpacing())
        mask_array.SetDirection(maskdata.GetDirection())

        return mask_array
        #For the need to save the file
        # path = os.getcwd()
        # sitk.WriteImage(mask_array, path + '/' + name + '.nii')
# y_1 = 1 / (1 + np.exp(0.930))
# print(y_1)