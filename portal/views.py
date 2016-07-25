# -*- coding: utf-8 -*-

import random

from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Product, Category


def rand():
    return sum([random.randint(20, 50) for i in range(2)])

def index(request):
    category_list = Category.objects.order_by('-category_type')[:5]
    template = loader.get_template('portal/index.html')
    context = {
        'category_list': category_list,
    }
    return HttpResponse(template.render(context, request))


def result(request):
    try:
        product = ""

        category_list = Category.objects.order_by('-category_type')[:5]
        product_list = sorted([
            {'registered': '2016/7/1 12:00', 'brand': 'ナチュリエ', 'Component': ['C0000001', 'C0000002', 'C0000003', 'C0000004', 'C0000005', 'C0000006'], 'product_img': 'P0000001', 'Product': 'スキンコンディショナー', 'id': 'P0000001', 'recommendation': rand()},
            {'registered': '2016/7/1 12:00', 'brand': 'ノーワン', 'Component': ['C0000001', 'C0000002', 'C0000003', 'C0000004', 'C0000005', 'C0000006'], 'product_img': 'P0000002', 'Product': 'ノーワン\u3000ローション８', 'id': 'P0000002', 'recommendation': rand()},
            {'registered': '2016/7/1 12:00', 'brand': '清肌晶', 'Component': ['C0000001', 'C0000002', 'C0000003', 'C0000004', 'C0000005', 'C0000006'], 'product_img': 'P0000003', 'Product': '清肌晶\u3000クリア\u3000ローション', 'id': 'P0000003', 'recommendation': rand()},
            {'registered': '2016/7/1 12:00', 'brand': 'ピュアイオン', 'Component': ['C0000001', 'C0000002', 'C0000003', 'C0000004', 'C0000005', 'C0000006'], 'product_img': 'P0000004', 'Product': 'ピュアイオンローション', 'id': 'P0000004', 'recommendation': rand()},
            {'registered': '2016/7/1 12:00', 'brand': '雪肌精', 'Component': ['C0000001', 'C0000002', 'C0000003', 'C0000004', 'C0000005', 'C0000006'], 'product_img': 'P0000005', 'Product': '薬用\u3000雪肌精', 'id': 'P0000005', 'recommendation': rand()},
            {'registered': '2016/7/1 12:00', 'brand': 'プリモディーネ', 'Component': ['C0000001', 'C0000002', 'C0000003', 'C0000004', 'C0000005', 'C0000006'], 'product_img': 'P0000006', 'Product': 'プリモディーネ シーバムコントロールVCローション', 'id': 'P0000006', 'recommendation': rand()},
            {'registered': '2016/7/1 12:00', 'brand': 'カバーマ ーク', 'Component': ['C0000001', 'C0000002', 'C0000003', 'C0000004', 'C0000005', 'C0000006'], 'product_img': 'P0000007', 'Product': 'プレシャスブライト ローション', 'id': 'P0000007', 'recommendation': rand()}
        ], key=lambda x: x['recommendation'], reverse=True)[:6]
        template = loader.get_template('portal/result.html')
        context = {
            'category_list': category_list,
            'product_list': product_list
        }

    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return HttpResponse(template.render(context, request))
    #return render(request, 'portal/result.html', {'product': product})


def form(request):
    try:
        product = ""

        category_list = Category.objects.order_by('-category_type')[:5]
        template = loader.get_template('portal/form.html')
        context = {
            'category_list': category_list,
        }

    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return HttpResponse(template.render(context, request))
    #return render(request, 'portal/form.html', {'product': product})
