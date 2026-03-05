# Rebar Hook Angle Matches Rebar Shape Definition Method

Source: https://www.revitapidocs.com/2026/3a5c4860-23a1-65bc-e825-8277c0720f45.htm

---

| Rebar Hook Angle Matches Rebar Shape Definition Method |
| --- |

Checks that the hook angle of the specified RebarHookType matches the hook angle used in the Rebar's RebarShape at the specified end of the bar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool HookAngleMatchesRebarShapeDefinition(
	int end,
	ElementId proposedHookId
)
```

```
Public Function HookAngleMatchesRebarShapeDefinition ( 
	end As Integer,
	proposedHookId As ElementId
) As Boolean
```

```
public:
bool HookAngleMatchesRebarShapeDefinition(
	int end, 
	ElementId^ proposedHookId
)
```

```
member HookAngleMatchesRebarShapeDefinition : 
        end : int * 
        proposedHookId : ElementId -> bool 
```

#### Parameters

end Int32
:   0 for the start hook, 1 for the end hook.

proposedHookId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Id of the RebarHookType

#### Return Value

Boolean 
Returns true if the hook angle of the RebarHookType matches the angle used in the RebarShape at the specified end of the bar. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Also checks that the specified id is a valid RebarHookType.
 If RebarShapeDefinesHooks property of ReinforcementSettings is false (European shapes), every valid hook angle matches RebarShape definition.
 If RebarShapeDefinesHooks property of ReinforcementSettings is true (non\-European shapes), hook angle matches RebarShape definition if it is null or equal RebarShape default hook angle. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
