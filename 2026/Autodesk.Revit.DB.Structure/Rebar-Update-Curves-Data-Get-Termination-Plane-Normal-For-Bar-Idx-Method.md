# Rebar Update Curves Data Get Termination Plane Normal For Bar Idx Method

Source: https://www.revitapidocs.com/2026/4126016a-2405-8ce2-4225-f17d9329453e.htm

---

| Rebar Update Curves Data Get Termination Plane Normal For Bar Idx Method |
| --- |

Gets the plane's normal in which the termination (e.g. hook, crank) at end of bar with index barPositionIndex that is currently in Rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public XYZ GetTerminationPlaneNormalForBarIdx(
	int end,
	int barPositionIndex
)
```

```
Public Function GetTerminationPlaneNormalForBarIdx ( 
	end As Integer,
	barPositionIndex As Integer
) As XYZ
```

```
public:
XYZ^ GetTerminationPlaneNormalForBarIdx(
	int end, 
	int barPositionIndex
)
```

```
member GetTerminationPlaneNormalForBarIdx : 
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
Returns the plane's normal in which the termination (e.g. hook, crank) at end of bar with index barPositionIndex that is currently in Rebar. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex is not in the range \[ 0, GetNumberOfBars()\-1 ].  \-or\-  Invalid end. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This method does not take into account the rotation of the bar relative to its default position along the distribution path. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarUpdateCurvesData Class](Rebar-Update-Curves-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
