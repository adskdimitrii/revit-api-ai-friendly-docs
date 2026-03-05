# Rebar Shape Create(Document, Rebar Shape Definition, Rebar Shape Multiplanar Definition, Rebar Style, Stirrup Tie Attachment Type, Int 32, Rebar Shape Terminations Data) Method

Source: https://www.revitapidocs.com/2026/6473e5c0-1e3c-c928-7dde-2294bdf873d0.htm

---

| Rebar Shape Create(Document, Rebar Shape Definition, Rebar Shape Multiplanar Definition, Rebar Style, Stirrup Tie Attachment Type, Int 32, Rebar Shape Terminations Data) Method |
| --- |

Create a new instance of a Rebar Shape, which defines the shape of a rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static RebarShape Create(
	Document doc,
	RebarShapeDefinition definition,
	RebarShapeMultiplanarDefinition multiplanarDefinition,
	RebarStyle style,
	StirrupTieAttachmentType attachmentType,
	int higherEnd,
	RebarShapeTerminationsData rebarShapeTerminationsData
)
```

```
Public Shared Function Create ( 
	doc As Document,
	definition As RebarShapeDefinition,
	multiplanarDefinition As RebarShapeMultiplanarDefinition,
	style As RebarStyle,
	attachmentType As StirrupTieAttachmentType,
	higherEnd As Integer,
	rebarShapeTerminationsData As RebarShapeTerminationsData
) As RebarShape
```

```
public:
static RebarShape^ Create(
	Document^ doc, 
	RebarShapeDefinition^ definition, 
	RebarShapeMultiplanarDefinition^ multiplanarDefinition, 
	RebarStyle style, 
	StirrupTieAttachmentType attachmentType, 
	int higherEnd, 
	RebarShapeTerminationsData^ rebarShapeTerminationsData
)
```

```
static member Create : 
        doc : Document * 
        definition : RebarShapeDefinition * 
        multiplanarDefinition : RebarShapeMultiplanarDefinition * 
        style : RebarStyle * 
        attachmentType : StirrupTieAttachmentType * 
        higherEnd : int * 
        rebarShapeTerminationsData : RebarShapeTerminationsData -> RebarShape 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   A document to contain the RebarShape.

definition [RebarShapeDefinition](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)
:   The definition of the rebar shape, as a set of curves in a plane
 driven by parameters.

multiplanarDefinition [RebarShapeMultiplanarDefinition](47a3135c-ce53-c041-f551-0795767eaa41.htm)
:   If not , the created RebarShape will be a 3D shape. The shape
 is built out of the planar RebarShapeDefinition, with additional
 out\-of\-plane segments defined by the RebarShapeMultiplanarDefinition
 object. Not supported in conjunction with RebarShapeDefinitionByArc
 of type Spiral or LappedCircle.

style [RebarStyle](a9ac65a6-29e6-25e5-caca-502e21385f47.htm)
:   Whether the shape is to be used as a standard bar or a stirrup/tie.

attachmentType [StirrupTieAttachmentType](01887c64-36b1-1f7f-5ff9-1fb3ba4f3023.htm)
:   When the style is stirrup/tie, specify whether it will attach to the
 interior of cover (cover is measured to the stirrups), or to the
 exterior of cover (cover is measured to the standard bars).
 Ignored when the style is Standard.

higherEnd Int32
:   When the rebar crosses itself, one end will be "lifted" to avoid self\-intersection.
 Specify which end should be lifted: 0 for start, 1 for end.

rebarShapeTerminationsData [RebarShapeTerminationsData](Rebar-Shape-Terminations-Data-Class.md)
:   Data about Rebar Shape terminations.

#### Return Value

[RebarShape](Rebar-Shape-Class.md) 
A new RebarShape instance. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | definition is linked to a Document other than doc.  \-or\-  A multiplanar definition is specified when the given RebarShapeDefinition  does not support it. The following RebarShapeDefinitions do not support  multiplanar: a simple line; spiral; lapped circle.  \-or\-  The DepthParamId property of multiplanarDefinition  is invalid or has not been added to definition.  \-or\-  The rebarShapeTerminationsData was not created using the input document. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | higherEnd must be 0 or 1\.  \-or\-  A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShape Class](Rebar-Shape-Class.md) [Create Overload](Rebar-Shape-Create-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
