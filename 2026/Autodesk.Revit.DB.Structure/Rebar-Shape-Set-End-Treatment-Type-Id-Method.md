# Rebar Shape Set End Treatment Type Id Method

Source: https://www.revitapidocs.com/2026/f7c875ee-c66f-e08b-78e2-ad40b0d83ea4.htm

---

| Rebar Shape Set End Treatment Type Id Method |
| --- |

**Note: This API is now obsolete.** 

Sets the EndTreatmentType id at the specified rebar shape end. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please create a new shape using RebarShape.Create(Document doc, RebarShapeDefinition definition, RebarShapeMultiplanarDefinition multiplanarDefinition, RebarStyle style, StirrupTieAttachmentType attachmentType, int higherEnd, RebarShapeTerminationsData rebarShapeTerminationsData) instead.")]
public void SetEndTreatmentTypeId(
	ElementId endTreatmentId,
	int end
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please create a new shape using RebarShape.Create(Document doc, RebarShapeDefinition definition, RebarShapeMultiplanarDefinition multiplanarDefinition, RebarStyle style, StirrupTieAttachmentType attachmentType, int higherEnd, RebarShapeTerminationsData rebarShapeTerminationsData) instead.")>
Public Sub SetEndTreatmentTypeId ( 
	endTreatmentId As ElementId,
	end As Integer
)
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please create a new shape using RebarShape.Create(Document doc, RebarShapeDefinition definition, RebarShapeMultiplanarDefinition multiplanarDefinition, RebarStyle style, StirrupTieAttachmentType attachmentType, int higherEnd, RebarShapeTerminationsData rebarShapeTerminationsData) instead.")]
void SetEndTreatmentTypeId(
	ElementId^ endTreatmentId, 
	int end
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please create a new shape using RebarShape.Create(Document doc, RebarShapeDefinition definition, RebarShapeMultiplanarDefinition multiplanarDefinition, RebarStyle style, StirrupTieAttachmentType attachmentType, int higherEnd, RebarShapeTerminationsData rebarShapeTerminationsData) instead.")>]
member SetEndTreatmentTypeId : 
        endTreatmentId : ElementId * 
        end : int -> unit 
```

#### Parameters

endTreatmentId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The id of an EndTreatmentType element, or invalidElementId if the rebar shape should have no end treatment at the specified end.

end Int32
:   0 for the start end treatment, 1 for the end end treatment.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | end not a valid shape end  \-or\-  the parameter endTreatmentId is not an EndTreatmentType element. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShape Class](Rebar-Shape-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
