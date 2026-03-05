# Rebar Free Form Accessor Can Be Termination Plane Normal Method

Source: https://www.revitapidocs.com/2026/ebd9c149-79f2-9568-3a06-958146774435.htm

---

| Rebar Free Form Accessor Can Be Termination Plane Normal Method |
| --- |

A vector can be termination (e.g. hook, crank) plane normal if for a bar specified by index, the bar direction is not parallel with the vector. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool CanBeTerminationPlaneNormal(
	int barIndex,
	int end,
	XYZ normal
)
```

```
Public Function CanBeTerminationPlaneNormal ( 
	barIndex As Integer,
	end As Integer,
	normal As XYZ
) As Boolean
```

```
public:
bool CanBeTerminationPlaneNormal(
	int barIndex, 
	int end, 
	XYZ^ normal
)
```

```
member CanBeTerminationPlaneNormal : 
        barIndex : int * 
        end : int * 
        normal : XYZ -> bool 
```

#### Parameters

barIndex Int32
:   The index of bar for which it will try to see if termination plane normal is applicable.

end Int32
:   The end of bar. Should be 0 for start, 1 for end.

normal [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The termination's plane normal that will be tested.

#### Return Value

Boolean 
A vector can be termination (e.g. hook, crank) plane normal if for a bar specified by index, the bar direction is not parallel with the vector. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barIndex is not in the range \[ 0, NumberOfBarPositions\-1 ].  \-or\-  Invalid end. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This method does not take into account the rotation of the bar relative to its default position along the distribution path. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarFreeFormAccessor Class](Rebar-Free-Form-Accessor-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
