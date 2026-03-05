# Rebar Get Crank Ratio Method

Source: https://www.revitapidocs.com/2026/43e99051-697b-e79c-4650-c5f596a23162.htm

---

| Rebar Get Crank Ratio Method |
| --- |

Gets the crank ratio at the indicated bar end. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double GetCrankRatio(
	int end
)
```

```
Public Function GetCrankRatio ( 
	end As Integer
) As Double
```

```
public:
double GetCrankRatio(
	int end
)
```

```
member GetCrankRatio : 
        end : int -> float 
```

#### Parameters

end Int32
:   The bar end.

#### Return Value

Double 
Returns the crank ratio. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The bar does not have a valid Rebar Crank Type at the end. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The crank slope is 1/crankRatio.
 If the crank lengths are overriden will return the overriden value. Otherwise will return the value from the RebarBarType for the existing Crank Type. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
