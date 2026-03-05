# Rebar Set Crank Length Override Method

Source: https://www.revitapidocs.com/2026/5ed493ae-0f3d-bca2-0c8e-c71366220221.htm

---

| Rebar Set Crank Length Override Method |
| --- |

Sets the crank length at the indicated bar end as an override value. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetCrankLengthOverride(
	int end,
	double crankLength
)
```

```
Public Sub SetCrankLengthOverride ( 
	end As Integer,
	crankLength As Double
)
```

```
public:
void SetCrankLengthOverride(
	int end, 
	double crankLength
)
```

```
member SetCrankLengthOverride : 
        end : int * 
        crankLength : float -> unit 
```

#### Parameters

end Int32
:   The bar end.

crankLength Double
:   The crank length.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The bar does not have a valid Rebar Crank Type at the end.  \-or\-  The ability to override crank lengths is not enabled for this rebar instance. Use enableCrankLengthOverride(true) to enable it. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
