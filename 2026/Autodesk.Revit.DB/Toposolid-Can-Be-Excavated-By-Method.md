# Toposolid Can Be Excavated By Method

Source: https://www.revitapidocs.com/2026/ed8909b2-a302-158b-0eae-05de0c05a40c.htm

---

| Toposolid Can Be Excavated By Method |
| --- |

Checks if the given element can be used to excavate the Toposolid. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool CanBeExcavatedBy(
	ElementId elementId
)
```

```
Public Function CanBeExcavatedBy ( 
	elementId As ElementId
) As Boolean
```

```
public:
bool CanBeExcavatedBy(
	ElementId^ elementId
)
```

```
member CanBeExcavatedBy : 
        elementId : ElementId -> bool 
```

#### Parameters

elementId [ElementId](Element-Id-Class.md)
:   Id of the element

#### Return Value

Boolean 
True if the element can be used to excavate the Toposolid. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Toposolid Class](Toposolid-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
