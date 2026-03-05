# Parameter Filter Rule Factory Create Ends With Rule Method

Source: https://www.revitapidocs.com/2026/a1d0b45e-6669-ebe7-a10c-5bc40c7272d2.htm

---

| Parameter Filter Rule Factory Create Ends With Rule Method |
| --- |

Creates a filter rule that determines whether strings from the document
 end with a certain string value. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static FilterRule CreateEndsWithRule(
	ElementId parameter,
	string value
)
```

```
Public Shared Function CreateEndsWithRule ( 
	parameter As ElementId,
	value As String
) As FilterRule
```

```
public:
static FilterRule^ CreateEndsWithRule(
	ElementId^ parameter, 
	String^ value
)
```

```
static member CreateEndsWithRule : 
        parameter : ElementId * 
        value : string -> FilterRule 
```

#### Parameters

parameter [ElementId](Element-Id-Class.md)
:   A string\-typed parameter used to get values from the document for a given element.

value String
:   The user\-supplied string value for which values from the document will be searched.

#### Return Value

[FilterRule](a8f202ca-3c88-ecc4-fa93-549b26a412d7.htm) 
Created filter rule object. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ParameterFilterRuleFactory Class](Parameter-Filter-Rule-Factory-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
