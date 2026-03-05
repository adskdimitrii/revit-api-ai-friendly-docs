# Solid Utils Compute Is Topologically Closed Method

Source: https://www.revitapidocs.com/2026/4849b82c-a63d-db1b-89f5-d306b4351a04.htm

---

| Solid Utils Compute Is Topologically Closed Method |
| --- |

Compute whether the input Solid is topologically closed. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static bool ComputeIsTopologicallyClosed(
	Solid geometry
)
```

```
Public Shared Function ComputeIsTopologicallyClosed ( 
	geometry As Solid
) As Boolean
```

```
public:
static bool ComputeIsTopologicallyClosed(
	Solid^ geometry
)
```

```
static member ComputeIsTopologicallyClosed : 
        geometry : Solid -> bool 
```

#### Parameters

geometry [Solid](7a3b5ac1-c66d-9f81-a11d-9bcd4e026295.htm)
:   The solid or shell geometry to test.

#### Return Value

Boolean 
True if the geometry is topologically closed, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A solid is topologically closed if every face has at least one edge loop and
 every edge is shared by exactly two faces. If the geometry contains multiple
 connected components, the function returns true if and only if every connected
 component is topologically closed. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[SolidUtils Class](Solid-Utils-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
