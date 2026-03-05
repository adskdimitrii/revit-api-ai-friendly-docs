# Zone Add Spaces Method

Source: https://www.revitapidocs.com/2026/455eec6f-75c4-1f73-ef11-326975163398.htm

---

| Zone Add Spaces Method |
| --- |

**Note: This API is now obsolete.** 

Add a set of existing spaces to Zone element. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")]
public bool AddSpaces(
	SpaceSet spaces
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")>
Public Function AddSpaces ( 
	spaces As SpaceSet
) As Boolean
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")]
bool AddSpaces(
	SpaceSet^ spaces
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")>]
member AddSpaces : 
        spaces : SpaceSet -> bool 
```

#### Parameters

spaces [SpaceSet](ff608354-dee5-99f7-fca3-d8b20ff5733d.htm)
:   The spaces which want to add to zone element.

#### Return Value

Boolean 
If successful the current zone element will add a set of input spaces, otherwise . ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the specified parameter Value is . |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the input spaces cannot be added to current zone element. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Zone Class](Zone-Class.md) [Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
