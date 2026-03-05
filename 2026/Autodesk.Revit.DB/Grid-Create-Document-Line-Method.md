# Grid Create(Document, Line) Method

Source: https://www.revitapidocs.com/2026/462cb588-9811-e464-0fe9-13226a2fc8f7.htm

---

| Grid Create(Document, Line) Method |
| --- |

Creates a new grid line. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static Grid Create(
	Document document,
	Line line
)
```

```
Public Shared Function Create ( 
	document As Document,
	line As Line
) As Grid
```

```
public:
static Grid^ Create(
	Document^ document, 
	Line^ line
)
```

```
static member Create : 
        document : Document * 
        line : Line -> Grid 
```

#### Parameters

document [Document](Document-Class.md)
:   The document in which the new instance is created.

line [Line](Line-Class.md)
:   A line which represents the location of the grid line.

#### Return Value

[Grid](47888507-2d69-664a-ead4-e481c7c5f42d.htm) 
The newly created grid. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document.  \-or\-  The input line is not on a horizontal plane. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The line should be on a horizontal plane. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Grid Class](47888507-2d69-664a-ead4-e481c7c5f42d.htm) [Create Overload](00ae8045-b65e-40b1-c162-ef5048fcf9f9.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
