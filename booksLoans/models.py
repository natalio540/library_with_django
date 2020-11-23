from django.db import models

# Create your models here.


class booksTable(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

# class clientsTable(models.Model):
#     name = models.CharField(max_length=50)
#     adress = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50)
#     email = models.EmailField()

#     def __str__(self):s
#         return '{}'.format(self.name)

# class loansTable(models.Model):
#     bookLoan = models.OneToOneField(booksTable,null=True,blank=True,on_delete=models.CASCADE)
#     clientLoan = models.ForeignKey(clientsTable,null=True,blank=True,on_delete=models.CASCADE)
#     dateLoan = models.DateField()
#     dateReturn = models.DateField()
    

