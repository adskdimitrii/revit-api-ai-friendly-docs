# IFCParameter Template Get Property Mapping Infos Method

Source: https://www.revitapidocs.com/2026/1f73ee6a-7194-25e2-c743-10e2cb11a8fe.htm

---

| IFCParameter Template Get Property Mapping Infos Method |
| --- |

Creates an array of property mappings contained in the property set according to provided selection type. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<IFCPropertyMappingInfo> GetPropertyMappingInfos(
	PropertySetupType propertySetupType,
	string propertySetName,
	PropertySelectionType propertySelectionType
)
```

```
Public Function GetPropertyMappingInfos ( 
	propertySetupType As PropertySetupType,
	propertySetName As String,
	propertySelectionType As PropertySelectionType
) As IList(Of IFCPropertyMappingInfo)
```

```
public:
IList<IFCPropertyMappingInfo^>^ GetPropertyMappingInfos(
	PropertySetupType propertySetupType, 
	String^ propertySetName, 
	PropertySelectionType propertySelectionType
)
```

```
member GetPropertyMappingInfos : 
        propertySetupType : PropertySetupType * 
        propertySetName : string * 
        propertySelectionType : PropertySelectionType -> IList<IFCPropertyMappingInfo> 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
:   The property setup type.

propertySetName String
:   The property set name.

propertySelectionType [PropertySelectionType](Property-Selection-Type-Enumeration.md)
:   The property selection type.

#### Return Value

IList [IFCPropertyMappingInfo](IFCProperty-Mapping-Info-Class.md) 
The array of the property mappings in the property set. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
