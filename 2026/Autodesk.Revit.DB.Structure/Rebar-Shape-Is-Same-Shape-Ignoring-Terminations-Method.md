# Rebar Shape Is Same Shape Ignoring Terminations Method

Source: https://www.revitapidocs.com/2026/5db9cdfe-9e7d-b6f5-9a81-563602eb45d6.htm

---

| Rebar Shape Is Same Shape Ignoring Terminations Method |
| --- |

Test whether two shapes have equivalent definitions by comparing
 the RebarShapeDefinition and MultiplanarDefinition properties. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool IsSameShapeIgnoringTerminations(
	RebarShape otherShape
)
```

```
Public Function IsSameShapeIgnoringTerminations ( 
	otherShape As RebarShape
) As Boolean
```

```
public:
bool IsSameShapeIgnoringTerminations(
	RebarShape^ otherShape
)
```

```
member IsSameShapeIgnoringTerminations : 
        otherShape : RebarShape -> bool 
```

#### Parameters

otherShape [RebarShape](Rebar-Shape-Class.md)
:   Another shape to be compared to this one.

#### Return Value

Boolean 
True if the shape definitions match, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This method will return true if the definitions are exactly equivalent.
 The hooks, cranks, end treatments, orientations and terminations' rotation angles are ignored. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShape Class](Rebar-Shape-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
