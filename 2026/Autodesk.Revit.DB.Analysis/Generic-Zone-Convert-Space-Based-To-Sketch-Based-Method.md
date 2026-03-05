# Generic Zone Convert Space Based To Sketch Based Method

Source: https://www.revitapidocs.com/2026/2e839684-51d0-cea5-c76b-c461b39bb623.htm

---

| Generic Zone Convert Space Based To Sketch Based Method |
| --- |

Converts a space\-based generic zone to a sketch\-based generic zone. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void ConvertSpaceBasedToSketchBased(
	ElementId typeId
)
```

```
Public Sub ConvertSpaceBasedToSketchBased ( 
	typeId As ElementId
)
```

```
public:
void ConvertSpaceBasedToSketchBased(
	ElementId^ typeId
)
```

```
member ConvertSpaceBasedToSketchBased : 
        typeId : ElementId -> unit 
```

#### Parameters

typeId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The sketch\-based element type for the new generic zone.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element typeId is not a valid sketch\-based zone type. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document containing this GenericZone is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements).  \-or\-  The element is a member of a loaded family.  \-or\-  The element is a member of a group type that is  not being edited.  \-or\-  This generic zone must be space\-based. |
| [ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document containing this GenericZone is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements).  \-or\-  The document containing this GenericZone is being loaded, or is in the midst of another  sensitive process.  \-or\-  This GenericZone is an internal element, such as a component of a  loaded family or a group type.  \-or\-  The document containing this GenericZone is in Group Edit Mode,  Sketch Edit Mode, or Paste Mode, and the element is not a  member of the group, sketch, or clipboard.  \-or\-  This GenericZone is a member of a group or sketch, and the document  is not currently editing the group or sketch. |
| [ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document containing this GenericZone has no open transaction. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This element must be the space\-based before the conversion. The conversation will keep the
 same element id, name, but swapped into a different type as specified. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[GenericZone Class](Generic-Zone-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
