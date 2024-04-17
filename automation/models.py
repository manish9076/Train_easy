from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# preprocesing model that lets user to select preprocessing steps
class Preprocessing(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    normalization = models.BooleanField(default=False)
    encoding = models.BooleanField(default=False)
    imputation = models.BooleanField(default=False)
    feature_selection = models.BooleanField(default=False)
    pca = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.dataset.name} - {self.created_at}'


class AlgorithmSelection(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    linear_Regression = models.BooleanField(default=False)
    logistic_Regression = models.BooleanField(default=False)
    decision_Tree = models.BooleanField(default=False)
    random_Forest = models.BooleanField(default=False)
    support_Vector_Machines = models.BooleanField(default=False)        
    naive_Bayes = models.BooleanField(default=False)        

    def __str__(self):
        return f'{self.dataset.name} - {self.created_at}'
    
    

    

