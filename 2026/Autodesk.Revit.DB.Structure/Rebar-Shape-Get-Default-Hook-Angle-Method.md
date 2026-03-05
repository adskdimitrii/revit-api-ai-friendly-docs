# Rebar Shape Get Default Hook Angle Method

Source: https://www.revitapidocs.com/2026/89fe9654-9f1c-6ba8-d87c-1b38b63feb31.htm

---

| Rebar Shape Get Default Hook Angle Method |
| --- |

**Note: This API is now obsolete.** 

Get the hook angle, expressed as an integral number of degrees (common values are 0, 90, 135, and 180\). 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().HookAngleAtStart or RebarShape.GetTerminationsData().HookAngleAtEnd instead.")]
public int GetDefaultHookAngle(
	int end
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().HookAngleAtStart or RebarShape.GetTerminationsData().HookAngleAtEnd instead.")>
Public Function GetDefaultHookAngle ( 
	end As Integer
) As Integer
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().HookAngleAtStart or RebarShape.GetTerminationsData().HookAngleAtEnd instead.")]
int GetDefaultHookAngle(
	int end
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().HookAngleAtStart or RebarShape.GetTerminationsData().HookAngleAtEnd instead.")>]
member GetDefaultHookAngle : 
        end : int -> int 
```

#### Parameters

end Int32
:   0 for the starting hook, 1 for the ending hook.

#### Return Value

Int32 ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Replaces the method GetHookAngle() from prior releases. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShape Class](Rebar-Shape-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
