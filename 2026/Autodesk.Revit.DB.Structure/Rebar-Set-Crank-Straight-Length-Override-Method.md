# Rebar Set Crank Straight Length Override Method

Source: https://www.revitapidocs.com/2026/1124fea9-d45d-83de-6e9a-d0a786b018ba.htm

---

| Rebar Set Crank Straight Length Override Method |
| --- |

Sets the crank straight length at the indicated bar end as an override value. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetCrankStraightLengthOverride(
	int end,
	double crankStraightLength
)
```

```
Public Sub SetCrankStraightLengthOverride ( 
	end As Integer,
	crankStraightLength As Double
)
```

```
public:
void SetCrankStraightLengthOverride(
	int end, 
	double crankStraightLength
)
```

```
member SetCrankStraightLengthOverride : 
        end : int * 
        crankStraightLength : float -> unit 
```

#### Parameters

end Int32
:   The bar end.

crankStraightLength Double
:   The crank straigth length.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The bar does not have a valid Rebar Crank Type at the end.  \-or\-  The ability to override crank lengths is not enabled for this rebar instance. Use enableCrankLengthOverride(true) to enable it. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks When the crank straight length is set, the crank ratio is keeping the same value. The offset length and angled length are adjusted. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
