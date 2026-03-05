# IFCParameter Template Is Exporting Property Set Method

Source: https://www.revitapidocs.com/2026/d86eac08-5823-79c1-c19a-6e09b8f18ad8.htm

---

| IFCParameter Template Is Exporting Property Set Method |
| --- |

Determines whether the provided property set is included in export. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool IsExportingPropertySet(
	PropertySetupType propertySetupType,
	string propertySetName
)
```

```
Public Function IsExportingPropertySet ( 
	propertySetupType As PropertySetupType,
	propertySetName As String
) As Boolean
```

```
public:
bool IsExportingPropertySet(
	PropertySetupType propertySetupType, 
	String^ propertySetName
)
```

```
member IsExportingPropertySet : 
        propertySetupType : PropertySetupType * 
        propertySetName : string -> bool 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
:   The property setup type.

propertySetName String
:   The property set name.

#### Return Value

Boolean 
Whether or not the property set is included in export. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | A property set with the given name is not present in the template. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
