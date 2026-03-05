# Rebar Bar Type Set Crank Angled Length Method

Source: https://www.revitapidocs.com/2026/55f0f6f3-bf99-c03c-af0e-a6ed5385011a.htm

---

| Rebar Bar Type Set Crank Angled Length Method |
| --- |

Sets the crank angled length for the specified Rebar Crank Type. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetCrankAngledLength(
	ElementId rebarCrankTypeId,
	double crankAngledLength
)
```

```
Public Sub SetCrankAngledLength ( 
	rebarCrankTypeId As ElementId,
	crankAngledLength As Double
)
```

```
public:
void SetCrankAngledLength(
	ElementId^ rebarCrankTypeId, 
	double crankAngledLength
)
```

```
member SetCrankAngledLength : 
        rebarCrankTypeId : ElementId * 
        crankAngledLength : float -> unit 
```

#### Parameters

rebarCrankTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Crank Type id.
 Interactions with Rebar Crank Types can be done with the functions in \[!:Autodesk::Revit::DB::Structure::RebarCrankTypeUtils] .

crankAngledLength Double
:   The new value of the crank angled length.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarCrankTypeId doesn't represent a valid Rebar Crank Type. It should be an ElementType of BuiltInCategory.OST\_RebarCrankType category.  \-or\-  For the specified Rebar Crank Type is auto calculated and the cannot be manually set.  \-or\-  The crank parameters cannot be computed for the specified crankAngledLength and Rebar Crank Type. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for crankAngledLength must be positive. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks When the crank angled length is set, the crank ratio is keeping the same value. The offset length and straight length are adjusted. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBarType Class](Rebar-Bar-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
