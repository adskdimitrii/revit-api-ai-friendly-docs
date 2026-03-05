# Rebar Set Crank Ratio Override Method

Source: https://www.revitapidocs.com/2026/e809888e-986a-df5a-b4b6-1084425ef60b.htm

---

| Rebar Set Crank Ratio Override Method |
| --- |

Sets the crank ratio at the indicated bar end as an override value. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetCrankRatioOverride(
	int end,
	double crankRatio
)
```

```
Public Sub SetCrankRatioOverride ( 
	end As Integer,
	crankRatio As Double
)
```

```
public:
void SetCrankRatioOverride(
	int end, 
	double crankRatio
)
```

```
member SetCrankRatioOverride : 
        end : int * 
        crankRatio : float -> unit 
```

#### Parameters

end Int32
:   The bar end.

crankRatio Double
:   The crank ratio.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The bar does not have a valid Rebar Crank Type at the end.  \-or\-  The ability to override crank lengths is not enabled for this rebar instance. Use enableCrankLengthOverride(true) to enable it. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The crank slope is 1/crankRatio.
 When the crank ratio is set, the crank offset length is keeping the same value. The angled length and straight length are adjusted. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
