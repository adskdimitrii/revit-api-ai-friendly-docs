# Rebar Crank Type Utils Set Crank Offset Multiplier Method

Source: https://www.revitapidocs.com/2026/30b20a3e-e8ac-8afa-c82a-25580d4c0810.htm

---

| Rebar Crank Type Utils Set Crank Offset Multiplier Method |
| --- |

Sets the crank offset multiplier value. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static void SetCrankOffsetMultiplier(
	Document document,
	ElementId rebarCrankTypeId,
	double crankOffsetMultiplier
)
```

```
Public Shared Sub SetCrankOffsetMultiplier ( 
	document As Document,
	rebarCrankTypeId As ElementId,
	crankOffsetMultiplier As Double
)
```

```
public:
static void SetCrankOffsetMultiplier(
	Document^ document, 
	ElementId^ rebarCrankTypeId, 
	double crankOffsetMultiplier
)
```

```
static member SetCrankOffsetMultiplier : 
        document : Document * 
        rebarCrankTypeId : ElementId * 
        crankOffsetMultiplier : float -> unit 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

rebarCrankTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Crank Type id.

crankOffsetMultiplier Double
:   The crank offset multiplier value.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarCrankTypeId doesn't represent a valid Rebar Crank Type. It should be an ElementType of BuiltInCategory.OST\_RebarCrankType category. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for crankOffsetMultiplier must be positive. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarCrankTypeUtils Class](Rebar-Crank-Type-Utils-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
