# Rebar Bar Type Can Crank Parameters Be Computed Using Crank Angled Length Method

Source: https://www.revitapidocs.com/2026/80384dda-ebad-5c12-c335-d9a960409809.htm

---

| Rebar Bar Type Can Crank Parameters Be Computed Using Crank Angled Length Method |
| --- |

Identifies if the all crank parameters can be computed for the specified crank angled length and Rebar Crank Type. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool CanCrankParametersBeComputedUsingCrankAngledLength(
	ElementId rebarCrankTypeId,
	double crankAngledLength
)
```

```
Public Function CanCrankParametersBeComputedUsingCrankAngledLength ( 
	rebarCrankTypeId As ElementId,
	crankAngledLength As Double
) As Boolean
```

```
public:
bool CanCrankParametersBeComputedUsingCrankAngledLength(
	ElementId^ rebarCrankTypeId, 
	double crankAngledLength
)
```

```
member CanCrankParametersBeComputedUsingCrankAngledLength : 
        rebarCrankTypeId : ElementId * 
        crankAngledLength : float -> bool 
```

#### Parameters

rebarCrankTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Crank Type id.
 Interactions with Rebar Crank Types can be done with the functions in \[!:Autodesk::Revit::DB::Structure::RebarCrankTypeUtils] .

crankAngledLength Double
:   The value of the crank angled length to be tested.

#### Return Value

Boolean 
Returns true if the crank paramters can be computed using the input crank angled length, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarCrankTypeId doesn't represent a valid Rebar Crank Type. It should be an ElementType of BuiltInCategory.OST\_RebarCrankType category. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBarType Class](Rebar-Bar-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
