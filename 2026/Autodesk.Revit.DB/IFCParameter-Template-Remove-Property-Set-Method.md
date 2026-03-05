# IFCParameter Template Remove Property Set Method

Source: https://www.revitapidocs.com/2026/f2bb1b32-a880-619b-9c7c-a92fc491e32a.htm

---

| IFCParameter Template Remove Property Set Method |
| --- |

Removes provided property set from the template. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void RemovePropertySet(
	PropertySetupType propertySetupType,
	string propertySetName
)
```

```
Public Sub RemovePropertySet ( 
	propertySetupType As PropertySetupType,
	propertySetName As String
)
```

```
public:
void RemovePropertySet(
	PropertySetupType propertySetupType, 
	String^ propertySetName
)
```

```
member RemovePropertySet : 
        propertySetupType : PropertySetupType * 
        propertySetName : string -> unit 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
:   The property setup type.

propertySetName String
:   The property set name.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | A property set with the given name is not present in the template. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
