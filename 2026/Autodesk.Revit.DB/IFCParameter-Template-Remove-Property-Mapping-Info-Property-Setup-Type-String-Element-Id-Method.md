# IFCParameter Template Remove Property Mapping Info(Property Setup Type, String, Element Id) Method

Source: https://www.revitapidocs.com/2026/a64921b8-776c-3f62-20cd-2e92be22aabf.htm

---

| IFCParameter Template Remove Property Mapping Info(Property Setup Type, String, Element Id) Method |
| --- |

Removes the property mapping from the property set by id. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void RemovePropertyMappingInfo(
	PropertySetupType propertySetupType,
	string propertySetName,
	ElementId revitPropertyId
)
```

```
Public Sub RemovePropertyMappingInfo ( 
	propertySetupType As PropertySetupType,
	propertySetName As String,
	revitPropertyId As ElementId
)
```

```
public:
void RemovePropertyMappingInfo(
	PropertySetupType propertySetupType, 
	String^ propertySetName, 
	ElementId^ revitPropertyId
)
```

```
member RemovePropertyMappingInfo : 
        propertySetupType : PropertySetupType * 
        propertySetName : string * 
        revitPropertyId : ElementId -> unit 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
:   The property setup type.

propertySetName String
:   The property set name.

revitPropertyId [ElementId](Element-Id-Class.md)
:   The Revit property id.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [RemovePropertyMappingInfo Overload](IFCParameter-Template-Remove-Property-Mapping-Info-Method.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
