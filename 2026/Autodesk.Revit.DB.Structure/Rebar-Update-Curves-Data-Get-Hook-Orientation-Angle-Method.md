# Rebar Update Curves Data Get Hook Orientation Angle Method

Source: https://www.revitapidocs.com/2026/50bd6278-bbb7-7b6c-029d-e34f7b42ddb9.htm

---

| Rebar Update Curves Data Get Hook Orientation Angle Method |
| --- |

**Note: This API is now obsolete.** 

Get the termination's rotation angle at end that is currently in the rebar.
 The angle is used for both hook and crank. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.GetTerminationRotationAngle instead.")]
public double GetHookOrientationAngle(
	int end
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.GetTerminationRotationAngle instead.")>
Public Function GetHookOrientationAngle ( 
	end As Integer
) As Double
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.GetTerminationRotationAngle instead.")]
double GetHookOrientationAngle(
	int end
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.GetTerminationRotationAngle instead.")>]
member GetHookOrientationAngle : 
        end : int -> float 
```

#### Parameters

end Int32
:   The end of bar. Should be 0 for start or 1 for end.

#### Return Value

Double 
The rotation angle at end that is currently in the rebar. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Invalid end. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarUpdateCurvesData Class](Rebar-Update-Curves-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
