# Rebar Bar Type Get Auto Calculated Crank Method

Source: https://www.revitapidocs.com/2026/09db753d-75dd-ef32-9e78-5b691b50cf50.htm

---

| Rebar Bar Type Get Auto Calculated Crank Method |
| --- |

Identifies if the crank dimensions are auto calculated for the specified Rebar Crank Type. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool GetAutoCalculatedCrank(
	ElementId rebarCrankTypeId
)
```

```
Public Function GetAutoCalculatedCrank ( 
	rebarCrankTypeId As ElementId
) As Boolean
```

```
public:
bool GetAutoCalculatedCrank(
	ElementId^ rebarCrankTypeId
)
```

```
member GetAutoCalculatedCrank : 
        rebarCrankTypeId : ElementId -> bool 
```

#### Parameters

rebarCrankTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Crank Type id.
 Interactions with Rebar Crank Types can be done with the functions in \[!:Autodesk::Revit::DB::Structure::RebarCrankTypeUtils] .

#### Return Value

Boolean 
Returns true if the crank dimensions are auto calculated for the specified Rebar Bar Type and Rebar Crank Type, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarCrankTypeId doesn't represent a valid Rebar Crank Type. It should be an ElementType of BuiltInCategory.OST\_RebarCrankType category. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBarType Class](Rebar-Bar-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
