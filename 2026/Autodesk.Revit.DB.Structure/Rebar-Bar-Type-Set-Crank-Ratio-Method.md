# Rebar Bar Type Set Crank Ratio Method

Source: https://www.revitapidocs.com/2026/2592660f-fb98-11d6-7e57-66e17131c4a4.htm

---

| Rebar Bar Type Set Crank Ratio Method |
| --- |

Sets the crank ratio for the specified Rebar Crank Type. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetCrankRatio(
	ElementId rebarCrankTypeId,
	double crankRatio
)
```

```
Public Sub SetCrankRatio ( 
	rebarCrankTypeId As ElementId,
	crankRatio As Double
)
```

```
public:
void SetCrankRatio(
	ElementId^ rebarCrankTypeId, 
	double crankRatio
)
```

```
member SetCrankRatio : 
        rebarCrankTypeId : ElementId * 
        crankRatio : float -> unit 
```

#### Parameters

rebarCrankTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Crank Type id.
 Interactions with Rebar Crank Types can be done with the functions in \[!:Autodesk::Revit::DB::Structure::RebarCrankTypeUtils] .

crankRatio Double
:   The new value of the crank ratio.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarCrankTypeId doesn't represent a valid Rebar Crank Type. It should be an ElementType of BuiltInCategory.OST\_RebarCrankType category.  \-or\-  For the specified Rebar Crank Type is auto calculated and the cannot be manually set.  \-or\-  The crank parameters cannot be computed for the specified crankRatio and Rebar Crank Type. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for crankRatio must be positive. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The crank slope is 1/crankRatio.
 When the crank ratio is set, the crank offset length is keeping the same value. The angled length and straight length are adjusted. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBarType Class](Rebar-Bar-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
