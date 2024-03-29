
from django.urls import re_path
from DjangoAPI import settings
from Products import views


from django.conf.urls.static import static


urlpatterns = [
    
    re_path(r'^product/$', views.Crud_Product),
    re_path(r'^SaveFile$', views.SaveFile),
    re_path(r'^product/([0-9]+)$', views.Crud_Product),
    re_path(r'^productImg/$', views.Crud_ProductImg),
    re_path(r'^productImg/([0-9]+)$', views.Crud_ProductImg),
     re_path(r'^productImgColor/$', views.Crud_ProductImgColor),
    re_path(r'^productImgColor/([0-9]+)$', views.Crud_ProductImgColor),
    re_path(r'^category/$', views.Crud_Category),
    re_path(r'^category/([0-9]+)$', views.Crud_Category),
    re_path(r'^caracteristic/$', views.Crud_Caracteristic),
    re_path(r'^caracteristic/([0-9]+)$', views.Crud_Caracteristic),
    re_path(r'^caracDetail/$', views.Crud_CaracDetail),
    re_path(r'^caracDetail/([0-9]+)$', views.Crud_CaracDetail),
    re_path(r'^caracProduct/$', views.Crud_CaracProduct),
    re_path(r'^caracProduct/([0-9]+)$', views.Crud_CaracProduct),
    re_path(r'^ProductById/([0-9]+)$', views.get_Product_ById),
    re_path(r'^get_Product_ByCateg/([0-9]+)$', views.get_Product_ByCateg),
    re_path(r'^editProduct/([0-9]+)$', views.edit_ProductQte),
    re_path(r'^get_caracByCateg/([0-9]+)$', views.Crud_Caracteristic_ByCateg),
    re_path(r'^get_detailByCarac/([0-9]+)$', views.Crud_CaracDetail_Bycarac),
     re_path(r'^get_caracProductByCarac/([0-9]+)$', views.Crud_CaracProductByCarac),

    
    
    # re_path(r'^send$',views.send_email),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
