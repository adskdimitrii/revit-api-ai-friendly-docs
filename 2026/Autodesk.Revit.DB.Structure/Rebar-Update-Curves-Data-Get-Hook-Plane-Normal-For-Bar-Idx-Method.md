# Rebar Update Curves Data Get Hook Plane Normal For Bar Idx Method

Source: https://www.revitapidocs.com/2026/ff212171-e964-2045-42f8-1519762cff43.htm

---

| Rebar Update Curves Data Get Hook Plane Normal For Bar Idx Method |
| --- |

**Note: This API is now obsolete.** 

Returns the plane's normal in which the termination at end of bar with index barPositionIndex that is currently in Rebar.
 The normal is used for both hook and crank. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.GetTerminationPlaneNormalForBarIdx instead.")]
public XYZ GetHookPlaneNormalForBarIdx(
	int end,
	int barPositionIndex
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.GetTerminationPlaneNormalForBarIdx instead.")>
Public Function GetHookPlaneNormalForBarIdx ( 
	end As Integer,
	barPositionIndex As Integer
) As XYZ
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.GetTerminationPlaneNormalForBarIdx instead.")]
XYZ^ GetHookPlaneNormalForBarIdx(
	int end, 
	int barPositionIndex
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.GetTerminationPlaneNormalForBarIdx instead.")>]
member GetHookPlaneNormalForBarIdx : 
        end : int * 
        barPositionIndex : int -> XYZ 
```

#### Parameters

end Int32
:   The end of bar. Should be 0 for start or 1 for end.

barPositionIndex Int32
:   An index between 0 and (GetNumberOfBars()\-1\).

#### Return Value

[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm) 
The plane's normal in which the termination (e.g. hook, crank) at end of bar with index barPositionIndex that is currently in Rebar.
 The normal is used for both hook and crank. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex is not in the range \[ 0, GetNumberOfBars()\-1 ].  \-or\-  Invalid end. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarUpdateCurvesData Class](Rebar-Update-Curves-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
