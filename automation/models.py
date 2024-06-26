from django.db import models


class Dataset(models.Model):
    name = models.CharField(max_length=255, help_text='Automation Project Name', default='AutoMate Project')
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
    
class MetricSelection(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    accuracy = models.BooleanField(default=False, help_text="for regression & classification")
    mse = models.BooleanField(default=False, help_text="for regression")
    rmse = models.BooleanField(default=False, help_text="for regression")
    mae = models.BooleanField(default=False, help_text="for regression")
    
    confusion_matrix = models.BooleanField(default=False, help_text="for classification")
    roc_auc = models.BooleanField(default=False, help_text="for classification")
    precision = models.BooleanField(default=False, help_text="for classification")
    recall = models.BooleanField(default=False, help_text="for classification")
    f1 = models.BooleanField(default=False, help_text="for classification")
<<<<<<< HEAD
=======
    
    def __str__(self):
        return f'{self.dataset.name} - {self.created_at}'
    
    
class Training(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    metric = models.ForeignKey(MetricSelection, on_delete=models.CASCADE)
    algo = models.ForeignKey(AlgorithmSelection, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    training_time = models.FloatField(default=0.0)
    training_accuracy = models.FloatField(default=0.0)
    testing_accuracy = models.FloatField(default=0.0)
    split = models.FloatField(default=.2, help_text="default 80% train - 20% test split")
    random_state = models.IntegerField(default=42, help_text="random state for splitting the data")
    model_path = models.FileField(upload_to='models/', help_text="path to save the model",blank=True, null=True)
    
    def __str__(self):
        return f'{self.dataset.name} - {self.created_at}'
    
class Visualizations(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    model = models.ForeignKey(Training, on_delete=models.CASCADE)
    metric = models.ForeignKey(MetricSelection, on_delete=models.CASCADE)
    algo = models.ForeignKey(AlgorithmSelection, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    plot = models.ImageField(upload_to='plots/')
    
    def __str__(self):
        return f'{self.dataset.name} - {self.created_at}'

>>>>>>> 0279efee633acf3f0b980c4b736ceca10c994581
    
    def __str__(self):
        return f'{self.dataset.name} - {self.created_at}'
    
    
class Training(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    metric = models.ForeignKey(MetricSelection, on_delete=models.CASCADE)
    algo = models.ForeignKey(AlgorithmSelection, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    training_time = models.FloatField(default=0.0)
    training_accuracy = models.FloatField(default=0.0)
    testing_accuracy = models.FloatField(default=0.0)
    split = models.FloatField(default=.2, help_text="default 80% train - 20% test split")
    random_state = models.IntegerField(default=42, help_text="random state for splitting the data")
    model_path = models.FileField(upload_to='models/', help_text="path to save the model",blank=True, null=True)
    
    def __str__(self):
        return f'{self.dataset.name} - {self.created_at}'
    
class Visualizations(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    model = models.ForeignKey(Training, on_delete=models.CASCADE)
    metric = models.ForeignKey(MetricSelection, on_delete=models.CASCADE)
    algo = models.ForeignKey(AlgorithmSelection, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    plot = models.ImageField(upload_to='plots/')
    
    def __str__(self):
        return f'{self.dataset.name} - {self.created_at}'

    