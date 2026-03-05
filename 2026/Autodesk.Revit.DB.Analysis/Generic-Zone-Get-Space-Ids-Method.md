# Generic Zone Get Space Ids Method

Source: https://www.revitapidocs.com/2026/c499ea28-9404-d818-f29c-63225a1f99e5.htm

---

| Generic Zone Get Space Ids Method |
| --- |

Gets a list of ElementIds of the associated spaces for the zone. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ISet<ElementId> GetSpaceIds()
```

```
Public Function GetSpaceIds As ISet(Of ElementId)
```

```
public:
ISet<ElementId^>^ GetSpaceIds()
```

```
member GetSpaceIds : unit -> ISet<ElementId> 
```

#### Return Value

ISet [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
The associated spaces for the space\-based zone. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This generic zone must be space\-based. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[GenericZone Class](Generic-Zone-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
