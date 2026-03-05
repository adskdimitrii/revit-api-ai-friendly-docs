# Rebar Free Form Accessor Set Reported Shape Method

Source: https://www.revitapidocs.com/2026/3f015caf-7844-ab56-c962-9020b141e0d2.htm

---

| Rebar Free Form Accessor Set Reported Shape Method |
| --- |

This method changes the RebarShape of a Free Form Rebar that is using RebarWorkInstructions.Straight property to the provided RebarShape. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetReportedShape(
	ElementId rebarShapeId
)
```

```
Public Sub SetReportedShape ( 
	rebarShapeId As ElementId
)
```

```
public:
void SetReportedShape(
	ElementId^ rebarShapeId
)
```

```
member SetReportedShape : 
        rebarShapeId : ElementId -> unit 
```

#### Parameters

rebarShapeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | rebarShapeId cannot be set as a reporting RebarShape for this Rebar element. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The Rebar element RebarWorkInstructions property should be Straight.
 The rebarShapeId parameter should be the id of a straight RebarShape (single straight segment, no RebarHookType, no EndTreatmentType, no Crank).
 Moreover the straight RebarShape RebarStyle should match ( if the current RebarShape RebarStyle is Standard then the RebarShape cannot be changed to a straigh RebarShape using the RebarStyle Stirrup/Tie ).
 If current RebarShape and the provided rebarShapeId has Stirrup/Tie RebarStyle then also the StirrupTieAttachmentType should match ( both InteriorFace or ExteriorFace ). ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarFreeFormAccessor Class](Rebar-Free-Form-Accessor-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
