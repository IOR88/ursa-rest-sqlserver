from rest_framework.filters import FilterSet
from awdw2012 import models


class AdventureworksdwbuildversionFilterSet(FilterSet):

    class Meta:
        model = models.Adventureworksdwbuildversion
        fields =[u'id', 'dbversion', 'versiondate']


class DatabaselogFilterSet(FilterSet):

    class Meta:
        model = models.Databaselog
        fields =[u'id', 'databaselogid', 'posttime', 'databaseuser', 'event', 'schema', 'object', 'tsql', 'xmlevent']


class DimaccountFilterSet(FilterSet):

    class Meta:
        model = models.Dimaccount
        fields =['dimaccount', 'factfinance', 'accountkey', 'parentaccountkey', 'accountcodealternatekey', 'parentaccountcodealternatekey', 'accountdescription', 'accounttype', 'operator', 'custommembers', 'valuetype', 'custommemberoptions']


class DimcurrencyFilterSet(FilterSet):

    class Meta:
        model = models.Dimcurrency
        fields =['dimorganization', 'factcurrencyrate', 'factinternetsales', 'factresellersales', 'currencykey', 'currencyalternatekey', 'currencyname']


class DimcustomerFilterSet(FilterSet):

    class Meta:
        model = models.Dimcustomer
        fields =['factinternetsales', 'factsurveyresponse', 'customerkey', 'geographykey', 'customeralternatekey', 'title', 'firstname', 'middlename', 'lastname', 'namestyle', 'birthdate', 'maritalstatus', 'suffix', 'gender', 'emailaddress', 'yearlyincome', 'totalchildren', 'numberchildrenathome', 'englisheducation', 'spanisheducation', 'frencheducation', 'englishoccupation', 'spanishoccupation', 'frenchoccupation', 'houseownerflag', 'numbercarsowned', 'addressline1', 'addressline2', 'phone', 'datefirstpurchase', 'commutedistance']


class DimdateFilterSet(FilterSet):

    class Meta:
        model = models.Dimdate
        fields =['factcallcenter', 'factcurrencyrate', 'factfinance', u'fis_by_orderdatekey', u'fis_by_duedatekey', u'fis_by_shipdatekey', 'factproductinventory', u'frs_by_orderdatekey', u'frs_by_duedatekey', u'frs_by_shipdatekey', 'factsalesquota', 'factsurveyresponse', 'datekey', 'fulldatealternatekey', 'daynumberofweek', 'englishdaynameofweek', 'spanishdaynameofweek', 'frenchdaynameofweek', 'daynumberofmonth', 'daynumberofyear', 'weeknumberofyear', 'englishmonthname', 'spanishmonthname', 'frenchmonthname', 'monthnumberofyear', 'calendarquarter', 'calendaryear', 'calendarsemester', 'fiscalquarter', 'fiscalyear', 'fiscalsemester']


class DimdepartmentgroupFilterSet(FilterSet):

    class Meta:
        model = models.Dimdepartmentgroup
        fields =['dimdepartmentgroup', 'factfinance', 'departmentgroupkey', 'parentdepartmentgroupkey', 'departmentgroupname']


class DimemployeeFilterSet(FilterSet):

    class Meta:
        model = models.Dimemployee
        fields =['dimemployee', 'factresellersales', 'factsalesquota', 'employeekey', 'parentemployeekey', 'employeenationalidalternatekey', 'parentemployeenationalidalternatekey', 'salesterritorykey', 'firstname', 'lastname', 'middlename', 'namestyle', 'title', 'hiredate', 'birthdate', 'loginid', 'emailaddress', 'phone', 'maritalstatus', 'emergencycontactname', 'emergencycontactphone', 'salariedflag', 'gender', 'payfrequency', 'baserate', 'vacationhours', 'sickleavehours', 'currentflag', 'salespersonflag', 'departmentname', 'startdate', 'enddate', 'status', 'employeephoto']


