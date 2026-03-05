# Rebar Set Hook Type Id Method

Source: https://www.revitapidocs.com/2026/31ce9472-9bf7-3567-eaad-b8b45d587438.htm

---

| Rebar Set Hook Type Id Method |
| --- |

Set the id of the RebarHookType to be applied to the rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetHookTypeId(
	int end,
	ElementId hookTypeId
)
```

```
Public Sub SetHookTypeId ( 
	end As Integer,
	hookTypeId As ElementId
)
```

```
public:
void SetHookTypeId(
	int end, 
	ElementId^ hookTypeId
)
```

```
member SetHookTypeId : 
        end : int * 
        hookTypeId : ElementId -> unit 
```

#### Parameters

end Int32
:   0 for the start hook, 1 for the end hook.

hookTypeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The id of a RebarHookType element, or invalidElementId if
 the rebar should have no hook at the specified end.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | the rebar hook type id hookTypeId is not valid |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
