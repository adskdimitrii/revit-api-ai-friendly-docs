# Rebar Get Crank Length Method

Source: https://www.revitapidocs.com/2026/68a75d49-2bcc-72a4-0219-f72fb7ff7e6b.htm

---

| Rebar Get Crank Length Method |
| --- |

Gets the crank length at the indicated bar end.
 If the crank lengths are overriden will return the overriden value. Otherwise will return the value from the RebarBarType for the existing Crank Type. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public double GetCrankLength(
	int end
)
```

```
Public Function GetCrankLength ( 
	end As Integer
) As Double
```

```
public:
double GetCrankLength(
	int end
)
```

```
member GetCrankLength : 
        end : int -> float 
```

#### Parameters

end Int32
:   The bar end.

#### Return Value

Double 
Returns the crank length. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The bar does not have a valid Rebar Crank Type at the end. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
