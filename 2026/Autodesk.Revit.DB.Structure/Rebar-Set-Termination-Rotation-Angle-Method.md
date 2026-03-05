# Rebar Set Termination Rotation Angle Method

Source: https://www.revitapidocs.com/2026/e77ff36b-b28c-8022-b714-ac0e6511cb01.htm

---

| Rebar Set Termination Rotation Angle Method |
| --- |

Sets the termination's (e.g hook, crank) out of plane rotation angle at the specified end. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetTerminationRotationAngle(
	int end,
	double rotationAngle
)
```

```
Public Sub SetTerminationRotationAngle ( 
	end As Integer,
	rotationAngle As Double
)
```

```
public:
void SetTerminationRotationAngle(
	int end, 
	double rotationAngle
)
```

```
member SetTerminationRotationAngle : 
        end : int * 
        rotationAngle : float -> unit 
```

#### Parameters

end Int32
:   0 for the start, 1 for the end.

rotationAngle Double
:   The termination's (e.g hook, crank) out of plane rotation angle at the specified end.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for rotationAngle is not finite |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
