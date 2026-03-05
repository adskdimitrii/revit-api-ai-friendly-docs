# Rebar Get Hook Type Id Method

Source: https://www.revitapidocs.com/2026/016d53d9-0ef5-99d1-b12f-089f04df3952.htm

---

| Rebar Get Hook Type Id Method |
| --- |

Get the id of the RebarHookType that is applied to the rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId GetHookTypeId(
	int end
)
```

```
Public Function GetHookTypeId ( 
	end As Integer
) As ElementId
```

```
public:
ElementId^ GetHookTypeId(
	int end
)
```

```
member GetHookTypeId : 
        end : int -> ElementId 
```

#### Parameters

end Int32
:   0 for the start hook, 1 for the end hook.

#### Return Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
The id of a RebarHookType, or invalidElementId if the rebar has
 no hook at the specified end. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
