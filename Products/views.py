from unicodedata import category
from django.http import Http404, HttpResponse
from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Products.models import *
from Products.serializers import *
from rest_framework import viewsets
#from django.core.mail import send_mail

from django.core.files.storage import default_storage
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.views import APIView

method_decorator(csrf_protect)
# Create your views here.


@csrf_exempt
def Crud_Product(request, id=0):
    if request.method == 'GET':
        products = T_Product.objects.all()
        products_serializer = S_Product(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        print(product_data)
        test = T_Product.objects.filter(Prod_Name=product_data['Prod_Name'])
        prod = S_Product(test, many=True)
        for i in prod.data:
            if (product_data["Prod_Name"] == i['Prod_Name']):
                print(i)
                return JsonResponse("you have already this product", safe=False)
        products_serializer = S_Product(data=product_data)
       # print(products_serializer.data)
        if products_serializer.is_valid():
            products_serializer.save()

            return JsonResponse(products_serializer.data, safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product = T_Product.objects.get(Prod_Id=id)
        products_serializer = S_Product(
            product, data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        product = T_Product.objects.get(Prod_Id=id)
        product.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def get_Product_ById(request, prodId):
    try:
        product = T_Product.objects.filter(Prod_Id=prodId)
        if request.method == 'GET':
            serializer = S_Product(product, many=True)
            return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponse(status=404)


@csrf_exempt
def get_Product_ByCateg(request, Id):
    try:
        product = T_Product.objects.filter(category=Id)
        if request.method == 'GET':
            serializer = S_Product(product, many=True)
            return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponse(status=404)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)


@csrf_exempt
def Crud_ProductImg(request, id=0):
    if request.method == 'GET':
        productsImg = T_ProductImg.objects.filter(product=id)
        productsImg_serializer = S_ProductImg(productsImg, many=True)
        return JsonResponse(productsImg_serializer.data, safe=False)
    elif request.method == 'POST':
        productImg_data = JSONParser().parse(request)
        print(productImg_data)
        productsImg_serializer = S_ProductImg(data=productImg_data)
        
        if productsImg_serializer.is_valid():
            productsImg_serializer.save()

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        productImg_data = JSONParser().parse(request)
        productImg = T_ProductImg.objects.get(
            product=productImg_data['product'])
        productsImg_serializer = S_ProductImg(productImg, data=productImg_data)
        if productsImg_serializer.is_valid():
            productsImg_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        productImg = T_ProductImg.objects.get(product=id)
        productImg.delete()
        return JsonResponse("Deleted Successfully", safe=False)



@csrf_exempt
def Crud_ProductImgColor(request, id=0):
    if request.method == 'GET':
        productsImg = T_ProductImgColor.objects.filter(Pic_Id=id)
        productsImg_serializer = S_ProductImgColor(productsImg, many=True)
        return JsonResponse(productsImg_serializer.data, safe=False)
    elif request.method == 'POST':
        productImg_data = JSONParser().parse(request)
        
        productsImg_serializer =S_ProductImgColor(data=productImg_data)
        if productsImg_serializer.is_valid():
            productsImg_serializer.save()

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        productImg_data = JSONParser().parse(request)
        productImg = T_ProductImg.objects.get(
            product=productImg_data['product'])
        productsImg_serializer = S_ProductImg(productImg, data=productImg_data)
        if productsImg_serializer.is_valid():
            productsImg_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        productImg = T_ProductImg.objects.get(product=id)
        productImg.delete()
        return JsonResponse("Deleted Successfully", safe=False)
@csrf_exempt
def Crud_Category(request, id=0):
    if request.method == 'GET':
        categories = T_Category.objects.all()
        categories_serializer = S_Category(categories, many=True)
        return JsonResponse(categories_serializer.data, safe=False)
    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        print(category_data)
        categories_serializer = S_Category(data=category_data)
        if categories_serializer.is_valid():
            categories_serializer.save()

            return JsonResponse(categories_serializer.data, safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category = T_Category.objects.get(Categ_Id=category_data['Categ_Id'])
        categories_serializer = S_Category(
            category, data=category_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        category = T_Category.objects.get(Categ_Id=id)
        category.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Crud_Caracteristic(request, id=0):
    if request.method == 'GET':
        characteristic = T_Characteristic.objects.filter(Carec_Id=id)
        serializer = S_Characteristic(characteristic, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        characteristic_data = JSONParser().parse(request)
        serializer = S_Characteristic(data=characteristic_data)
        
        if serializer.is_valid():
            
            serializer.save()
           
            for categ in characteristic_data["category"]:
             categobj=T_Category.objects.get(Categ_Id=categ)
            
             print(serializer.fields["category"])
             serializer.data["category"].append(categobj)
             
             
             #serializer.category.add(categ_obj)
            serializer_carac=S_Characteristic(serializer)
            

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        characteristic_data = JSONParser().parse(request)
        characteristic = T_Characteristic.objects.get(
            Carec_Id=characteristic_data['Carec_Id'])
        serializer = S_Characteristic(
            characteristic, data=characteristic_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        characteristic = T_Characteristic.objects.get(Carec_Id=id)
        characteristic.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Crud_Caracteristic_ByCateg(request, id=0):
    if request.method == 'GET':
        characteristic = T_Characteristic.objects.filter(category=id)
        serializer = S_Characteristic(characteristic, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        characteristic_data = JSONParser().parse(request)
        serializer = S_Characteristic(data=characteristic_data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        characteristic_data = JSONParser().parse(request)
        characteristic = T_Characteristic.objects.get(
            Carec_Id=characteristic_data['Carec_Id'])
        serializer = S_Characteristic(
            characteristic, data=characteristic_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        characteristic = T_Characteristic.objects.get(Carec_Id=id)
        characteristic.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Crud_CaracDetail(request, id=0):
    if request.method == 'GET':
        characDetail = T_Carac_detail.objects.filter(Carac_Detail_Id=id)
        serializer = S_Carac_detail(characDetail, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        characDetail_data = JSONParser().parse(request)
        serializer = S_Carac_detail(data=characDetail_data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        characDetail_data = JSONParser().parse(request)
        characDetail = T_Carac_detail.objects.get(
            Carac_Detail_Id=characDetail_data['Carac_Detail_Id'])
        serializer = S_Carac_detail(
            characDetail, data=characDetail_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        characDetail = T_Carac_detail.objects.get(Carac_Detail_Id=id)
        characDetail.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def Crud_CaracDetail_Bycarac(request, id=0):
    if request.method == 'GET':
        characDetail = T_Carac_detail.objects.filter(Carac_Id=id)
        serializer = S_Carac_detail(characDetail, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        characDetail_data = JSONParser().parse(request)
        serializer = S_Carac_detail(data=characDetail_data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        characDetail_data = JSONParser().parse(request)
        characDetail = T_Carac_detail.objects.get(
            Carac_Detail_Id=characDetail_data['Carac_Detail_Id'])
        serializer = S_Carac_detail(
            characDetail, data=characDetail_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        characDetail = T_Carac_detail.objects.get(Carac_Detail_Id=id)
        characDetail.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Crud_CaracProduct(request, id=0):
    if request.method == 'GET':
        characProduct = T_Carac_Product.objects.filter(Prod_Id=id)
        serializer = S_Carac_Product(characProduct, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        characProduct_data = JSONParser().parse(request)
        serializer = S_Carac_Product(data=characProduct_data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        characProduct_data = JSONParser().parse(request)
        
        characProduct = T_Carac_Product.objects.get(
            Carec_Prod_Id=characProduct_data['Carec_Prod_Id'])
        
        serializer = S_Carac_Product(
            characProduct, data=characProduct_data)
        
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method == 'DELETE':
        characProduct = T_Carac_Product.objects.get(Carec_Prod_Id=id)
        characProduct.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def Crud_CaracProductByCarac(request, id=0):
    if request.method == 'GET':
        characProduct = T_Carac_Product.objects.filter(Carec_Id=id)
        serializer = S_Carac_Product(characProduct, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        characProduct_data = JSONParser().parse(request)
        serializer = S_Carac_Product(data=characProduct_data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        characProduct_data = JSONParser().parse(request)
        characProduct = T_Carac_Product.objects.get(
            Carec_Prod_Id=characProduct_data['Carec_Prod_Id'])
        serializer = S_Carac_detail(
            characProduct, data=characProduct_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        characProduct = T_Carac_Product.objects.get(Carec_Prod_Id=id)
        characProduct.delete()
        return JsonResponse("Deleted Successfully", safe=False)

# Create your views here.
class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return T_Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except T_Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = S_Product(product)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = T_Product.objects.filter(
            Q(Prod_Name__icontains=query) | Q(Prod_Description__icontains=query))
        serializer = S_Product(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})


@csrf_exempt
def product_by_category(request, category):
    try:
        product = T_Product.objects.get(category=category)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = S_Product(product, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def edit_ProductQte(request, Id):

    Vqte = JSONParser().parse(request)
    item = T_Product.objects.get(Prod_Id=Id)
    item.Prod_Quantity = Vqte['Prod_Quantity']
    item.save(update_fields=['Prod_Quantity'])
    return JsonResponse(item.Prod_Quantity, safe=False)
