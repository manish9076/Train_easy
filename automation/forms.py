from django import forms
<<<<<<< HEAD
from .models import Dataset, Preprocessing, AlgorithmSelection
=======
>>>>>>> 0279efee633acf3f0b980c4b736ceca10c994581
from .models import Dataset, Preprocessing, AlgorithmSelection, MetricSelection, Training

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
<<<<<<< HEAD
       
=======
        
>>>>>>> 0279efee633acf3f0b980c4b736ceca10c994581
class MetricSelectionForm(forms.ModelForm): 
    class Meta:
        model = MetricSelection
        fields = ['dataset','accuracy', 'mse', 'rmse', 'mae', 'confusion_matrix', 'roc_auc', 'precision', 'recall', 'f1']
<<<<<<< HEAD

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['dataset', 'training_time', 'training_accuracy', 'testing_accuracy', 'split', 'random_state', 'model_path']
           
    
=======
        
class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['dataset', 'training_time' , 'training_accuracy', 'testing_accuracy','split' , 'random_state', 'model_path']  
>>>>>>> 0279efee633acf3f0b980c4b736ceca10c994581
        
