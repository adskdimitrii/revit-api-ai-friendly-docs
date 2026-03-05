# View Position Create Method

Source: https://www.revitapidocs.com/2026/2fa7e4cb-8f6f-bbf0-13cc-253669aae2a2.htm

---

| View Position Create Method |
| --- |

Creates a new view position element. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static ViewPosition Create(
	Document document,
	string name,
	XYZ position,
	ViewAnchor viewAnchor
)
```

```
Public Shared Function Create ( 
	document As Document,
	name As String,
	position As XYZ,
	viewAnchor As ViewAnchor
) As ViewPosition
```

```
public:
static ViewPosition^ Create(
	Document^ document, 
	String^ name, 
	XYZ^ position, 
	ViewAnchor viewAnchor
)
```

```
static member Create : 
        document : Document * 
        name : string * 
        position : XYZ * 
        viewAnchor : ViewAnchor -> ViewPosition 
```

#### Parameters

document [Document](Document-Class.md)
:   The document to which the ViewPosition will be added.

name String
:   The name of the view position element.

position [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The position of the view.

viewAnchor [ViewAnchor](View-Anchor-Enumeration.md)
:   The method the view will be positioned on the sheet.

#### Return Value

[ViewPosition](View-Position-Class.md) 
The newly created view position element. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document.  \-or\-  name is an empty string or contains only whitespace.  \-or\-  name cannot include prohibited characters, such as "{, }, \[, ], \|, ;, less\-than sign, greater\-than sign, ?, \`, \~".  \-or\-  The given value for name is already in use as a view position name. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ViewPosition Class](View-Position-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
