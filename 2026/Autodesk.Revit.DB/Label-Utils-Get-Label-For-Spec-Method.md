# Label Utils Get Label For Spec Method

Source: https://www.revitapidocs.com/2026/5f0e82b9-cf62-062d-5136-3c4032cca766.htm

---

| Label Utils Get Label For Spec Method |
| --- |

Gets the user\-visible name for a spec. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static string GetLabelForSpec(
	ForgeTypeId specTypeId
)
```

```
Public Shared Function GetLabelForSpec ( 
	specTypeId As ForgeTypeId
) As String
```

```
public:
static String^ GetLabelForSpec(
	ForgeTypeId^ specTypeId
)
```

```
static member GetLabelForSpec : 
        specTypeId : ForgeTypeId -> string 
```

#### Parameters

specTypeId [ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)
:   Identifier of the spec to get the user\-visible name.

#### Return Value

String 
Returns the user\-visible name for a spec. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given identifier is neither a spec nor a category. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The name is obtained in the current Revit language.
 If the given identifier is a category, this method returns the name
 of the Family Type spec with that category, e.g. "Family Type: Walls". ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[LabelUtils Class](Label-Utils-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
