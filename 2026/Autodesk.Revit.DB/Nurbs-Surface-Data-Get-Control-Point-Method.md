# Nurbs Surface Data Get Control Point Method

Source: https://www.revitapidocs.com/2026/d8a259a6-4ada-a397-b7a1-52ba6d742d11.htm

---

| Nurbs Surface Data Get Control Point Method |
| --- |

Get the list of control points. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public XYZ GetControlPoint(
	int idx
)
```

```
Public Function GetControlPoint ( 
	idx As Integer
) As XYZ
```

```
public:
XYZ^ GetControlPoint(
	int idx
)
```

```
member GetControlPoint : 
        idx : int -> XYZ 
```

#### Parameters

idx Int32
:   The index of the control point.

#### Return Value

[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Out\-of\-range access. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[NurbsSurfaceData Class](Nurbs-Surface-Data-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
