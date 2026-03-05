# Rebar Container Append Item From Rebar Shape Method

Source: https://www.revitapidocs.com/2026/292aade1-0459-1a6a-9bd3-715e8bb634df.htm

---

| Rebar Container Append Item From Rebar Shape Method |
| --- |

Appends an Item to the RebarContainer. Fills its data on base of the Rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public RebarContainerItem AppendItemFromRebarShape(
	RebarShape rebarShape,
	RebarBarType barType,
	XYZ origin,
	XYZ xVector,
	XYZ yVector
)
```

```
Public Function AppendItemFromRebarShape ( 
	rebarShape As RebarShape,
	barType As RebarBarType,
	origin As XYZ,
	xVector As XYZ,
	yVector As XYZ
) As RebarContainerItem
```

```
public:
RebarContainerItem^ AppendItemFromRebarShape(
	RebarShape^ rebarShape, 
	RebarBarType^ barType, 
	XYZ^ origin, 
	XYZ^ xVector, 
	XYZ^ yVector
)
```

```
member AppendItemFromRebarShape : 
        rebarShape : RebarShape * 
        barType : RebarBarType * 
        origin : XYZ * 
        xVector : XYZ * 
        yVector : XYZ -> RebarContainerItem 
```

#### Parameters

rebarShape [RebarShape](Rebar-Shape-Class.md)
:   A RebarShape element that defines the shape of the rebar.

barType [RebarBarType](Rebar-Bar-Type-Class.md)
:   A RebarBarType element that defines bar diameter, bend radius and material of the rebar.

origin [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The lower\-left corner of the shape's bounding box will be placed at this point in the project.

xVector [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The x\-axis in the shape definition will be mapped to this direction in the project.

yVector [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)
:   The y\-axis in the shape definition will be mapped to this direction in the project.

#### Return Value

[RebarContainerItem](Rebar-Container-Item-Class.md) 
The Rebar Container Item. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | A RebarContainerItem cannot be created from a Rebar Shape that has End Treatments or Cranks or terminations' rotation angles are different than 0\. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | xVector has zero length.  \-or\-  yVector has zero length. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainer Class](Rebar-Container-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
