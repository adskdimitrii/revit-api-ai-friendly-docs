# Rebar Crank Type Utils Get All Rebar Crank Types Method

Source: https://www.revitapidocs.com/2026/b57660d4-da60-f69e-bd26-3909dae0c6c1.htm

---

| Rebar Crank Type Utils Get All Rebar Crank Types Method |
| --- |

Gets all the Rebar Crank Types elements from the document. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static IList<ElementId> GetAllRebarCrankTypes(
	Document document
)
```

```
Public Shared Function GetAllRebarCrankTypes ( 
	document As Document
) As IList(Of ElementId)
```

```
public:
static IList<ElementId^>^ GetAllRebarCrankTypes(
	Document^ document
)
```

```
static member GetAllRebarCrankTypes : 
        document : Document -> IList<ElementId> 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

#### Return Value

IList [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
Returns all the Rebar Crank Types elements from the document. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Internally this function is returning all element ids from a FilteredElementCollector of category BuiltInCategory.OST\_RebarCrankType. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarCrankTypeUtils Class](Rebar-Crank-Type-Utils-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
