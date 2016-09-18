from django.conf.urls import url, include
from rest_framework import routers
from awdw2012 import views

router = routers.DefaultRouter()
router.register(r'Adventureworksdwbuildversion', views.AdventureworksdwbuildversionViewSet)
router.register(r'Databaselog', views.DatabaselogViewSet)
router.register(r'Dimaccount', views.DimaccountViewSet)
router.register(r'Dimcurrency', views.DimcurrencyViewSet)
router.register(r'Dimcustomer', views.DimcustomerViewSet)
router.register(r'Dimdate', views.DimdateViewSet)
router.register(r'Dimdepartmentgroup', views.DimdepartmentgroupViewSet)
router.register(r'Dimemployee', views.DimemployeeViewSet)
router.register(r'Dimgeography', views.DimgeographyViewSet)
router.register(r'Dimorganization', views.DimorganizationViewSet)
router.register(r'Dimproduct', views.DimproductViewSet)
router.register(r'Dimproductcategory', views.DimproductcategoryViewSet)
router.register(r'Dimproductsubcategory', views.DimproductsubcategoryViewSet)
router.register(r'Dimpromotion', views.DimpromotionViewSet)
router.register(r'Dimreseller', views.DimresellerViewSet)
router.register(r'Dimsalesreason', views.DimsalesreasonViewSet)
router.register(r'Dimsalesterritory', views.DimsalesterritoryViewSet)
router.register(r'Dimscenario', views.DimscenarioViewSet)
router.register(r'Factadditionalinternationalproductdescription', views.FactadditionalinternationalproductdescriptionViewSet)
router.register(r'Factcallcenter', views.FactcallcenterViewSet)
router.register(r'Factcurrencyrate', views.FactcurrencyrateViewSet)
router.register(r'Factfinance', views.FactfinanceViewSet)
router.register(r'Factinternetsales', views.FactinternetsalesViewSet)
router.register(r'Factinternetsalesreason', views.FactinternetsalesreasonViewSet)
router.register(r'Factproductinventory', views.FactproductinventoryViewSet)
router.register(r'Factresellersales', views.FactresellersalesViewSet)
router.register(r'Factsalesquota', views.FactsalesquotaViewSet)
router.register(r'Factsurveyresponse', views.FactsurveyresponseViewSet)
router.register(r'Prospectivebuyer', views.ProspectivebuyerViewSet)
router.register(r'Sysdiagrams', views.SysdiagramsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
