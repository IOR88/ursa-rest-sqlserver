from rest_framework.viewsets import ModelViewSet
from awdw2012 import models
from awdw2012 import serializers
from awdw2012 import filters


class AdventureworksdwbuildversionViewSet(ModelViewSet):

    queryset = models.Adventureworksdwbuildversion.objects.all()
    serializer_class = serializers.AdventureworksdwbuildversionSerializer
    filter_class = filters.AdventureworksdwbuildversionFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DatabaselogViewSet(ModelViewSet):

    queryset = models.Databaselog.objects.all()
    serializer_class = serializers.DatabaselogSerializer
    filter_class = filters.DatabaselogFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimaccountViewSet(ModelViewSet):

    queryset = models.Dimaccount.objects.all()
    serializer_class = serializers.DimaccountSerializer
    filter_class = filters.DimaccountFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimcurrencyViewSet(ModelViewSet):

    queryset = models.Dimcurrency.objects.all()
    serializer_class = serializers.DimcurrencySerializer
    filter_class = filters.DimcurrencyFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimcustomerViewSet(ModelViewSet):

    queryset = models.Dimcustomer.objects.all()
    serializer_class = serializers.DimcustomerSerializer
    filter_class = filters.DimcustomerFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimdateViewSet(ModelViewSet):

    queryset = models.Dimdate.objects.all()
    serializer_class = serializers.DimdateSerializer
    filter_class = filters.DimdateFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimdepartmentgroupViewSet(ModelViewSet):

    queryset = models.Dimdepartmentgroup.objects.all()
    serializer_class = serializers.DimdepartmentgroupSerializer
    filter_class = filters.DimdepartmentgroupFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimemployeeViewSet(ModelViewSet):

    queryset = models.Dimemployee.objects.all()
    serializer_class = serializers.DimemployeeSerializer
    filter_class = filters.DimemployeeFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimgeographyViewSet(ModelViewSet):

    queryset = models.Dimgeography.objects.all()
    serializer_class = serializers.DimgeographySerializer
    filter_class = filters.DimgeographyFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimorganizationViewSet(ModelViewSet):

    queryset = models.Dimorganization.objects.all()
    serializer_class = serializers.DimorganizationSerializer
    filter_class = filters.DimorganizationFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimproductViewSet(ModelViewSet):

    queryset = models.Dimproduct.objects.all()
    serializer_class = serializers.DimproductSerializer
    filter_class = filters.DimproductFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimproductcategoryViewSet(ModelViewSet):

    queryset = models.Dimproductcategory.objects.all()
    serializer_class = serializers.DimproductcategorySerializer
    filter_class = filters.DimproductcategoryFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimproductsubcategoryViewSet(ModelViewSet):

    queryset = models.Dimproductsubcategory.objects.all()
    serializer_class = serializers.DimproductsubcategorySerializer
    filter_class = filters.DimproductsubcategoryFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimpromotionViewSet(ModelViewSet):

    queryset = models.Dimpromotion.objects.all()
    serializer_class = serializers.DimpromotionSerializer
    filter_class = filters.DimpromotionFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimresellerViewSet(ModelViewSet):

    queryset = models.Dimreseller.objects.all()
    serializer_class = serializers.DimresellerSerializer
    filter_class = filters.DimresellerFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimsalesreasonViewSet(ModelViewSet):

    queryset = models.Dimsalesreason.objects.all()
    serializer_class = serializers.DimsalesreasonSerializer
    filter_class = filters.DimsalesreasonFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimsalesterritoryViewSet(ModelViewSet):

    queryset = models.Dimsalesterritory.objects.all()
    serializer_class = serializers.DimsalesterritorySerializer
    filter_class = filters.DimsalesterritoryFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class DimscenarioViewSet(ModelViewSet):

    queryset = models.Dimscenario.objects.all()
    serializer_class = serializers.DimscenarioSerializer
    filter_class = filters.DimscenarioFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class FactadditionalinternationalproductdescriptionViewSet(ModelViewSet):

    queryset = models.Factadditionalinternationalproductdescription.objects.all()
    serializer_class = serializers.FactadditionalinternationalproductdescriptionSerializer
    filter_class = filters.FactadditionalinternationalproductdescriptionFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class FactcallcenterViewSet(ModelViewSet):

    queryset = models.Factcallcenter.objects.all()
    serializer_class = serializers.FactcallcenterSerializer
    filter_class = filters.FactcallcenterFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class FactcurrencyrateViewSet(ModelViewSet):

    queryset = models.Factcurrencyrate.objects.all()
    serializer_class = serializers.FactcurrencyrateSerializer
    filter_class = filters.FactcurrencyrateFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class FactfinanceViewSet(ModelViewSet):

    queryset = models.Factfinance.objects.all()
    serializer_class = serializers.FactfinanceSerializer
    filter_class = filters.FactfinanceFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class FactinternetsalesViewSet(ModelViewSet):

    queryset = models.Factinternetsales.objects.all()
    serializer_class = serializers.FactinternetsalesSerializer
    filter_class = filters.FactinternetsalesFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class FactinternetsalesreasonViewSet(ModelViewSet):

    queryset = models.Factinternetsalesreason.objects.all()
    serializer_class = serializers.FactinternetsalesreasonSerializer
    filter_class = filters.FactinternetsalesreasonFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class FactproductinventoryViewSet(ModelViewSet):

    queryset = models.Factproductinventory.objects.all()
    serializer_class = serializers.FactproductinventorySerializer
    filter_class = filters.FactproductinventoryFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class FactresellersalesViewSet(ModelViewSet):

    queryset = models.Factresellersales.objects.all()
    serializer_class = serializers.FactresellersalesSerializer
    filter_class = filters.FactresellersalesFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class FactsalesquotaViewSet(ModelViewSet):

    queryset = models.Factsalesquota.objects.all()
    serializer_class = serializers.FactsalesquotaSerializer
    filter_class = filters.FactsalesquotaFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class FactsurveyresponseViewSet(ModelViewSet):

    queryset = models.Factsurveyresponse.objects.all()
    serializer_class = serializers.FactsurveyresponseSerializer
    filter_class = filters.FactsurveyresponseFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class ProspectivebuyerViewSet(ModelViewSet):

    queryset = models.Prospectivebuyer.objects.all()
    serializer_class = serializers.ProspectivebuyerSerializer
    filter_class = filters.ProspectivebuyerFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)


class SysdiagramsViewSet(ModelViewSet):

    queryset = models.Sysdiagrams.objects.all()
    serializer_class = serializers.SysdiagramsSerializer
    filter_class = filters.SysdiagramsFilterSet
    # filter_fields = ('type_filed_name_here',)
    # search_fields = ('type_filed_name_here',)
