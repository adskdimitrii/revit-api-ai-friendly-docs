# Rebar Get Parameter Value At Index Method

Source: https://www.revitapidocs.com/2026/d4d5a126-4e14-8fda-bbb9-2178b7162486.htm

---

| Rebar Get Parameter Value At Index Method |
| --- |

Get the parameter value for a bar at the specified index. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ParameterValue GetParameterValueAtIndex(
	ElementId paramId,
	int barPositionIndex
)
```

```
Public Function GetParameterValueAtIndex ( 
	paramId As ElementId,
	barPositionIndex As Integer
) As ParameterValue
```

```
public:
ParameterValue^ GetParameterValueAtIndex(
	ElementId^ paramId, 
	int barPositionIndex
)
```

```
member GetParameterValueAtIndex : 
        paramId : ElementId * 
        barPositionIndex : int -> ParameterValue 
```

#### Parameters

paramId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The parameter Id.

barPositionIndex Int32
:   The bar index in the rebar distribution. Accepts only values between 0 and NumberOfBarPositions\-1\.

#### Return Value

[ParameterValue](366521ef-ecc2-c3e3-feb5-81b3bbd8df0c.htm) 
The ParameterValue for given parameterId and barPositionIndex. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barPositionIndex should be in range \[ 0, NumberOfBarPositions\-1 ] and the bar at barPositionIndex should be included. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks For rebar sets which don't have varying length bars the returned ParameterValue is the same no matter the index.
 For rebar sets which have varying length bars the returned ParameterValue is evaluated at the given index. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