class DimgeographyFilterSet(FilterSet):

    class Meta:
        model = models.Dimgeography
        fields =['dimcustomer', 'dimreseller', 'geographykey', 'city', 'stateprovincecode', 'stateprovincename', 'countryregioncode', 'englishcountryregionname', 'spanishcountryregionname', 'frenchcountryregionname', 'postalcode', 'salesterritorykey', 'ipaddresslocator']


class DimorganizationFilterSet(FilterSet):

    class Meta:
        model = models.Dimorganization
        fields =['dimorganization', 'factfinance', 'organizationkey', 'parentorganizationkey', 'percentageofownership', 'organizationname', 'currencykey']


class DimproductFilterSet(FilterSet):

    class Meta:
        model = models.Dimproduct
        fields =['factinternetsales', 'factproductinventory', 'factresellersales', 'productkey', 'productalternatekey', 'productsubcategorykey', 'weightunitmeasurecode', 'sizeunitmeasurecode', 'englishproductname', 'spanishproductname', 'frenchproductname', 'standardcost', 'finishedgoodsflag', 'color', 'safetystocklevel', 'reorderpoint', 'listprice', 'size', 'sizerange', 'weight', 'daystomanufacture', 'productline', 'dealerprice', 'class_field', 'style', 'modelname', 'largephoto', 'englishdescription', 'frenchdescription', 'chinesedescription', 'arabicdescription', 'hebrewdescription', 'thaidescription', 'germandescription', 'japanesedescription', 'turkishdescription', 'startdate', 'enddate', 'status']


class DimproductcategoryFilterSet(FilterSet):

    class Meta:
        model = models.Dimproductcategory
        fields =['dimproductsubcategory', 'productcategorykey', 'productcategoryalternatekey', 'englishproductcategoryname', 'spanishproductcategoryname', 'frenchproductcategoryname']


class DimproductsubcategoryFilterSet(FilterSet):

    class Meta:
        model = models.Dimproductsubcategory
        fields =['dimproduct', 'productsubcategorykey', 'productsubcategoryalternatekey', 'englishproductsubcategoryname', 'spanishproductsubcategoryname', 'frenchproductsubcategoryname', 'productcategorykey']


class DimpromotionFilterSet(FilterSet):

    class Meta:
        model = models.Dimpromotion
        fields =['factinternetsales', 'factresellersales', 'promotionkey', 'promotionalternatekey', 'englishpromotionname', 'spanishpromotionname', 'frenchpromotionname', 'discountpct', 'englishpromotiontype', 'spanishpromotiontype', 'frenchpromotiontype', 'englishpromotioncategory', 'spanishpromotioncategory', 'frenchpromotioncategory', 'startdate', 'enddate', 'minqty', 'maxqty']


class DimresellerFilterSet(FilterSet):

    class Meta:
        model = models.Dimreseller
        fields =['factresellersales', 'resellerkey', 'geographykey', 'reselleralternatekey', 'phone', 'businesstype', 'resellername', 'numberemployees', 'orderfrequency', 'ordermonth', 'firstorderyear', 'lastorderyear', 'productline', 'addressline1', 'addressline2', 'annualsales', 'bankname', 'minpaymenttype', 'minpaymentamount', 'annualrevenue', 'yearopened']


class DimsalesreasonFilterSet(FilterSet):

    class Meta:
        model = models.Dimsalesreason
        fields =['factinternetsalesreason', 'salesreasonkey', 'salesreasonalternatekey', 'salesreasonname', 'salesreasonreasontype']


class DimsalesterritoryFilterSet(FilterSet):

    class Meta:
        model = models.Dimsalesterritory
        fields =['dimemployee', 'dimgeography', 'factinternetsales', 'factresellersales', 'salesterritorykey', 'salesterritoryalternatekey', 'salesterritoryregion', 'salesterritorycountry', 'salesterritorygroup', 'salesterritoryimage']


class DimscenarioFilterSet(FilterSet):

    class Meta:
        model = models.Dimscenario
        fields =['factfinance', 'scenariokey', 'scenarioname']


class FactadditionalinternationalproductdescriptionFilterSet(FilterSet):

    class Meta:
        model = models.Factadditionalinternationalproductdescription
        fields =[u'id', 'productkey', 'culturename', 'productdescription']


