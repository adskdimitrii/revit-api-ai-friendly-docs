# Rebar Free Form Accessor Get Termination Plane Normal For Bar Index Method

Source: https://www.revitapidocs.com/2026/5b8bc12b-dee4-a901-abf4-13a9bebcdb52.htm

---

| Rebar Free Form Accessor Get Termination Plane Normal For Bar Index Method |
| --- |

Gets the plane's normal in which the termination (e.g. hook, crank) at end of bar with index barPositionIndex will stay. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public XYZ GetTerminationPlaneNormalForBarIndex(
	int end,
	int barPositionIndex
)
```

```
Public Function GetTerminationPlaneNormalForBarIndex ( 
	end As Integer,
	barPositionIndex As Integer
) As XYZ
```

```
public:
XYZ^ GetTerminationPlaneNormalForBarIndex(
	int end, 
	int barPositionIndex
)
```

```
member GetTerminationPlaneNormalForBarIndex : 
        end : int * 
        barPositionIndex : int -> XYZ 
```

#### Parameters

end Int32
:   The end of bar. Should be 0 for start or 1 for end.

barPositionIndex Int32
:   An index between 0 and (NumberOfBarPositions\-1\).

#### Return Value

[XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm) 
Returns the plane's normal in which the termination (e.g. hook, crank) at end of bar with index barPositionIndex will stay. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex is not in the range \[ 0, NumberOfBarPositions\-1 ].  \-or\-  Invalid end. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This method does not take into account the rotation of the bar relative to its default position along the distribution path. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarFreeFormAccessor Class](Rebar-Free-Form-Accessor-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
