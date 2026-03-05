# Rebar Set Crank Angled Length Override Method

Source: https://www.revitapidocs.com/2026/6667e0a1-7d51-6cb0-222b-c0fa8e8bda20.htm

---

| Rebar Set Crank Angled Length Override Method |
| --- |

Sets the crank angled length at the indicated bar end as an override value. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetCrankAngledLengthOverride(
	int end,
	double crankAngledLength
)
```

```
Public Sub SetCrankAngledLengthOverride ( 
	end As Integer,
	crankAngledLength As Double
)
```

```
public:
void SetCrankAngledLengthOverride(
	int end, 
	double crankAngledLength
)
```

```
member SetCrankAngledLengthOverride : 
        end : int * 
        crankAngledLength : float -> unit 
```

#### Parameters

end Int32
:   The bar end.

crankAngledLength Double
:   The crank angled length.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The bar does not have a valid Rebar Crank Type at the end.  \-or\-  The ability to override crank lengths is not enabled for this rebar instance. Use enableCrankLengthOverride(true) to enable it. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks When the crank angled length is set, the crank ratio is keeping the same value. The offset length and straight length are adjusted. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
