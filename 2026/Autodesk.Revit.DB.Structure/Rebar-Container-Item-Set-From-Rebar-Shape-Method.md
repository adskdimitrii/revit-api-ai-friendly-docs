# Rebar Container Item Set From Rebar Shape Method

Source: https://www.revitapidocs.com/2026/2fef9f31-7da8-ffa8-c01d-a16e553e2167.htm

---

| Rebar Container Item Set From Rebar Shape Method |
| --- |

Set an instance of a RebarContainerItem element, as an instance of a RebarShape.
 The instance will have the default shape parameters from the RebarShape,
 and its location is based on the bounding box of the shape in the shape definition.
 Hooks are removed from the shape before computing its bounding box.
 If appropriate hooks can be found in the document, they will be assigned arbitrarily. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetFromRebarShape(
	RebarShape rebarShape,
	RebarBarType barType,
	XYZ origin,
	XYZ xVec,
	XYZ yVec
)
```

```
Public Sub SetFromRebarShape ( 
	rebarShape As RebarShape,
	barType As RebarBarType,
	origin As XYZ,
	xVec As XYZ,
	yVec As XYZ
)
```

```
public:
void SetFromRebarShape(
	RebarShape^ rebarShape, 
	RebarBarType^ barType, 
	XYZ^ origin, 
	XYZ^ xVec, 
	XYZ^ yVec
)
```

```
member SetFromRebarShape : 
        rebarShape : RebarShape * 
        barType : RebarBarType * 
        origin : XYZ * 
        xVec : XYZ * 
        yVec : XYZ -> unit 
```

#### Parameters

rebarShape [RebarShape](Rebar-Shape-Class.md)
:   A RebarShape element that defines the shape of the rebar.

barType [RebarBarType](Rebar-Bar-Type-Class.md)
:   A RebarBarType element that defines bar diameter, bend radius and material of the rebar.

origin [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The lower\-left corner of the shape's bounding box will be placed at this point in the project.

xVec [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The x\-axis in the shape definition will be mapped to this direction in the project.

yVec [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The y\-axis in the shape definition will be mapped to this direction in the project.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | A RebarContainerItem cannot be created from a Rebar Shape that has End Treatments or Cranks or terminations' rotation angles are different than 0\. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | xVec has zero length.  \-or\-  yVec has zero length. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainerItem Class](Rebar-Container-Item-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
