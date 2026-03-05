# Toposolid Remove Excavation By Method

Source: https://www.revitapidocs.com/2026/2366a1f0-2898-e99a-c1f1-2f0e4454477f.htm

---

| Toposolid Remove Excavation By Method |
| --- |

Removes the excavation between the given element and the Toposolid. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void RemoveExcavationBy(
	ElementId elementId
)
```

```
Public Sub RemoveExcavationBy ( 
	elementId As ElementId
)
```

```
public:
void RemoveExcavationBy(
	ElementId^ elementId
)
```

```
member RemoveExcavationBy : 
        elementId : ElementId -> unit 
```

#### Parameters

elementId [ElementId](Element-Id-Class.md)
:   Id of the element that already excavates the Toposolid.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The element is not supported for Toposolid excavation operations. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Toposolid Class](Toposolid-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
