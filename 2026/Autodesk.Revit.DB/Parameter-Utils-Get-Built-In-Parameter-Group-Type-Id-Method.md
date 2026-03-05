# Parameter Utils Get Built In Parameter Group Type Id Method

Source: https://www.revitapidocs.com/2026/9cea4e68-53ab-c371-f8b2-b205d75b4ec8.htm

---

| Parameter Utils Get Built In Parameter Group Type Id Method |
| --- |

The parameter group identifier corresponding to the given built\-in parameter identifier. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static ForgeTypeId GetBuiltInParameterGroupTypeId(
	ForgeTypeId parameterTypeId
)
```

```
Public Shared Function GetBuiltInParameterGroupTypeId ( 
	parameterTypeId As ForgeTypeId
) As ForgeTypeId
```

```
public:
static ForgeTypeId^ GetBuiltInParameterGroupTypeId(
	ForgeTypeId^ parameterTypeId
)
```

```
static member GetBuiltInParameterGroupTypeId : 
        parameterTypeId : ForgeTypeId -> ForgeTypeId 
```

#### Parameters

parameterTypeId [ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)
:   The identifier to check.

#### Return Value

[ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm) 
The parameter group identifier. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A ForgeTypeId identifies a built\-in parameter if it corresponds to a valid BuiltInParameter value. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ParameterUtils Class](Parameter-Utils-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
