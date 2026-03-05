# IFCParameter Template Is Property Set AMember Of Template Method

Source: https://www.revitapidocs.com/2026/1d036e8a-64f8-dff2-7d49-789287137f14.htm

---

| IFCParameter Template Is Property Set AMember Of Template Method |
| --- |

Checks whether a property set exists in the template. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool IsPropertySetAMemberOfTemplate(
	PropertySetupType propertySetupType,
	string propertySetName
)
```

```
Public Function IsPropertySetAMemberOfTemplate ( 
	propertySetupType As PropertySetupType,
	propertySetName As String
) As Boolean
```

```
public:
bool IsPropertySetAMemberOfTemplate(
	PropertySetupType propertySetupType, 
	String^ propertySetName
)
```

```
member IsPropertySetAMemberOfTemplate : 
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
True if the property set exists in the template. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
