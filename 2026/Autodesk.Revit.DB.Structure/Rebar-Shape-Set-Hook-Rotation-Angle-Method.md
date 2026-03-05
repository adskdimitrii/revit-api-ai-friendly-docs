# Rebar Shape Set Hook Rotation Angle Method

Source: https://www.revitapidocs.com/2026/b30a6f55-b672-e942-7c1f-ab3d9b27dd4e.htm

---

| Rebar Shape Set Hook Rotation Angle Method |
| --- |

**Note: This API is now obsolete.** 

Sets the termination's (e.g hook, crank) out of plane rotation angle at the specified end.
 The angle will be used for both hook and crank. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please create a new shape using RebarShape.Create(Document doc, RebarShapeDefinition definition, RebarShapeMultiplanarDefinition multiplanarDefinition, RebarStyle style, StirrupTieAttachmentType attachmentType, int higherEnd, RebarShapeTerminationsData rebarShapeTerminationsData) instead.")]
public void SetHookRotationAngle(
	double rotationAngle,
	int end
)
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please create a new shape using RebarShape.Create(Document doc, RebarShapeDefinition definition, RebarShapeMultiplanarDefinition multiplanarDefinition, RebarStyle style, StirrupTieAttachmentType attachmentType, int higherEnd, RebarShapeTerminationsData rebarShapeTerminationsData) instead.")>
Public Sub SetHookRotationAngle ( 
	rotationAngle As Double,
	end As Integer
)
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please create a new shape using RebarShape.Create(Document doc, RebarShapeDefinition definition, RebarShapeMultiplanarDefinition multiplanarDefinition, RebarStyle style, StirrupTieAttachmentType attachmentType, int higherEnd, RebarShapeTerminationsData rebarShapeTerminationsData) instead.")]
void SetHookRotationAngle(
	double rotationAngle, 
	int end
)
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Please create a new shape using RebarShape.Create(Document doc, RebarShapeDefinition definition, RebarShapeMultiplanarDefinition multiplanarDefinition, RebarStyle style, StirrupTieAttachmentType attachmentType, int higherEnd, RebarShapeTerminationsData rebarShapeTerminationsData) instead.")>]
member SetHookRotationAngle : 
        rotationAngle : float * 
        end : int -> unit 
```

#### Parameters

rotationAngle Double
:   The out of plane rotation angle at the specified end.
 The angle will be used for both hook and crank.

end Int32
:   0 for the start, 1 for the end.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for rotationAngle is not finite |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1\. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShape Class](Rebar-Shape-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
