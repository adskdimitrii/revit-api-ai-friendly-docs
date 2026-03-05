# Rebar Get Crank Type Id Method

Source: https://www.revitapidocs.com/2026/8c6fcfcd-064e-8202-396b-01883443cc4a.htm

---

| Rebar Get Crank Type Id Method |
| --- |

Gets the id of the Crank Type id that is applied to the rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId GetCrankTypeId(
	int end
)
```

```
Public Function GetCrankTypeId ( 
	end As Integer
) As ElementId
```

```
public:
ElementId^ GetCrankTypeId(
	int end
)
```

```
member GetCrankTypeId : 
        end : int -> ElementId 
```

#### Parameters

end Int32
:   0 for the start Crank, 1 for the end Crank.

#### Return Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
Returns the id of a Crank Type, or invalidElementId if the rebar has no crank at the specified end. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Interactions with Rebar Crank Types can be done with the functions in \[!:Autodesk::Revit::DB::Structure::RebarCrankTypeUtils] . ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
