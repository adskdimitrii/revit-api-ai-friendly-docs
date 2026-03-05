# IFCParameter Template Get Property Set Names Method

Source: https://www.revitapidocs.com/2026/deb275c9-c490-380c-f0fe-132360c4515d.htm

---

| IFCParameter Template Get Property Set Names Method |
| --- |

Creates an array of property set names contained in the template according to provided selection type. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<string> GetPropertySetNames(
	PropertySetupType propertySetupType,
	PropertySelectionType propertySelectionType
)
```

```
Public Function GetPropertySetNames ( 
	propertySetupType As PropertySetupType,
	propertySelectionType As PropertySelectionType
) As IList(Of String)
```

```
public:
IList<String^>^ GetPropertySetNames(
	PropertySetupType propertySetupType, 
	PropertySelectionType propertySelectionType
)
```

```
member GetPropertySetNames : 
        propertySetupType : PropertySetupType * 
        propertySelectionType : PropertySelectionType -> IList<string> 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
:   The property setup type.

propertySelectionType [PropertySelectionType](Property-Selection-Type-Enumeration.md)
:   The property selection type.

#### Return Value

IList String 
The array of the property set names in the template. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
