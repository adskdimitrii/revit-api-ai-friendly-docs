# Label Utils Get Structural Section Shape Name Method

Source: https://www.revitapidocs.com/2026/4969a1cc-9943-c418-dfca-9672b0fba75f.htm

---

| Label Utils Get Structural Section Shape Name Method |
| --- |

Gets the user\-visible name for a StructuralSectionShape. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static string GetStructuralSectionShapeName(
	StructuralSectionShape shape
)
```

```
Public Shared Function GetStructuralSectionShapeName ( 
	shape As StructuralSectionShape
) As String
```

```
public:
static String^ GetStructuralSectionShapeName(
	StructuralSectionShape shape
)
```

```
static member GetStructuralSectionShapeName : 
        shape : StructuralSectionShape -> string 
```

#### Parameters

shape [StructuralSectionShape](daaa1d33-7ee8-738a-5ab7-b93f056deaf8.htm)
:   The StructuralSectionShape to get the user\-visible name.

#### Return Value

String 
Returns the user\-visible name for the StructuralSectionShape. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The name is obtained in the current Revit language. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[LabelUtils Class](Label-Utils-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
