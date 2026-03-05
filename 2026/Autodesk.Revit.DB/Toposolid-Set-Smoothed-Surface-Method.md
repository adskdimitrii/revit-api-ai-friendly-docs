# Toposolid Set Smoothed Surface Method

Source: https://www.revitapidocs.com/2026/a565b8eb-196a-415d-3826-81b58d1e4018.htm

---

| Toposolid Set Smoothed Surface Method |
| --- |

Sets smoothed surface setting of Toposolid. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static void SetSmoothedSurface(
	Document document,
	bool enable
)
```

```
Public Shared Sub SetSmoothedSurface ( 
	document As Document,
	enable As Boolean
)
```

```
public:
static void SetSmoothedSurface(
	Document^ document, 
	bool enable
)
```

```
static member SetSmoothedSurface : 
        document : Document * 
        enable : bool -> unit 
```

#### Parameters

document [Document](Document-Class.md)
:   The document.

enable Boolean
:   True means enable smoothed surface setting, otherwise disable.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Toposolid Class](Toposolid-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
