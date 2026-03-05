# Rebar Update Curves Data Set Hook Orientation Angle Method

Source: https://www.revitapidocs.com/2026/182e024d-55e6-24e7-4125-a1288a2cb7a1.htm

---

| Rebar Update Curves Data Set Hook Orientation Angle Method |
| --- |

**Note: This API is now obsolete.** 

Sets the termination's rotation angle at end.
 The angle will be used for both hook and crank.
 This information is set to the rebar after the API execution is finished successfully. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.SetTerminationRotationAngle instead.")]
public void SetHookOrientationAngle(
	int end,
	double angle
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.SetTerminationRotationAngle instead.")>
Public Sub SetHookOrientationAngle ( 
	end As Integer,
	angle As Double
)
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.SetTerminationRotationAngle instead.")]
void SetHookOrientationAngle(
	int end, 
	double angle
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarUpdateCurvesData.SetTerminationRotationAngle instead.")>]
member SetHookOrientationAngle : 
        end : int * 
        angle : float -> unit 
```

#### Parameters

end Int32
:   The end of bar. Should be 0 for start or 1 for end.

angle Double
:   The termination's rotation angle at end.
 The angle will be used for both hook and crank.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for angle is not finite |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Invalid end. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarUpdateCurvesData Class](Rebar-Update-Curves-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
