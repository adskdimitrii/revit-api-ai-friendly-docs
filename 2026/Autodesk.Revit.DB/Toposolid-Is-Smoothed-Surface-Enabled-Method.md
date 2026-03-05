# Toposolid Is Smoothed Surface Enabled Method

Source: https://www.revitapidocs.com/2026/96dbefd0-7927-7a7e-dd50-536eb6c56e88.htm

---

| Toposolid Is Smoothed Surface Enabled Method |
| --- |

Gets smoothed surface setting of Toposolid. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static bool IsSmoothedSurfaceEnabled(
	Document document
)
```

```
Public Shared Function IsSmoothedSurfaceEnabled ( 
	document As Document
) As Boolean
```

```
public:
static bool IsSmoothedSurfaceEnabled(
	Document^ document
)
```

```
static member IsSmoothedSurfaceEnabled : 
        document : Document -> bool 
```

#### Parameters

document [Document](Document-Class.md)
:   The document.

#### Return Value

Boolean 
True if smoothed surface is enabled for Toposolid, otherwise return false. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Toposolid Class](Toposolid-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
