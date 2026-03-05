# Nurbs Surface Data Get Weight Method

Source: https://www.revitapidocs.com/2026/7dfeae66-3fc4-08b1-a00f-4f1eb8317d69.htm

---

| Nurbs Surface Data Get Weight Method |
| --- |

Get the weight. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double GetWeight(
	int idx
)
```

```
Public Function GetWeight ( 
	idx As Integer
) As Double
```

```
public:
double GetWeight(
	int idx
)
```

```
member GetWeight : 
        idx : int -> float 
```

#### Parameters

idx Int32
:   The index of the weight.

#### Return Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Out\-of\-range access. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[NurbsSurfaceData Class](Nurbs-Surface-Data-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
