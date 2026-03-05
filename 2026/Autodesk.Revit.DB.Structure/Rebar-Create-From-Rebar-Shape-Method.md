# Rebar Create From Rebar Shape Method

Source: https://www.revitapidocs.com/2026/5e58e3f3-dea6-79cb-9de4-475e6fe5c28b.htm

---

| Rebar Create From Rebar Shape Method |
| --- |

Creates a new shape driven Rebar, as an instance of a RebarShape.
 The instance will have the default shape parameters from the RebarShape,
 and its location is based on the bounding box of the shape in the shape definition.
 Hooks and cranks are removed from the shape before computing its bounding box.
 If appropriate hooks and cranks can be found in the document, they will be assigned arbitrarily. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static Rebar CreateFromRebarShape(
	Document doc,
	RebarShape rebarShape,
	RebarBarType barType,
	Element host,
	XYZ origin,
	XYZ xVec,
	XYZ yVec
)
```

```
Public Shared Function CreateFromRebarShape ( 
	doc As Document,
	rebarShape As RebarShape,
	barType As RebarBarType,
	host As Element,
	origin As XYZ,
	xVec As XYZ,
	yVec As XYZ
) As Rebar
```

```
public:
static Rebar^ CreateFromRebarShape(
	Document^ doc, 
	RebarShape^ rebarShape, 
	RebarBarType^ barType, 
	Element^ host, 
	XYZ^ origin, 
	XYZ^ xVec, 
	XYZ^ yVec
)
```

```
static member CreateFromRebarShape : 
        doc : Document * 
        rebarShape : RebarShape * 
        barType : RebarBarType * 
        host : Element * 
        origin : XYZ * 
        xVec : XYZ * 
        yVec : XYZ -> Rebar 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   A document.

rebarShape [RebarShape](Rebar-Shape-Class.md)
:   A RebarShape element that defines the shape of the rebar.

barType [RebarBarType](Rebar-Bar-Type-Class.md)
:   A RebarBarType element that defines bar diameter, bend radius and material of the rebar.

host [Element](../Autodesk.Revit.DB/Element-Class.md)
:   The element to which the rebar belongs. The element must support rebar hosting; \[!:Autodesk::Revit::DB::Structure::RebarHostData] .

origin [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The lower\-left corner of the shape's bounding box will be placed at this point in the project.

xVec [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The x\-axis in the shape definition will be mapped to this direction in the project.

yVec [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The y\-axis in the shape definition will be mapped to this direction in the project.

#### Return Value

[Rebar](Rebar-Class.md) 
The newly created Rebar instance, or if the operation fails. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element host was not found in the given document.  \-or\-  host is not a valid rebar host. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | xVec has zero length.  \-or\-  yVec has zero length. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
