import logging

from django.http import HttpResponse
from django.http import JsonResponse
from .models import ProductLine, Checks, ChartSales, ChartSpecialTask
from .models import SpecialTask, Shops, Traffic, Conversion, MainIndicator
from django.views import View
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)


class SaleProductLine(View):
    def get(self, request):
        try:
            product_lines = ProductLine.objects.all()
        except ProductLine.DoesNotExist:
            return JsonResponse({'error': 'Данные не найдены'}, status=404)

        data = []

        for product_line in product_lines:
            row = [
                product_line.shops.name,
                product_line.name,
                product_line.color,
                product_line.planFact,
                product_line.margin,
                product_line.balances,
                product_line.turnover
            ]
            data.append(row)

        column_names = ['Магазин', 'Продукт', 'Светофор', 'План/Факт', 'Наценка', 'Остатки', 'Оборачиваемость']

        return render(request, 'sale.html', {'data': data, 'column_names': column_names})


class SpecialTaskShops(View):
    def get(self, request):
        try:
            special_tasks = SpecialTask.objects.all()
        except SpecialTask.DoesNotExist:
            return JsonResponse({'error': 'Данные не найдены'}, status=404)

        data = []

        for special_task in special_tasks:
            row = [
                special_task.shops.name,
                special_task.name,
                special_task.planFact,

            ]
            data.append(row)

        column_names = ['Магазин', 'Спецзадача', 'План/Факт']

        return render(request, 'stask.html', {'data': data, 'column_names': column_names})

class TrafficShops(View):
    def get(self, request):
        try:
            traffics = Traffic.objects.all()
        except Traffic.DoesNotExist:
            return JsonResponse({'error': 'Данные не найдены'}, status=404)

        data = []

        for traffic in traffics:
            row = [
                traffic.shops.name,
                traffic.APPG,
                traffic.count,
                traffic.planFact,
            ]
            data.append(row)

        column_names = ['Магазин', 'к АППГ', 'Фактическое количество', 'План/Факт']

        return render(request, 'traffic.html', {'data': data, 'column_names': column_names})

class ChecksShops(View):
    def get(self, request):
        try:
            checks = Checks.objects.all()
        except Checks.DoesNotExist:
            return JsonResponse({'error': 'Данные не найдены'}, status=404)

        data = []

        for check in checks:
            row = [
                check.shops.name,
                check.APPG,
                check.checksRoz,
                check.checksEcom,
                check.partCheckRoz,
            ]
            data.append(row)

        column_names = ['Магазин', 'к АППГ', 'Всего чеков розницы', 'Всего чеков с сайта', 'Доля чеков розницы']

        return render(request, 'check.html', {'data': data, 'column_names': column_names})

class ConversionShops(View):
    def get(self, request):
        try:
            conversions = Conversion.objects.all()
        except Conversion.DoesNotExist:
            return JsonResponse({'error': 'Данные не найдены'}, status=404)

        data = []

        for conversion in conversions:
            row = [
                conversion.shops.name,
                conversion.planFact,
                conversion.conversionFact,
                conversion.APPG,
            ]
            data.append(row)

        column_names = ['Магазин', 'План/Факт', 'Конверсия', 'к АППГ']

        return render(request, 'conversion.html', {'data': data, 'column_names': column_names})

class ChartSalesShops(View):
    def get(self, request):
        try:
            chartsales = ChartSales.objects.all()
        except ChartSales.DoesNotExist:
            return JsonResponse({'error': 'Данные не найдены'}, status=404)

        data = []

        for chartsale in chartsales:
            row = [
                chartsale.shops.name,
                chartsale.date,
                chartsale.sales,
                chartsale.productLine,
                chartsale.planFact,
                chartsale.planDay,
            ]
            data.append(row)

        column_names = ['Магазин', 'Дата', 'Выручка','Товарное направление', 'План/Факт', 'Дневной план']

        return render(request, 'chartsalesshops.html', {'data': data, 'column_names': column_names})


class ChartSpecialTaskShops(View):
    def get(self, request):
        try:
            chartspecialsales = ChartSpecialTask.objects.all()
        except ChartSpecialTask.DoesNotExist:
            return JsonResponse({'error': 'Данные не найдены'}, status=404)

        data = []

        for chartspecialsale in chartspecialsales:
            row = [
                chartspecialsale.shops.name,
                chartspecialsale.date,
                chartspecialsale.sales,
                chartspecialsale.specialTask,
                chartspecialsale.planFact,
                chartspecialsale.planDay,
            ]
            data.append(row)

        column_names = ['Магазин', 'Дата', 'Выручка','Спец.задача', 'План/Факт', 'Дневной план']

        return render(request, 'chartspecsalesshops.html', {'data': data, 'column_names': column_names})

class MainIndicatorShops(View):
    def get(self, request):
        try:
            mainindicators = MainIndicator.objects.all()
        except MainIndicator.DoesNotExist:
            return JsonResponse({'error': 'Данные не найдены'}, status=404)

        data = []

        for mainindicator in mainindicators:
            row = [
                mainindicator.color_value,
                mainindicator.colorPROD,
                mainindicator.planFactMI,
                mainindicator.colorNAC,
                mainindicator.marginMI,
                mainindicator.colorOST,
                mainindicator.balancesMI,
                mainindicator.colorOBOR,
                mainindicator.turnoverMI,
                mainindicator.colorSPEC,
                mainindicator.colorTRAFF,
                mainindicator.colorCHECK,
                mainindicator.colorCONF,
            ]
            data.append(row)

        column_names = ['Итоговый светофор', 'Цвет ПРОД', 'ПРОД','Цвет НАЦ', 'НАЦ', 'Цвет ОСТ', 'ОСТ',
                        'Цвет ОБОР', 'ОБОР', 'Цвет СПЕЦ', 'Цвет ТРАФИК', 'Цвет Чеки', 'Цвет КОНВ']

        return render(request, 'mainindicator.html', {'data': data, 'column_names': column_names})