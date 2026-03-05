# IFCProperty Mapping Info(Boolean, String, Element Id, String) Constructor

Source: https://www.revitapidocs.com/2026/d8a51852-e001-31b4-447d-58b3731f2c67.htm

---

| IFCProperty Mapping Info(Boolean, String, Element Id, String) Constructor |
| --- |

Constructs a new IFCPropertyMappingInfo with input values.
 The flag that indicates whether the property is included in export.
 The property name.
 The Revit property id.
 The Revit property id. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IFCPropertyMappingInfo(
	bool exportFlag,
	string ifcPropertyName,
	ElementId revitPropertyId,
	string revitPropertyName
)
```

```
Public Sub New ( 
	exportFlag As Boolean,
	ifcPropertyName As String,
	revitPropertyId As ElementId,
	revitPropertyName As String
)
```

```
public:
IFCPropertyMappingInfo(
	bool exportFlag, 
	String^ ifcPropertyName, 
	ElementId^ revitPropertyId, 
	String^ revitPropertyName
)
```

```
new : 
        exportFlag : bool * 
        ifcPropertyName : string * 
        revitPropertyId : ElementId * 
        revitPropertyName : string -> IFCPropertyMappingInfo
```

#### Parameters

exportFlag Boolean
ifcPropertyName String
revitPropertyId [ElementId](Element-Id-Class.md)
revitPropertyName String

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCPropertyMappingInfo Class](IFCProperty-Mapping-Info-Class.md) [IFCPropertyMappingInfo Overload](IFCProperty-Mapping-Info-Constructor.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
