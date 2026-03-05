# End Treatment Type Create(Document, String) Method

Source: https://www.revitapidocs.com/2026/75a20905-c88b-df7e-1adc-d6beb096bec9.htm

---

| End Treatment Type Create(Document, String) Method |
| --- |

Creates a new EndTreatmentType in the specified document and adds the input string to the endTreatment parameter. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static EndTreatmentType Create(
	Document doc,
	string treatment
)
```

```
Public Shared Function Create ( 
	doc As Document,
	treatment As String
) As EndTreatmentType
```

```
public:
static EndTreatmentType^ Create(
	Document^ doc, 
	String^ treatment
)
```

```
static member Create : 
        doc : Document * 
        treatment : string -> EndTreatmentType 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   Returns the newly created EndTreatmentType in the specified document.

treatment String
:   This string will be se to the endTreatment parameter.

#### Return Value

[EndTreatmentType](End-Treatment-Type-Class.md) 
Returns the newly created EndTreatmentType in the specified document. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[EndTreatmentType Class](End-Treatment-Type-Class.md) [Create Overload](End-Treatment-Type-Create-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
