# Label Utils Get Label For Symbol Method

Source: https://www.revitapidocs.com/2026/d8dc0d86-c548-89ba-da65-3f3a9b2f9ec8.htm

---

| Label Utils Get Label For Symbol Method |
| --- |

Gets the user\-visible name for a symbol. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static string GetLabelForSymbol(
	ForgeTypeId symbolTypeId
)
```

```
Public Shared Function GetLabelForSymbol ( 
	symbolTypeId As ForgeTypeId
) As String
```

```
public:
static String^ GetLabelForSymbol(
	ForgeTypeId^ symbolTypeId
)
```

```
static member GetLabelForSymbol : 
        symbolTypeId : ForgeTypeId -> string 
```

#### Parameters

symbolTypeId [ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)
:   Identifier of the symbol to get the user\-visible name.

#### Return Value

String 
Returns the user\-visible name for a symbol. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Symbol must have a definition. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The name is obtained in the current Revit language. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[LabelUtils Class](Label-Utils-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
