# Toposolid Is Cut Void Stability Enabled Method

Source: https://www.revitapidocs.com/2026/edae798c-d914-2d4c-12d5-96cce8f06290.htm

---

| Toposolid Is Cut Void Stability Enabled Method |
| --- |

Identifies if the setting for stability of Boolean operations for Toposolid elements is enabled or disabled. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static bool IsCutVoidStabilityEnabled(
	Document document
)
```

```
Public Shared Function IsCutVoidStabilityEnabled ( 
	document As Document
) As Boolean
```

```
public:
static bool IsCutVoidStabilityEnabled(
	Document^ document
)
```

```
static member IsCutVoidStabilityEnabled : 
        document : Document -> bool 
```

#### Parameters

document [Document](Document-Class.md)
:   The document.

#### Return Value

Boolean 
True means enable cut void stability setting, otherwise disable. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The stability setting increases the chance of cut and void operation success by applying a random shift
 (a hyper\-random testing action where the computer shifts the cut\-void along the x or y axis, starting from the minimum distance).
 Enabling this may slightly impact the accuracy of the geometry.
 When used, the voided geometry is changed, and will be reported in a warning.
 Please note that success cannot be guaranteed for Boolean operations when this setting is enabled. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Toposolid Class](Toposolid-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
