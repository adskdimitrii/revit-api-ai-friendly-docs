# Rebar Container Item Rebar Shape Id Property

Source: https://www.revitapidocs.com/2026/4e755081-80ba-11c1-f428-ed1f0a1f580b.htm

---

| Rebar Container Item Rebar Shape Id Property |
| --- |

The RebarShape element that defines the shape of the rebar. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId RebarShapeId { get; set; }
```

```
Public Property RebarShapeId As ElementId
	Get
	Set
```

```
public:
property ElementId^ RebarShapeId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```

```
member RebarShapeId : ElementId with get, set
```

#### Property Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: shapeId is not the id of a RebarShape in the document.  \-or\-  When setting this property: A RebarContainerItem cannot be created from a Rebar Shape that has End Treatments or Cranks or terminations' rotation angles are different than 0\. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Changing the value of this property causes the Rebar instance to choose values for its
 shape parameters to preserve its previous shape as closely as possible ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainerItem Class](Rebar-Container-Item-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
