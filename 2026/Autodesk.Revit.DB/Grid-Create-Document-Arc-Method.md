# Grid Create(Document, Arc) Method

Source: https://www.revitapidocs.com/2026/2f1e2722-d302-eb69-818a-44e0e169140c.htm

---

| Grid Create(Document, Arc) Method |
| --- |

Creates a new radial grid line. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static Grid Create(
	Document document,
	Arc arc
)
```

```
Public Shared Function Create ( 
	document As Document,
	arc As Arc
) As Grid
```

```
public:
static Grid^ Create(
	Document^ document, 
	Arc^ arc
)
```

```
static member Create : 
        document : Document * 
        arc : Arc -> Grid 
```

#### Parameters

document [Document](Document-Class.md)
:   The document in which the new instance is created.

arc [Arc](Arc-Class.md)
:   An arc object that represents the location of the new grid curve.

#### Return Value

[Grid](47888507-2d69-664a-ead4-e481c7c5f42d.htm) 
The newly created grid. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document.  \-or\-  The input arc is not on a horizontal plane. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The arc should be on a horizontal plane. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Grid Class](47888507-2d69-664a-ead4-e481c7c5f42d.htm) [Create Overload](00ae8045-b65e-40b1-c162-ef5048fcf9f9.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
