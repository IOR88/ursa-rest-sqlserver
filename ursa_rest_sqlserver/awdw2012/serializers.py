from rest_framework.serializers import HyperlinkedModelSerializer
from awdw2012 import models


class AdventureworksdwbuildversionSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Adventureworksdwbuildversion
        fields = '__all__'
        # fields =(u'id', 'dbversion', 'versiondate')


class DatabaselogSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Databaselog
        fields = '__all__'
        # fields =(u'id', 'databaselogid', 'posttime', 'databaseuser', 'event', 'schema', 'object', 'tsql', 'xmlevent')


class DimaccountSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimaccount
        #fields = '__all__'
        fields =('accountkey',
                 'parentaccountkey',
                 'accountcodealternatekey',
                 'parentaccountcodealternatekey',
                 'accountdescription',
                 'accounttype',
                 'operator',
                 'custommembers',
                 'valuetype',
                 'custommemberoptions')


class DimcurrencySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimcurrency
        fields = '__all__'
        # fields =('dimorganization', 'factcurrencyrate', 'factinternetsales', 'factresellersales', 'currencykey', 'currencyalternatekey', 'currencyname')


class DimcustomerSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimcustomer
        fields = '__all__'
        # fields =('factinternetsales', 'factsurveyresponse', 'customerkey', 'geographykey', 'customeralternatekey', 'title', 'firstname', 'middlename', 'lastname', 'namestyle', 'birthdate', 'maritalstatus', 'suffix', 'gender', 'emailaddress', 'yearlyincome', 'totalchildren', 'numberchildrenathome', 'englisheducation', 'spanisheducation', 'frencheducation', 'englishoccupation', 'spanishoccupation', 'frenchoccupation', 'houseownerflag', 'numbercarsowned', 'addressline1', 'addressline2', 'phone', 'datefirstpurchase', 'commutedistance')


class DimdateSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimdate
        fields = '__all__'
        # fields =('factcallcenter', 'factcurrencyrate', 'factfinance', u'fis_by_orderdatekey', u'fis_by_duedatekey', u'fis_by_shipdatekey', 'factproductinventory', u'frs_by_orderdatekey', u'frs_by_duedatekey', u'frs_by_shipdatekey', 'factsalesquota', 'factsurveyresponse', 'datekey', 'fulldatealternatekey', 'daynumberofweek', 'englishdaynameofweek', 'spanishdaynameofweek', 'frenchdaynameofweek', 'daynumberofmonth', 'daynumberofyear', 'weeknumberofyear', 'englishmonthname', 'spanishmonthname', 'frenchmonthname', 'monthnumberofyear', 'calendarquarter', 'calendaryear', 'calendarsemester', 'fiscalquarter', 'fiscalyear', 'fiscalsemester')


class DimdepartmentgroupSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimdepartmentgroup
        fields = '__all__'
        # fields =('dimdepartmentgroup', 'factfinance', 'departmentgroupkey', 'parentdepartmentgroupkey', 'departmentgroupname')


class DimemployeeSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimemployee
        fields = '__all__'
        # fields =('dimemployee', 'factresellersales', 'factsalesquota', 'employeekey', 'parentemployeekey', 'employeenationalidalternatekey', 'parentemployeenationalidalternatekey', 'salesterritorykey', 'firstname', 'lastname', 'middlename', 'namestyle', 'title', 'hiredate', 'birthdate', 'loginid', 'emailaddress', 'phone', 'maritalstatus', 'emergencycontactname', 'emergencycontactphone', 'salariedflag', 'gender', 'payfrequency', 'baserate', 'vacationhours', 'sickleavehours', 'currentflag', 'salespersonflag', 'departmentname', 'startdate', 'enddate', 'status', 'employeephoto')


class DimgeographySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimgeography
        fields = '__all__'
        # fields =('dimcustomer', 'dimreseller', 'geographykey', 'city', 'stateprovincecode', 'stateprovincename', 'countryregioncode', 'englishcountryregionname', 'spanishcountryregionname', 'frenchcountryregionname', 'postalcode', 'salesterritorykey', 'ipaddresslocator')


class DimorganizationSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimorganization
        fields = '__all__'
        # fields =('dimorganization', 'factfinance', 'organizationkey', 'parentorganizationkey', 'percentageofownership', 'organizationname', 'currencykey')


class DimproductSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimproduct
        fields = '__all__'
        # fields =('factinternetsales', 'factproductinventory', 'factresellersales', 'productkey', 'productalternatekey', 'productsubcategorykey', 'weightunitmeasurecode', 'sizeunitmeasurecode', 'englishproductname', 'spanishproductname', 'frenchproductname', 'standardcost', 'finishedgoodsflag', 'color', 'safetystocklevel', 'reorderpoint', 'listprice', 'size', 'sizerange', 'weight', 'daystomanufacture', 'productline', 'dealerprice', 'class_field', 'style', 'modelname', 'largephoto', 'englishdescription', 'frenchdescription', 'chinesedescription', 'arabicdescription', 'hebrewdescription', 'thaidescription', 'germandescription', 'japanesedescription', 'turkishdescription', 'startdate', 'enddate', 'status')


class DimproductcategorySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimproductcategory
        fields = '__all__'
        # fields =('dimproductsubcategory', 'productcategorykey', 'productcategoryalternatekey', 'englishproductcategoryname', 'spanishproductcategoryname', 'frenchproductcategoryname')


class DimproductsubcategorySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimproductsubcategory
        fields = '__all__'
        # fields =('dimproduct', 'productsubcategorykey', 'productsubcategoryalternatekey', 'englishproductsubcategoryname', 'spanishproductsubcategoryname', 'frenchproductsubcategoryname', 'productcategorykey')


class DimpromotionSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimpromotion
        fields = '__all__'
        # fields =('factinternetsales', 'factresellersales', 'promotionkey', 'promotionalternatekey', 'englishpromotionname', 'spanishpromotionname', 'frenchpromotionname', 'discountpct', 'englishpromotiontype', 'spanishpromotiontype', 'frenchpromotiontype', 'englishpromotioncategory', 'spanishpromotioncategory', 'frenchpromotioncategory', 'startdate', 'enddate', 'minqty', 'maxqty')


class DimresellerSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimreseller
        fields = '__all__'
        # fields =('factresellersales', 'resellerkey', 'geographykey', 'reselleralternatekey', 'phone', 'businesstype', 'resellername', 'numberemployees', 'orderfrequency', 'ordermonth', 'firstorderyear', 'lastorderyear', 'productline', 'addressline1', 'addressline2', 'annualsales', 'bankname', 'minpaymenttype', 'minpaymentamount', 'annualrevenue', 'yearopened')


class DimsalesreasonSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimsalesreason
        fields = '__all__'
        # fields =('factinternetsalesreason', 'salesreasonkey', 'salesreasonalternatekey', 'salesreasonname', 'salesreasonreasontype')


class DimsalesterritorySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimsalesterritory
        fields = '__all__'
        # fields =('dimemployee', 'dimgeography', 'factinternetsales', 'factresellersales', 'salesterritorykey', 'salesterritoryalternatekey', 'salesterritoryregion', 'salesterritorycountry', 'salesterritorygroup', 'salesterritoryimage')


class DimscenarioSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Dimscenario
        fields = '__all__'
        # fields =('factfinance', 'scenariokey', 'scenarioname')


class FactadditionalinternationalproductdescriptionSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Factadditionalinternationalproductdescription
        fields = '__all__'
        # fields =(u'id', 'productkey', 'culturename', 'productdescription')


class FactcallcenterSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Factcallcenter
        fields = '__all__'
        # fields =('factcallcenterid', 'datekey', 'wagetype', 'shift', 'leveloneoperators', 'leveltwooperators', 'totaloperators', 'calls', 'automaticresponses', 'orders', 'issuesraised', 'averagetimeperissue', 'servicegrade', 'date')


class FactcurrencyrateSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Factcurrencyrate
        fields = '__all__'
        # fields =(u'id', 'currencykey', 'datekey', 'averagerate', 'endofdayrate', 'date')


class FactfinanceSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Factfinance
        fields = '__all__'
        # fields =(u'id', 'financekey', 'datekey', 'organizationkey', 'departmentgroupkey', 'scenariokey', 'accountkey', 'amount', 'date')


class FactinternetsalesSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Factinternetsales
        fields = '__all__'
        # fields =(u'fisr_by_salesordernumber', u'fisr_by_salesorderlinenumber', u'id', 'productkey', 'orderdatekey', 'duedatekey', 'shipdatekey', 'customerkey', 'promotionkey', 'currencykey', 'salesterritorykey', 'salesordernumber', 'salesorderlinenumber', 'revisionnumber', 'orderquantity', 'unitprice', 'extendedamount', 'unitpricediscountpct', 'discountamount', 'productstandardcost', 'totalproductcost', 'salesamount', 'taxamt', 'freight', 'carriertrackingnumber', 'customerponumber', 'orderdate', 'duedate', 'shipdate')


class FactinternetsalesreasonSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Factinternetsalesreason
        fields = '__all__'
        # fields =(u'id', 'salesordernumber', 'salesorderlinenumber', 'salesreasonkey')


class FactproductinventorySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Factproductinventory
        fields = '__all__'
        # fields =(u'id', 'productkey', 'datekey', 'movementdate', 'unitcost', 'unitsin', 'unitsout', 'unitsbalance')


class FactresellersalesSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Factresellersales
        fields = '__all__'
        # fields =(u'id', 'productkey', 'orderdatekey', 'duedatekey', 'shipdatekey', 'resellerkey', 'employeekey', 'promotionkey', 'currencykey', 'salesterritorykey', 'salesordernumber', 'salesorderlinenumber', 'revisionnumber', 'orderquantity', 'unitprice', 'extendedamount', 'unitpricediscountpct', 'discountamount', 'productstandardcost', 'totalproductcost', 'salesamount', 'taxamt', 'freight', 'carriertrackingnumber', 'customerponumber', 'orderdate', 'duedate', 'shipdate')


class FactsalesquotaSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Factsalesquota
        fields = '__all__'
        # fields =('salesquotakey', 'employeekey', 'datekey', 'calendaryear', 'calendarquarter', 'salesamountquota', 'date')


class FactsurveyresponseSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Factsurveyresponse
        fields = '__all__'
        # fields =('surveyresponsekey', 'datekey', 'customerkey', 'productcategorykey', 'englishproductcategoryname', 'productsubcategorykey', 'englishproductsubcategoryname', 'date')


class ProspectivebuyerSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Prospectivebuyer
        fields = '__all__'
        # fields =('prospectivebuyerkey', 'prospectalternatekey', 'firstname', 'middlename', 'lastname', 'birthdate', 'maritalstatus', 'gender', 'emailaddress', 'yearlyincome', 'totalchildren', 'numberchildrenathome', 'education', 'occupation', 'houseownerflag', 'numbercarsowned', 'addressline1', 'addressline2', 'city', 'stateprovincecode', 'postalcode', 'phone', 'salutation', 'unknown')


class SysdiagramsSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = models.Sysdiagrams
        fields = '__all__'
        # fields =('name', 'principal_id', 'diagram_id', 'version', 'definition')
