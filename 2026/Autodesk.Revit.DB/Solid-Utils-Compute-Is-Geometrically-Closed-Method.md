# Solid Utils Compute Is Geometrically Closed Method

Source: https://www.revitapidocs.com/2026/33ffdb0e-fab6-6f12-bd99-6b12ce6ad9cc.htm

---

| Solid Utils Compute Is Geometrically Closed Method |
| --- |

Computes whether the input Solid is geometrically closed to within Revit's tolerances. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static bool ComputeIsGeometricallyClosed(
	Solid geometry
)
```

```
Public Shared Function ComputeIsGeometricallyClosed ( 
	geometry As Solid
) As Boolean
```

```
public:
static bool ComputeIsGeometricallyClosed(
	Solid^ geometry
)
```

```
static member ComputeIsGeometricallyClosed : 
        geometry : Solid -> bool 
```

#### Parameters

geometry [Solid](7a3b5ac1-c66d-9f81-a11d-9bcd4e026295.htm)
:   The solid or shell geometry to test.

#### Return Value

Boolean 
True if the geometry is geometrically closed, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to compute whether the geometry is geometrically closed. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A solid is geometrically closed if it is topologically closed and also meets certain
 geometric criteria. In particular, every pair of faces adjoining an edge must intersect
 along the edge, and edge loops must have no gaps between consecutive edges of the loop,
 when evaluated on the edge loop's face.
 If the geometry contains multiple connected components, the function returns true
 if and only if every connected component is geometrically closed. If the input Solid
 contains grossly invalid geometry, an InvalidOperationException will be thrown. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[SolidUtils Class](Solid-Utils-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
