# Folder Item Info Get Grouping Parameter Id Path Method

Source: https://www.revitapidocs.com/2026/4947b568-de07-2200-153e-4ad2139308af.htm

---

| Folder Item Info Get Grouping Parameter Id Path Method |
| --- |

The parameter Id path used to determine the folder items in the browser. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<ElementId> GetGroupingParameterIdPath()
```

```
Public Function GetGroupingParameterIdPath As IList(Of ElementId)
```

```
public:
IList<ElementId^>^ GetGroupingParameterIdPath()
```

```
member GetGroupingParameterIdPath : unit -> IList<ElementId> 
```

#### Return Value

IList [ElementId](Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A parameter Id path consists of reference parameter Id(s) {0\...n} \+ paramId,
 and the value of the last parameter in the path is the one that is used to determine the folder items in the browser.
 Reference parameter is ElementId valued parameter used to retrieve related element, its parameter value is the related element Id.
 Given an Element, get the value of reference parameter and use the ElementId value to retrieve the referenced element.
 Each paramId in the path except for the last one is a reference parameter pointing to the next element.
 Recursively get next element through element obtained in the previous round with the next paramId in the path,
 finally get the value of the last parameter. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[FolderItemInfo Class](Folder-Item-Info-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
