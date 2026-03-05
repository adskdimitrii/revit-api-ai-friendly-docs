# Rebar Bar Type Can Crank Parameters Be Computed Using Crank Offset Length Method

Source: https://www.revitapidocs.com/2026/5cda46e3-c3ce-9eb6-7d43-bcfc9424451e.htm

---

| Rebar Bar Type Can Crank Parameters Be Computed Using Crank Offset Length Method |
| --- |

Identifies if the all crank parameters can be computed for the specified crank offset length and Rebar Crank Type. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool CanCrankParametersBeComputedUsingCrankOffsetLength(
	ElementId rebarCrankTypeId,
	double crankOffsetLength
)
```

```
Public Function CanCrankParametersBeComputedUsingCrankOffsetLength ( 
	rebarCrankTypeId As ElementId,
	crankOffsetLength As Double
) As Boolean
```

```
public:
bool CanCrankParametersBeComputedUsingCrankOffsetLength(
	ElementId^ rebarCrankTypeId, 
	double crankOffsetLength
)
```

```
member CanCrankParametersBeComputedUsingCrankOffsetLength : 
        rebarCrankTypeId : ElementId * 
        crankOffsetLength : float -> bool 
```

#### Parameters

rebarCrankTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Crank Type id.
 Interactions with Rebar Crank Types can be done with the functions in \[!:Autodesk::Revit::DB::Structure::RebarCrankTypeUtils] .

crankOffsetLength Double
:   The value of the crank offset length to be tested.

#### Return Value

Boolean 
Returns true if the crank paramters can be computed using the input crank offset length, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarCrankTypeId doesn't represent a valid Rebar Crank Type. It should be an ElementType of BuiltInCategory.OST\_RebarCrankType category. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBarType Class](Rebar-Bar-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
