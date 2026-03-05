# Rebar Bar Type Set Crank Straight Length Method

Source: https://www.revitapidocs.com/2026/a4ff1243-7bac-7099-cd13-ea5e554bfee1.htm

---

| Rebar Bar Type Set Crank Straight Length Method |
| --- |

Sets the crank straigh length for the specified Rebar Crank Type. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetCrankStraightLength(
	ElementId rebarCrankTypeId,
	double crankStraightLength
)
```

```
Public Sub SetCrankStraightLength ( 
	rebarCrankTypeId As ElementId,
	crankStraightLength As Double
)
```

```
public:
void SetCrankStraightLength(
	ElementId^ rebarCrankTypeId, 
	double crankStraightLength
)
```

```
member SetCrankStraightLength : 
        rebarCrankTypeId : ElementId * 
        crankStraightLength : float -> unit 
```

#### Parameters

rebarCrankTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Crank Type id.
 Interactions with Rebar Crank Types can be done with the functions in \[!:Autodesk::Revit::DB::Structure::RebarCrankTypeUtils] .

crankStraightLength Double
:   The new value of the crank straight length.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarCrankTypeId doesn't represent a valid Rebar Crank Type. It should be an ElementType of BuiltInCategory.OST\_RebarCrankType category.  \-or\-  For the specified Rebar Crank Type is auto calculated and the cannot be manually set.  \-or\-  The crank parameters cannot be computed for the specified crankStraightLength and Rebar Crank Type. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for crankStraightLength must be positive. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks When the crank straight length is set, the crank ratio is keeping the same value. The offset length and angled length are adjusted. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBarType Class](Rebar-Bar-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