class FactcallcenterFilterSet(FilterSet):

    class Meta:
        model = models.Factcallcenter
        fields =['factcallcenterid', 'datekey', 'wagetype', 'shift', 'leveloneoperators', 'leveltwooperators', 'totaloperators', 'calls', 'automaticresponses', 'orders', 'issuesraised', 'averagetimeperissue', 'servicegrade', 'date']


class FactcurrencyrateFilterSet(FilterSet):

    class Meta:
        model = models.Factcurrencyrate
        fields =[u'id', 'currencykey', 'datekey', 'averagerate', 'endofdayrate', 'date']


class FactfinanceFilterSet(FilterSet):

    class Meta:
        model = models.Factfinance
        fields =[u'id', 'financekey', 'datekey', 'organizationkey', 'departmentgroupkey', 'scenariokey', 'accountkey', 'amount', 'date']


class FactinternetsalesFilterSet(FilterSet):

    class Meta:
        model = models.Factinternetsales
        fields =[u'fisr_by_salesordernumber', u'fisr_by_salesorderlinenumber', u'id', 'productkey', 'orderdatekey', 'duedatekey', 'shipdatekey', 'customerkey', 'promotionkey', 'currencykey', 'salesterritorykey', 'salesordernumber', 'salesorderlinenumber', 'revisionnumber', 'orderquantity', 'unitprice', 'extendedamount', 'unitpricediscountpct', 'discountamount', 'productstandardcost', 'totalproductcost', 'salesamount', 'taxamt', 'freight', 'carriertrackingnumber', 'customerponumber', 'orderdate', 'duedate', 'shipdate']


class FactinternetsalesreasonFilterSet(FilterSet):

    class Meta:
        model = models.Factinternetsalesreason
        fields =[u'id', 'salesordernumber', 'salesorderlinenumber', 'salesreasonkey']


class FactproductinventoryFilterSet(FilterSet):

    class Meta:
        model = models.Factproductinventory
        fields =[u'id', 'productkey', 'datekey', 'movementdate', 'unitcost', 'unitsin', 'unitsout', 'unitsbalance']


class FactresellersalesFilterSet(FilterSet):

    class Meta:
        model = models.Factresellersales
        fields =[u'id', 'productkey', 'orderdatekey', 'duedatekey', 'shipdatekey', 'resellerkey', 'employeekey', 'promotionkey', 'currencykey', 'salesterritorykey', 'salesordernumber', 'salesorderlinenumber', 'revisionnumber', 'orderquantity', 'unitprice', 'extendedamount', 'unitpricediscountpct', 'discountamount', 'productstandardcost', 'totalproductcost', 'salesamount', 'taxamt', 'freight', 'carriertrackingnumber', 'customerponumber', 'orderdate', 'duedate', 'shipdate']


class FactsalesquotaFilterSet(FilterSet):

    class Meta:
        model = models.Factsalesquota
        fields =['salesquotakey', 'employeekey', 'datekey', 'calendaryear', 'calendarquarter', 'salesamountquota', 'date']


class FactsurveyresponseFilterSet(FilterSet):

    class Meta:
        model = models.Factsurveyresponse
        fields =['surveyresponsekey', 'datekey', 'customerkey', 'productcategorykey', 'englishproductcategoryname', 'productsubcategorykey', 'englishproductsubcategoryname', 'date']


class ProspectivebuyerFilterSet(FilterSet):

    class Meta:
        model = models.Prospectivebuyer
        fields =['prospectivebuyerkey', 'prospectalternatekey', 'firstname', 'middlename', 'lastname', 'birthdate', 'maritalstatus', 'gender', 'emailaddress', 'yearlyincome', 'totalchildren', 'numberchildrenathome', 'education', 'occupation', 'houseownerflag', 'numbercarsowned', 'addressline1', 'addressline2', 'city', 'stateprovincecode', 'postalcode', 'phone', 'salutation', 'unknown']


class SysdiagramsFilterSet(FilterSet):

    class Meta:
        model = models.Sysdiagrams
        fields =['name', 'principal_id', 'diagram_id', 'version', 'definition']
