# Rebar Set Hook Rotation Angle Method

Source: https://www.revitapidocs.com/2026/399efb81-f360-4e7b-bbc3-938325f0baba.htm

---

| Rebar Set Hook Rotation Angle Method |
| --- |

**Note: This API is now obsolete.** 

Sets the terminitation's out of plane hook rotation angle at the specified end. The rotation angle it's the same for both hook and crank. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.SetTerminationRotationAngle instead.")]
public void SetHookRotationAngle(
	double rotationAngle,
	int end
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.SetTerminationRotationAngle instead.")>
Public Sub SetHookRotationAngle ( 
	rotationAngle As Double,
	end As Integer
)
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.SetTerminationRotationAngle instead.")]
void SetHookRotationAngle(
	double rotationAngle, 
	int end
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use Rebar.SetTerminationRotationAngle instead.")>]
member SetHookRotationAngle : 
        rotationAngle : float * 
        end : int -> unit 
```

#### Parameters

rotationAngle Double
:   The termination's out of plane rotation angle at the specified end. The rotation angle it's the same for both hook and crank.

end Int32
:   0 for the start, 1 for the end.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for rotationAngle is not finite |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
