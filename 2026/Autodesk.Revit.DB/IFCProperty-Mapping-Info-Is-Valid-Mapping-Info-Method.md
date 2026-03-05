# IFCProperty Mapping Info Is Valid Mapping Info Method

Source: https://www.revitapidocs.com/2026/6f5dc519-9d05-6355-bc9f-462125a6e347.htm

---

| IFCProperty Mapping Info Is Valid Mapping Info Method |
| --- |

Defines whether the mapping info contains meaningful data. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static bool IsValidMappingInfo(
	IFCPropertyMappingInfo mappingInfo
)
```

```
Public Shared Function IsValidMappingInfo ( 
	mappingInfo As IFCPropertyMappingInfo
) As Boolean
```

```
public:
static bool IsValidMappingInfo(
	IFCPropertyMappingInfo^ mappingInfo
)
```

```
static member IsValidMappingInfo : 
        mappingInfo : IFCPropertyMappingInfo -> bool 
```

#### Parameters

mappingInfo [IFCPropertyMappingInfo](IFCProperty-Mapping-Info-Class.md)
:   The mapping info

#### Return Value

Boolean 
Whether or not the mapping info is valid. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCPropertyMappingInfo Class](IFCProperty-Mapping-Info-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
