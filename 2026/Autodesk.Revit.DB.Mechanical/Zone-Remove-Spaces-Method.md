# Zone Remove Spaces Method

Source: https://www.revitapidocs.com/2026/2d015441-724c-d576-fcd6-5a00d9b94d44.htm

---

| Zone Remove Spaces Method |
| --- |

**Note: This API is now obsolete.** 

Remove a set of existing spaces to the current Zone element. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")]
public bool RemoveSpaces(
	SpaceSet spaces
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")>
Public Function RemoveSpaces ( 
	spaces As SpaceSet
) As Boolean
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")]
bool RemoveSpaces(
	SpaceSet^ spaces
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use the GenericZone object instead.")>]
member RemoveSpaces : 
        spaces : SpaceSet -> bool 
```

#### Parameters

spaces [SpaceSet](ff608354-dee5-99f7-fca3-d8b20ff5733d.htm)
:   The spaces which want to delete from the current zone element.

#### Return Value

Boolean 
If successful the current zone element will remove a set of input spaces, otherwise . ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the specified parameter Value is . |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the input spaces cannot be deleted from current zone element. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Zone Class](Zone-Class.md) [Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
