# IFCParameter Template Clear Property Sets Method

Source: https://www.revitapidocs.com/2026/66847d13-a609-806d-f915-6f1f53a2960c.htm

---

| IFCParameter Template Clear Property Sets Method |
| --- |

Removes all property sets from the template. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void ClearPropertySets(
	PropertySetupType propertySetupType
)
```

```
Public Sub ClearPropertySets ( 
	propertySetupType As PropertySetupType
)
```

```
public:
void ClearPropertySets(
	PropertySetupType propertySetupType
)
```

```
member ClearPropertySets : 
        propertySetupType : PropertySetupType -> unit 
```

#### Parameters

propertySetupType [PropertySetupType](Property-Setup-Type-Enumeration.md)
:   The property setup type.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCParameterTemplate Class](IFCParameter-Template-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
