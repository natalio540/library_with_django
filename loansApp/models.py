from django.db import models
from booksLoans.models import booksTable
from ClientsLoans.models import clientsTable

# Create your models here.

    


class loansTable(models.Model):
    bookLoan = models.OneToOneField(booksTable,null=True,blank=True,on_delete=models.CASCADE)
    clientLoan = models.ForeignKey(clientsTable,null=True,blank=True,on_delete=models.CASCADE)
    dateLoan = models.DateField()
    dateReturn = models.DateField()
    status = models.CharField(max_length=10,default='borrowed')

    def __str__(self):
        return '{}'.format(self.bookLoan,self.clientLoan,self.status)