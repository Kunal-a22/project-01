from django.db import models

class category(models.Model):
    Name=models.CharField(max_length=50)

    def __str__(self):
        return self.Name
    
    # show for card name (Bike,Car)
    @staticmethod
    def View_All_Category():
        return category.objects.all()