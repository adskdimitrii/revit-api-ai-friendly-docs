# Toposolid Excavate By Method

Source: https://www.revitapidocs.com/2026/00ff5e57-e904-3779-31d2-25f3ea4ea64b.htm

---

| Toposolid Excavate By Method |
| --- |

Excavates the Toposolid by a given element. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void ExcavateBy(
	ElementId elementId
)
```

```
Public Sub ExcavateBy ( 
	elementId As ElementId
)
```

```
public:
void ExcavateBy(
	ElementId^ elementId
)
```

```
member ExcavateBy : 
        elementId : ElementId -> unit 
```

#### Parameters

elementId [ElementId](Element-Id-Class.md)
:   Id of the element used to excavate the Toposolid.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The element is not supported for Toposolid excavation operations. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Toposolid Class](Toposolid-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
