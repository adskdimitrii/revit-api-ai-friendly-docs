# Rebar Shape Is Same Shape Ignoring Hooks Method

Source: https://www.revitapidocs.com/2026/5815937c-ac80-2f85-ff5a-4e728336251e.htm

---

| Rebar Shape Is Same Shape Ignoring Hooks Method |
| --- |

**Note: This API is now obsolete.** 

Test whether two shapes have equivalent definitions by comparing
 the RebarShapeDefinition and MultiplanarDefinition properties. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.IsSameShapeIgnoringTerminations instead.")]
public bool IsSameShapeIgnoringHooks(
	RebarShape otherShape
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.IsSameShapeIgnoringTerminations instead.")>
Public Function IsSameShapeIgnoringHooks ( 
	otherShape As RebarShape
) As Boolean
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.IsSameShapeIgnoringTerminations instead.")]
bool IsSameShapeIgnoringHooks(
	RebarShape^ otherShape
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.IsSameShapeIgnoringTerminations instead.")>]
member IsSameShapeIgnoringHooks : 
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
