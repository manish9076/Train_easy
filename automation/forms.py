from django import forms
from .models import Dataset, Preprocessing, AlgorithmSelection

class DatasetUploadForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['name', 'file']
        
class PreprocessingForm(forms.ModelForm):
    class Meta:
        model = Preprocessing
        fields = ['dataset','normalization', 'encoding', 'imputation', 'feature_selection', 'pca']
        
class AlgorithmSelectionForm(forms.ModelForm):
    class Meta:
        model = AlgorithmSelection
        fields = ['dataset','linear_Regression', 'logistic_Regression', 'decision_Tree', 'random_Forest', 'support_Vector_Machines', 'naive_Bayes']
        
    
        
                