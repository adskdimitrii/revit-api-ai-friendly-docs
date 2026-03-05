# Curve Element Set Tangent Lock Method

Source: https://www.revitapidocs.com/2026/34e01fde-176d-c53b-1a9e-bda92dbdf142.htm

---

| Curve Element Set Tangent Lock Method |
| --- |

Sets a new status for an existing tangent join with another curve element at the given end\-point. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetTangentLock(
	int end,
	ElementId other,
	bool state
)
```

```
Public Sub SetTangentLock ( 
	end As Integer,
	other As ElementId,
	state As Boolean
)
```

```
public:
void SetTangentLock(
	int end, 
	ElementId^ other, 
	bool state
)
```

```
member SetTangentLock : 
        end : int * 
        other : ElementId * 
        state : bool -> unit 
```

#### Parameters

end Int32
:   Index of one of the curve's ends. Values '0' and '1' indicate the start or end point, respectively.

other [ElementId](Element-Id-Class.md)
:   ElementId of another Curve Element from the same document.

state Boolean
:   Requested new state of the lock; True to lock it, False to unlock it.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given Id does not represent any of the two end\-points of a curve element.  A valid value of either '0' or '1' is expected.  \-or\-  The given ElementId (%elementId) is not of a valid Curve Element.  A valid Curve Element must be in the same document and must be  diferent than this curve elements self.  \-or\-  This element has no tangent join with the input element at the given end\-point.  \-or\-  The element other does not exist in the document containing this CurveElement |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This curve element does not support tangent joins with other elements. |
| [ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | This CurveElement is an internal element, such as a component of a  loaded family or a group type.  \-or\-  The document containing this CurveElement is in Group Edit Mode,  Sketch Edit Mode, or Paste Mode, and the element is not a  member of the group, sketch, or clipboard.  \-or\-  This CurveElement is a member of a group or sketch, and the document  is not currently editing the group or sketch.  \-or\-  other is an internal element, such as a component of a  loaded family or a group type.  \-or\-  The document containing other is in Group Edit Mode,  Sketch Edit Mode, or Paste Mode, and the element is not a  member of the group, sketch, or clipboard.  \-or\-  other is a member of a group or sketch, and the document  is not currently editing the group or sketch. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The input status indicates whether the tangent join is to be locked or unlocked.
 Note that the status can be set only if this and the other curve element are currently
 joined and tangent at the given point. 

Locking a tangent join between elements of a family will make the family parametric.
 A parametric family needs to utilize a geometry solver in order to determine final
 shapes of its instances. Using the solver in families which contain large sketches
 may cause regenerations of such families to become significantly slower.
 To determine whether a particular family falls into such a category, programmers
 can query [IsParametric](Family-Is-Parametric-Property.md) property
 and [HasLargeSketches](c49820d6-d8f2-de9a-544d-f896a32e39c8.htm) method of the [Family](f51d019d-6ff3-692b-d1d2-b497cab564de.htm) class. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CurveElement Class](61673852-2d08-003d-e9fd-4be89d533774.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
