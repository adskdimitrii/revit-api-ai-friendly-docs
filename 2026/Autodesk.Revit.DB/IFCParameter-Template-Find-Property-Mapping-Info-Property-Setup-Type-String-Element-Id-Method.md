# IFCParameter Template Find Property Mapping Info(Property Setup Type, String, Element Id) Method

Source: https://www.revitapidocs.com/2026/1f3d6de5-7af8-6f09-99b5-2eff538073ac.htm

---

| IFCParameter Template Find Property Mapping Info(Property Setup Type, String, Element Id) Method |
| --- |

Finds the property mapping info in the property set by id. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IFCPropertyMappingInfo FindPropertyMappingInfo(
	PropertySetupType propertySetupType,
	string propertySetName,
	ElementId revitPropertyId
)
```

```
Public Function FindPropertyMappingInfo ( 
	propertySetupType As PropertySetupType,
	propertySetName As String,
	revitPropertyId As ElementId
) As IFCPropertyMappingInfo
```

```
public:
IFCPropertyMappingInfo^ FindPropertyMappingInfo(
	PropertySetupType propertySetupType, 
	String^ propertySetName, 
	ElementId^ revitPropertyId
)
```

```
member FindPropertyMappingInfo : 
        propertySetupType : PropertySetupType * 
        propertySetName : string * 
        revitPropertyId : ElementId -> IFCPropertyMappingInfo 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
:   The property setup type.

propertySetName String
:   The property set name.

revitPropertyId [ElementId](Element-Id-Class.md)
:   The Revit property id.

#### Return Value

[IFCPropertyMappingInfo](IFCProperty-Mapping-Info-Class.md) 
The property mapping info or if not found. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [FindPropertyMappingInfo Overload](IFCParameter-Template-Find-Property-Mapping-Info-Method.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
