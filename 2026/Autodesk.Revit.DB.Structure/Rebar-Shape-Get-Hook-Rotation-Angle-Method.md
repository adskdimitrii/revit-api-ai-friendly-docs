# Rebar Shape Get Hook Rotation Angle Method

Source: https://www.revitapidocs.com/2026/76a3c46d-031e-37c6-d8c2-3342a60d8bc5.htm

---

| Rebar Shape Get Hook Rotation Angle Method |
| --- |

**Note: This API is now obsolete.** 

Gets the termination's (e.g hook, crank) out of plane rotation angle at the specified end.
 The angle is used for both hook and crank. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().TerminationRotationAngleAtStart or RebarShape.GetTerminationsData().TerminationRotationAngleAtEnd instead.")]
public double GetHookRotationAngle(
	int end
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().TerminationRotationAngleAtStart or RebarShape.GetTerminationsData().TerminationRotationAngleAtEnd instead.")>
Public Function GetHookRotationAngle ( 
	end As Integer
) As Double
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().TerminationRotationAngleAtStart or RebarShape.GetTerminationsData().TerminationRotationAngleAtEnd instead.")]
double GetHookRotationAngle(
	int end
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().TerminationRotationAngleAtStart or RebarShape.GetTerminationsData().TerminationRotationAngleAtEnd instead.")>]
member GetHookRotationAngle : 
        end : int -> float 
```

#### Parameters

end Int32
:   0 for the start, 1 for the end.

#### Return Value

Double 
Returns the termination's (e.g hook, crank) out of plane rotation angle at the specified end.
 The angle is used for both hook and crank. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShape Class](Rebar-Shape-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
