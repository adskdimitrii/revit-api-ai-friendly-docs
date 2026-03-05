# Rebar Update Curves Data Set Termination Rotation Angle Method

Source: https://www.revitapidocs.com/2026/8e53f5b2-e370-f5f5-7ab6-e55bf09a9b42.htm

---

| Rebar Update Curves Data Set Termination Rotation Angle Method |
| --- |

Sets the termination's (e.g hook, crank) rotation angle (in radians) at end. This information is set to the rebar after the API execution is finished successfully. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetTerminationRotationAngle(
	int end,
	double angle
)
```

```
Public Sub SetTerminationRotationAngle ( 
	end As Integer,
	angle As Double
)
```

```
public:
void SetTerminationRotationAngle(
	int end, 
	double angle
)
```

```
member SetTerminationRotationAngle : 
        end : int * 
        angle : float -> unit 
```

#### Parameters

end Int32
:   The end of bar. Should be 0 for start or 1 for end.

angle Double
:   The termination's (e.g hook, crank) rotation angle (in radians) at end.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for angle is not finite |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Invalid end. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarUpdateCurvesData Class](Rebar-Update-Curves-Data-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
