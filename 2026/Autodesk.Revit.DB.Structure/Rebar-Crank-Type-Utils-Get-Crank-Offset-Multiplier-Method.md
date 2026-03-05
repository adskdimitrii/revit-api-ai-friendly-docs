# Rebar Crank Type Utils Get Crank Offset Multiplier Method

Source: https://www.revitapidocs.com/2026/885a70c2-318d-7561-69e0-0e5b6dbdabc5.htm

---

| Rebar Crank Type Utils Get Crank Offset Multiplier Method |
| --- |

Gets the crank offset multiplier value. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static double GetCrankOffsetMultiplier(
	Document document,
	ElementId rebarCrankTypeId
)
```

```
Public Shared Function GetCrankOffsetMultiplier ( 
	document As Document,
	rebarCrankTypeId As ElementId
) As Double
```

```
public:
static double GetCrankOffsetMultiplier(
	Document^ document, 
	ElementId^ rebarCrankTypeId
)
```

```
static member GetCrankOffsetMultiplier : 
        document : Document * 
        rebarCrankTypeId : ElementId -> float 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

rebarCrankTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Crank Type id.

#### Return Value

Double 
Returns the crank offset multiplier value. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarCrankTypeId doesn't represent a valid Rebar Crank Type. It should be an ElementType of BuiltInCategory.OST\_RebarCrankType category. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarCrankTypeUtils Class](Rebar-Crank-Type-Utils-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
