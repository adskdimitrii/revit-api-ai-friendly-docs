# Rebar Free Form Accessor Set Termination Plane Normal For Bar Index Method

Source: https://www.revitapidocs.com/2026/e9008ca6-ffab-9c00-e366-1797d30e0a7b.htm

---

| Rebar Free Form Accessor Set Termination Plane Normal For Bar Index Method |
| --- |

Sets the plane's normal in which the termination (e.g. hook, crank) at end of bar with index barPositionIndex will stay.
 Will throw exception if the rebar has valid constraints. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetTerminationPlaneNormalForBarIndex(
	int end,
	int barPositionIndex,
	XYZ terminationPlaneNormal
)
```

```
Public Sub SetTerminationPlaneNormalForBarIndex ( 
	end As Integer,
	barPositionIndex As Integer,
	terminationPlaneNormal As XYZ
)
```

```
public:
void SetTerminationPlaneNormalForBarIndex(
	int end, 
	int barPositionIndex, 
	XYZ^ terminationPlaneNormal
)
```

```
member SetTerminationPlaneNormalForBarIndex : 
        end : int * 
        barPositionIndex : int * 
        terminationPlaneNormal : XYZ -> unit 
```

#### Parameters

end Int32
:   The end of bar. Should be 0 for start or 1 for end.

barPositionIndex Int32
:   An index between 0 and (NumberOfBarPositions\-1\).

terminationPlaneNormal [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The plane's normal in which the termination (e.g. hook, crank) at end of bar with index barPositionIndex will stay.
 The normal should be perpendicular to the bar direction at the specified end of bar.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Normal terminationPlaneNormal for end end isn't a valid normal for bar with index barPositionIndex |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex is not in the range \[ 0, NumberOfBarPositions\-1 ].  \-or\-  Invalid end.  \-or\-  terminationPlaneNormal has zero length. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RebarFreeFormAccessor Rebar is constrained. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This method does not take into account the rotation of the bar relative to its default position along the distribution path. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarFreeFormAccessor Class](Rebar-Free-Form-Accessor-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
