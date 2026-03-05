# IFCParameter Template Add Property Set Method

Source: https://www.revitapidocs.com/2026/753f1a27-0829-a591-bc11-9a34586502ca.htm

---

| IFCParameter Template Add Property Set Method |
| --- |

Adds a property set to the template. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void AddPropertySet(
	PropertySetupType propertySetupType,
	bool exportFlag,
	string propertySetName
)
```

```
Public Sub AddPropertySet ( 
	propertySetupType As PropertySetupType,
	exportFlag As Boolean,
	propertySetName As String
)
```

```
public:
void AddPropertySet(
	PropertySetupType propertySetupType, 
	bool exportFlag, 
	String^ propertySetName
)
```

```
member AddPropertySet : 
        propertySetupType : PropertySetupType * 
        exportFlag : bool * 
        propertySetName : string -> unit 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
:   The property setup type.

exportFlag Boolean
:   The flag that indicates whether the property set is included in export.

propertySetName String
:   The property set name.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | A property set with the given name already exists in the template. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
