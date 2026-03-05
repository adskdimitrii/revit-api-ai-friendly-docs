# Nurbs Surface Data Get Knot V Method

Source: https://www.revitapidocs.com/2026/6f0ee09b-1506-2b16-3679-bc363c09bc5e.htm

---

| Nurbs Surface Data Get Knot V Method |
| --- |

Get the knot in the v\-direction. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double GetKnotV(
	int idx
)
```

```
Public Function GetKnotV ( 
	idx As Integer
) As Double
```

```
public:
double GetKnotV(
	int idx
)
```

```
member GetKnotV : 
        idx : int -> float 
```

#### Parameters

idx Int32
:   The index of the knot.

#### Return Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Out\-of\-range access. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[NurbsSurfaceData Class](Nurbs-Surface-Data-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
