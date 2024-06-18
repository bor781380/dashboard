from django.db import models
from datetime import date

class Shops(models.Model):
    name = models.CharField(max_length=30)


class ProductLine(models.Model):
    name = models.CharField(max_length=30)
    shops = models.ForeignKey(Shops, on_delete=models.CASCADE)
    color = models.IntegerField()
    colorName = models.CharField(max_length=1, default='3')
    planFact = models.DecimalField(decimal_places=2, max_digits=5)
    planFactName = models.CharField(max_length=2, default='ПР')
    margin = models.DecimalField(decimal_places=2, max_digits=5)
    marginName = models.CharField(max_length=2, default='ОС')
    balances = models.DecimalField(decimal_places=2, max_digits=5)
    balancesName = models.CharField(max_length=2, default='НЦ')
    turnover = models.DecimalField(decimal_places=2, max_digits=5)
    turnoverName = models.CharField(max_length=2, default='ОБ')


class SpecialTask(models.Model):
    name = models.CharField(max_length=30)
    planFact = models.DecimalField(decimal_places=2, max_digits=5)
    shops = models.ForeignKey(Shops, on_delete=models.CASCADE)


class Traffic(models.Model):
    shops = models.ForeignKey(Shops, on_delete=models.CASCADE)
    APPG = models.DecimalField(decimal_places=2, max_digits=5)
    count = models.IntegerField()
    planFact = models.DecimalField(decimal_places=2, max_digits=5)


class Checks(models.Model):
    shops = models.ForeignKey(Shops, on_delete=models.CASCADE)
    APPG = models.DecimalField(decimal_places=2, max_digits=5)
    checksRoz = models.IntegerField()
    checksEcom = models.IntegerField()
    partCheckRoz = models.DecimalField(decimal_places=2, max_digits=5)


class Conversion(models.Model):
    shops = models.ForeignKey(Shops, on_delete=models.CASCADE)
    planFact = models.DecimalField(decimal_places=2, max_digits=5)
    conversionFact = models.DecimalField(decimal_places=2, max_digits=5)
    APPG = models.DecimalField(decimal_places=2, max_digits=5)



class ChartSales(models.Model):
    shops = models.ForeignKey(Shops, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    sales = models.DecimalField(decimal_places=2, max_digits=10)
    productLine = models.CharField(max_length=100,default="Проверка")
    planFact = models.DecimalField(decimal_places=4, max_digits=10)
    planDay = models.DecimalField(decimal_places=2, max_digits=10)


class ChartSpecialTask(models.Model):
    shops = models.ForeignKey(Shops, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    specialTask = models.CharField(max_length=30)
    sales = models.DecimalField(decimal_places=2, max_digits=10)
    planFact = models.DecimalField(decimal_places=4, max_digits=10)
    planDay = models.DecimalField(decimal_places=2, max_digits=10)


class MainIndicator(models.Model):
    color_value = models.IntegerField()
    colorPROD = models.IntegerField()
    planFactMI = models.DecimalField(decimal_places=2, max_digits=5)
    colorNAC = models.IntegerField()
    marginMI = models.DecimalField(decimal_places=2, max_digits=5)
    colorOST = models.IntegerField()
    balancesMI = models.DecimalField(decimal_places=2, max_digits=5)
    colorOBOR = models.IntegerField()
    turnoverMI = models.DecimalField(decimal_places=2, max_digits=5)
    colorSPEC = models.IntegerField()
    colorTRAFF = models.IntegerField()
    colorCHECK = models.IntegerField()
    colorCONF = models.IntegerField()