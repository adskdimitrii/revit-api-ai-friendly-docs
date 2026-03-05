# Rebar Get Termination Rotation Angle Method

Source: https://www.revitapidocs.com/2026/c3c64e0d-6663-b8c0-6fab-25416e3fd34f.htm

---

| Rebar Get Termination Rotation Angle Method |
| --- |

Gets the termination's (e.g hook, crank) out of plane rotation angle at the specified end. 
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
:   0 for the start, 1 for the end.

#### Return Value

Double 
Returns the termination's (e.g hook, crank) out of plane rotation angle at the specified end. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
