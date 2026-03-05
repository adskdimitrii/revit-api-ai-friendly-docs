# Rebar Bar Type Set Auto Calculated Crank Method

Source: https://www.revitapidocs.com/2026/442b027e-7264-159e-e2ec-75f6b890db32.htm

---

| Rebar Bar Type Set Auto Calculated Crank Method |
| --- |

Sets if the crank dimensions are auto calculated or not for the specified Rebar Crank Type. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetAutoCalculatedCrank(
	ElementId rebarCrankTypeId,
	bool autoCalculated
)
```

```
Public Sub SetAutoCalculatedCrank ( 
	rebarCrankTypeId As ElementId,
	autoCalculated As Boolean
)
```

```
public:
void SetAutoCalculatedCrank(
	ElementId^ rebarCrankTypeId, 
	bool autoCalculated
)
```

```
member SetAutoCalculatedCrank : 
        rebarCrankTypeId : ElementId * 
        autoCalculated : bool -> unit 
```

#### Parameters

rebarCrankTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Rebar Crank Type id.
 Interactions with Rebar Crank Types can be done with the functions in \[!:Autodesk::Revit::DB::Structure::RebarCrankTypeUtils] .

autoCalculated Boolean
:   True, if the crank dimensions are auto calculated, false otherwise.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarCrankTypeId doesn't represent a valid Rebar Crank Type. It should be an ElementType of BuiltInCategory.OST\_RebarCrankType category. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarBarType Class](Rebar-Bar-Type-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
