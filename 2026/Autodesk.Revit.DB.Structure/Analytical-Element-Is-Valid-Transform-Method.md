# Analytical Element Is Valid Transform Method

Source: https://www.revitapidocs.com/2026/4c5b9a26-118a-d022-e2ff-bf9a2c4a9c3a.htm

---

| Analytical Element Is Valid Transform Method |
| --- |

Checks whether the value set for Local Coordinate System is valid for an Analytical Element. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool IsValidTransform(
	Transform trf
)
```

```
Public Function IsValidTransform ( 
	trf As Transform
) As Boolean
```

```
public:
bool IsValidTransform(
	Transform^ trf
)
```

```
member IsValidTransform : 
        trf : Transform -> bool 
```

#### Parameters

trf [Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)
:   The value set to be verified.

#### Return Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Origin should be equal with Origin from [GetTransform](23e0c0f8-3f72-235e-0b1f-b977bbe5d697.htm) Z axis should be parallel with Analytical Element's plane's normal.
 X and Y axis should be in Analytical Element's plane.
 For non\-planar elements the X or Y axis should be tangent at transform origin. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[AnalyticalElement Class](Analytical-Element-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
