# Conductor Size Create Method

Source: https://www.revitapidocs.com/2026/563d9315-533d-5266-e556-14dbf0163b29.htm

---

| Conductor Size Create Method |
| --- |

Creates a Conductor Size. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static ConductorSize Create(
	Document document
)
```

```
Public Shared Function Create ( 
	document As Document
) As ConductorSize
```

```
public:
static ConductorSize^ Create(
	Document^ document
)
```

```
static member Create : 
        document : Document -> ConductorSize 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

#### Return Value

[ConductorSize](Conductor-Size-Class.md) 
The newly created Conductor Size data. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements).  \-or\-  The document is being loaded, or is in the midst of another  sensitive process. |
| [ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ConductorSize Class](Conductor-Size-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
