# Rebar Free Form Accessor Can Be Hook Normal Method

Source: https://www.revitapidocs.com/2026/3848f3d8-f2f3-fca8-66af-9122d00b3869.htm

---

| Rebar Free Form Accessor Can Be Hook Normal Method |
| --- |

**Note: This API is now obsolete.** 

A vector can be termination's (e.g. hook, crank) normal if for a bar specified by index, the bar direction is not parallel with the vector. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarFreeFormAccessor.CanBeTerminationPlaneNormal instead.")]
public bool CanBeHookNormal(
	int barIndex,
	int end,
	XYZ normal
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarFreeFormAccessor.CanBeTerminationPlaneNormal instead.")>
Public Function CanBeHookNormal ( 
	barIndex As Integer,
	end As Integer,
	normal As XYZ
) As Boolean
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarFreeFormAccessor.CanBeTerminationPlaneNormal instead.")]
bool CanBeHookNormal(
	int barIndex, 
	int end, 
	XYZ^ normal
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarFreeFormAccessor.CanBeTerminationPlaneNormal instead.")>]
member CanBeHookNormal : 
        barIndex : int * 
        end : int * 
        normal : XYZ -> bool 
```

#### Parameters

barIndex Int32
:   The index of bar for which it will try to see if termination's plane normal is applicable.

end Int32
:   The end of bar. Should be 0 for start, 1 for end.

normal [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The teriantion's (e.g. hook, crank) plane normal that will be tested.

#### Return Value

Boolean 
A vector can be termination's (e.g. hook, crank) normal if for a bar specified by index, the bar direction is not parallel with the vector. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barIndex is not in the range \[ 0, NumberOfBarPositions\-1 ].  \-or\-  Invalid end. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarFreeFormAccessor Class](Rebar-Free-Form-Accessor-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
