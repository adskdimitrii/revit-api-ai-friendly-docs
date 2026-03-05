# Label Utils Get Label For Unit Method

Source: https://www.revitapidocs.com/2026/96491567-d6a1-23ed-2d82-673d5b1dfc5b.htm

---

| Label Utils Get Label For Unit Method |
| --- |

Gets the user\-visible name for a unit. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static string GetLabelForUnit(
	ForgeTypeId unitTypeId
)
```

```
Public Shared Function GetLabelForUnit ( 
	unitTypeId As ForgeTypeId
) As String
```

```
public:
static String^ GetLabelForUnit(
	ForgeTypeId^ unitTypeId
)
```

```
static member GetLabelForUnit : 
        unitTypeId : ForgeTypeId -> string 
```

#### Parameters

unitTypeId [ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)
:   Identifier of the unit to get the user\-visible name.

#### Return Value

String 
Returns the user\-visible name for a unit. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Cannot find DisplayUnitTypeInfo for the given unit identifier. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The name is obtained in the current Revit language. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[LabelUtils Class](Label-Utils-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
