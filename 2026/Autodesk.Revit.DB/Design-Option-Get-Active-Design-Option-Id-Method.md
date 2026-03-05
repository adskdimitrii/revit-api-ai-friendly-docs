# Design Option Get Active Design Option Id Method

Source: https://www.revitapidocs.com/2026/d0b47e58-a5fc-9424-a94c-2428b4ec4d16.htm

---

| Design Option Get Active Design Option Id Method |
| --- |

Gets the active design option id for the document. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static ElementId GetActiveDesignOptionId(
	Document document
)
```

```
Public Shared Function GetActiveDesignOptionId ( 
	document As Document
) As ElementId
```

```
public:
static ElementId^ GetActiveDesignOptionId(
	Document^ document
)
```

```
static member GetActiveDesignOptionId : 
        document : Document -> ElementId 
```

#### Parameters

document [Document](Document-Class.md)
:   The document.

#### Return Value

[ElementId](Element-Id-Class.md) 
The active design option id. It can be invalid id if there is no active design option in the document. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[DesignOption Class](Design-Option-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
