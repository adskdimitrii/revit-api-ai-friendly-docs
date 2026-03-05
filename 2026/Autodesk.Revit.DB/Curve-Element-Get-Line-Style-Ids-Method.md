# Curve Element Get Line Style Ids Method

Source: https://www.revitapidocs.com/2026/3e30d0b4-6c74-18bf-043f-2430ff9ac17b.htm

---

| Curve Element Get Line Style Ids Method |
| --- |

Ids of all line style Elements that are applicable to this curve element. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ICollection<ElementId> GetLineStyleIds()
```

```
Public Function GetLineStyleIds As ICollection(Of ElementId)
```

```
public:
ICollection<ElementId^>^ GetLineStyleIds()
```

```
member GetLineStyleIds : unit -> ICollection<ElementId> 
```

#### Return Value

ICollection [ElementId](Element-Id-Class.md) 
A collection of Ids of line style elements. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The elements are of the \[!:Autodesk::Revit::DB::GraphicsStyle] class. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CurveElement Class](61673852-2d08-003d-e9fd-4be89d533774.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
