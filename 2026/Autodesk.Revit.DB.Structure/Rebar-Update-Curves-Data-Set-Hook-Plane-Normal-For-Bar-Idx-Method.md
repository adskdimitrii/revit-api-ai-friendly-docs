# Rebar Update Curves Data Set Hook Plane Normal For Bar Idx Method

Source: https://www.revitapidocs.com/2026/e639b633-d0c2-3913-dad4-ad9fde83fc32.htm

---

| Rebar Update Curves Data Set Hook Plane Normal For Bar Idx Method |
| --- |

**Note: This API is now obsolete.** 

Sets the plane's normal in which the termination at end of bar with index barPositionIndex will stay.
 The normal will be used for both hook and crank.
 This information is set to the rebar after the API execution is finished successfully. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.SetTerminationPlaneNormalForBarIdx instead.")]
public void SetHookPlaneNormalForBarIdx(
	int end,
	int barPositionIndex,
	XYZ terminationPlaneNormal
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.SetTerminationPlaneNormalForBarIdx instead.")>
Public Sub SetHookPlaneNormalForBarIdx ( 
	end As Integer,
	barPositionIndex As Integer,
	terminationPlaneNormal As XYZ
)
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.SetTerminationPlaneNormalForBarIdx instead.")]
void SetHookPlaneNormalForBarIdx(
	int end, 
	int barPositionIndex, 
	XYZ^ terminationPlaneNormal
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.SetTerminationPlaneNormalForBarIdx instead.")>]
member SetHookPlaneNormalForBarIdx : 
        end : int * 
        barPositionIndex : int * 
        terminationPlaneNormal : XYZ -> unit 
```

#### Parameters

end Int32
:   The end of bar. Should be 0 for start or 1 for end.

barPositionIndex Int32
:   Index of the bar for which it will set the termination's plane normal.

terminationPlaneNormal [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The plane's normal in which the termination at end of bar with index barPositionIndex will stay.
 The normal will be used for both hook and crank.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Invalid end.  \-or\-  terminationPlaneNormal has zero length. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This information is set to the rebar after the API execution is finished successfully. Before setting the value a validation will be done.
 We consider a termination plane normal valid if it's perpendicular with the bar direction at end. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarUpdateCurvesData Class](Rebar-Update-Curves-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
