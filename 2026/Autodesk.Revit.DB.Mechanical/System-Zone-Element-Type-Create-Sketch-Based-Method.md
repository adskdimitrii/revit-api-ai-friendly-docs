# System Zone Element Type Create Sketch Based Method

Source: https://www.revitapidocs.com/2026/f08251f7-468d-ec59-233b-50c4e0d22676.htm

---

| System Zone Element Type Create Sketch Based Method |
| --- |

Creates a new element type for sketch\-based system\-zone elements and adds it to the document. 
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static SystemZoneElementType CreateSketchBased(
	Document doc,
	string name
)
```

```
Public Shared Function CreateSketchBased ( 
	doc As Document,
	name As String
) As SystemZoneElementType
```

```
public:
static SystemZoneElementType^ CreateSketchBased(
	Document^ doc, 
	String^ name
)
```

```
static member CreateSketchBased : 
        doc : Document * 
        name : string -> SystemZoneElementType 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document where the new type is created.

name String
:   The name of new type.

#### Return Value

[SystemZoneElementType](System-Zone-Element-Type-Class.md) 
The newly created system\-zone element type. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name cannot include prohibited characters, such as "{, }, \[, ], \|, ;, less\-than sign, greater\-than sign, ?, \`, \~".  \-or\-  name is an empty string.  \-or\-  This name is already used by an existing system\-zone element type in the document. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements). |
| [ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements).  \-or\-  The document is being loaded, or is in the midst of another  sensitive process. |
| [ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[SystemZoneElementType Class](System-Zone-Element-Type-Class.md) [Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
