
class RS(object):

    def changeNumber(self, inValue):
        tempValue = inValue
        while tempValue > 1 or tempValue < -1:
            tempValue = tempValue / 10
        return tempValue

    # def Cal_Rs_ct(self, result):
    #     return (-1.77 * result['original_glcm_DifferenceEntropy'] + 3.61e-3 * result['original_glcm_MaximumProbability']
    #             - 2.68e-2 * result['wavelet-LLH_glcm_DifferenceAverage']
    #             + 0.91 * result['wavelet-LLH_glcm_Id'] + 1.98e-4 *
    #             result['wavelet-LLH_glrlm_RunLengthNonUniformity']
    #             + 0.19 * result['wavelet-LLH_glrlm_HighGrayLevelRunEmphasis']
    #             + 52.00 * result['wavelet-LLH_glrlm_LongRunLowGrayLevelEmphasis']
    #             + 2.90e-4 * result['wavelet-LLH_glrlm_LongRunHighGrayLevelEmphasis'] + 0.71)

    # def Cal_Rs_pet(self, petresult):
    #     return (3.32e-5 * petresult['original_firstorder_Uniformity'] - 2.35e-2 * petresult[
    #         'original_shape_VoxelVolume']
    #             + 3.73e-4 * petresult['original_glcm_DifferenceEntropy'] +
    #             6.85e-3 * petresult['original_glcm_JointEntropy']
    #             - 1.02e-5 * petresult['original_glcm_ClusterTendency'] -
    #             1.30e-3 * petresult['original_glcm_Idmn']
    #             + 0.19 * petresult['original_firstorder_Variance'] -
    #             0.11 * petresult['original_glrlm_RunPercentage']
    #             + 0.52 * petresult['original_glrlm_LongRunHighGrayLevelEmphasis'] - 0.15 * petresult[
    #                 'wavelet-LLH_glcm_JointEnergy']
    #             + 6.88e-3 * petresult['wavelet-LLH_glcm_Imc2'] +
    #             0.72 * petresult['wavelet-LLH_glcm_Imc2']
    #             - 4.24e-3 * petresult['wavelet-LLH_glcm_ClusterTendency'] +
    #             1.23 * petresult['wavelet-LLH_glcm_Idmn']
    #             + 2.25e-4 * petresult['wavelet-LLH_glrlm_RunPercentage'] + 1.37 * petresult[
    #                 'wavelet-LLH_glrlm_ShortRunEmphasis'] - 1.54)

    # def Cal_Rs_two(self, result, petresult):
    #     return (2.79e-5 * petresult['original_firstorder_Uniformity'] + 5.68e-4 * petresult[
    #         'original_glcm_DifferenceEntropy']
    #             + 0.18 * petresult['original_firstorder_Variance'] -
    #             9.98e-2 * petresult['original_glrlm_RunPercentage']
    #             + self.changeNumber(0.59 * petresult['original_glrlm_LongRunHighGrayLevelEmphasis']) - 6.96e-2 * petresult[
    #                 'wavelet-LLH_glcm_JointEnergy']
    #             + 6.20e-3 * petresult['wavelet-LLH_glcm_Imc2'] +
    #             0.53 * petresult['wavelet-LLH_glcm_Imc2']
    #             - 3.72e-4 * petresult['wavelet-LLH_glcm_ClusterTendency'] +
    #             0.26 * petresult['wavelet-LLH_glcm_Idmn']
    #             + 1.42e-4 * petresult['wavelet-LLH_glrlm_RunPercentage'] - self.changeNumber(0.92 * result[
    #                 'original_glcm_DifferenceEntropy']) +
    #             4.63e-4 * result['original_glcm_MaximumProbability'] + 4.91e-5 * result[
    #                 'wavelet-LLH_glrlm_RunLengthNonUniformity'] - 0.48)
    def Cal_Rs_two(self, result, petresult):

        return (result['square_glszm_SizeZoneNonUniformityNormalized']*0.071103+
                result['wavelet-LHH_gldm_DependenceNonUniformityNormalized']*0.091237+
                petresult['lbp-2D_glrlm_ShortRunLowGrayLevelEmphasis']*0.101662
                +petresult['lbp-2D_glrlm_ShortRunEmphasis']*0.003222+
                petresult['lbp-2D_gldm_GrayLevelVariance']*(-0.003286)+
                petresult['original_glcm_MaximumProbability']* 0.037816+
                petresult['lbp-2D_gldm_SmallDependenceLowGrayLevelEmphasis']*0.074111+
                petresult['lbp-2D_glcm_DifferenceVariance']*0.253524+
                result['wavelet-HHL_firstorder_Skewness']*0.141952+
                petresult['lbp-2D_firstorder_Variance']*(-0.311782)+
                result['wavelet-HHL_gldm_DependenceNonUniformityNormalized']*0.054750+
                petresult['gradient_firstorder_Kurtosis']*0.076734)

    def Cal_Rs_two_fake(self, result, petresult):
        return (2.79e-5 * petresult['original_firstorder_Uniformity'] + 5.68e-4 * petresult[
            'original_glcm_DifferenceEntropy']
                + 0.18 * petresult['original_firstorder_Variance'] -
                9.98e-2 * petresult['original_glrlm_RunPercentage']
                + self.changeNumber(0.59 * petresult['original_glrlm_LongRunHighGrayLevelEmphasis']) - 6.96e-2 *
                petresult[
                    'wavelet-LLH_glcm_JointEnergy']
                + 6.20e-3 * petresult['wavelet-LLH_glcm_Imc2'] +
                0.53 * petresult['wavelet-LLH_glcm_Imc2']
                - 3.72e-4 * petresult['wavelet-LLH_glcm_ClusterTendency'] +
                0.26 * petresult['wavelet-LLH_glcm_Idmn']
                + 1.42e-4 * petresult['wavelet-LLH_glrlm_RunPercentage'] - self.changeNumber(0.92 * result[
                    'original_glcm_DifferenceEntropy']) +
                4.63e-4 * result['original_glcm_MaximumProbability'] + 4.91e-5 * result[
                    'wavelet-LLH_glrlm_RunLengthNonUniformity'] - 0.48)