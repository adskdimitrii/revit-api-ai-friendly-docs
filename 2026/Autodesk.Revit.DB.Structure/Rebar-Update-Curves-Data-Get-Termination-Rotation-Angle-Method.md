# Rebar Update Curves Data Get Termination Rotation Angle Method

Source: https://www.revitapidocs.com/2026/8d559a4b-b58d-f8a3-1ce5-08e8e81e59f1.htm

---

| Rebar Update Curves Data Get Termination Rotation Angle Method |
| --- |

Gets the termination's (e.g hook, crank) rotation angle (in radians) at end that is currently in the rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double GetTerminationRotationAngle(
	int end
)
```

```
Public Function GetTerminationRotationAngle ( 
	end As Integer
) As Double
```

```
public:
double GetTerminationRotationAngle(
	int end
)
```

```
member GetTerminationRotationAngle : 
        end : int -> float 
```

#### Parameters

end Int32
:   The end of bar. Should be 0 for start or 1 for end.

#### Return Value

Double 
Returns the termination's (e.g hook, crank) rotation angle (in radians) at end that is currently in the rebar. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Invalid end. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarUpdateCurvesData Class](Rebar-Update-Curves-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
