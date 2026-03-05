# Rebar Shape Get Default Hook Orientation Method

Source: https://www.revitapidocs.com/2026/2a97de53-42d6-cf64-f998-73ad9b79fcf0.htm

---

| Rebar Shape Get Default Hook Orientation Method |
| --- |

**Note: This API is now obsolete.** 

Gets the termination's orientation. The orientation it's the same for both hook and crank. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().TerminationOrientationAtStart or RebarShape.GetTerminationsData().TerminationOrientationAtEnd instead.")]
public RebarHookOrientation GetDefaultHookOrientation(
	int end
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().TerminationOrientationAtStart or RebarShape.GetTerminationsData().TerminationOrientationAtEnd instead.")>
Public Function GetDefaultHookOrientation ( 
	end As Integer
) As RebarHookOrientation
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().TerminationOrientationAtStart or RebarShape.GetTerminationsData().TerminationOrientationAtEnd instead.")]
RebarHookOrientation GetDefaultHookOrientation(
	int end
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please use RebarShape.GetTerminationsData().TerminationOrientationAtStart or RebarShape.GetTerminationsData().TerminationOrientationAtEnd instead.")>]
member GetDefaultHookOrientation : 
        end : int -> RebarHookOrientation 
```

#### Parameters

end Int32
:   0 for the termination at start, 1 for the termination at end.

#### Return Value

[RebarHookOrientation](Rebar-Hook-Orientation-Enumeration.md) 
Returns the termination's orientation. The orientation it's the same for both hook and crank. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShape Class](Rebar-Shape-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
